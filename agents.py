import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()

# Check for Groq Key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file!")

# Initialize Groq Llama 3.3
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    groq_api_key=api_key,
    temperature=0.1
)

search_tool = DuckDuckGoSearchRun()

def run_log_analysis(logs):
    """Agent 1: Extracts root cause and evidence."""
    prompt = f"""
    Analyze these production logs:
    {logs}
    
    Output a JSON object exactly like this:
    {{
        "root_cause": "summary of the issue",
        "evidence": ["specific log line 1", "specific log line 2"],
        "search_query": "specific technical keywords for a fix",
        "confidence": "High/Medium/Low"
    }}
    """
    response = llm.invoke(prompt)
    # Clean markdown if model adds it
    content = response.content.replace('```json', '').replace('```', '').strip()
    return json.loads(content)

def run_solution_research(analysis_data):
    """Agent 2: Non-LLM primary discovery via Search."""
    query = analysis_data.get("search_query", "linux api error fix")
    print(f"[*] Agent 2 (Research) Searching: {query}")
    results = search_tool.run(query)
    return results

def run_resolution_planner(analysis, research):
    """Agent 3: Creates the final runbook."""
    prompt = f"""
    Diagnosis: {analysis['root_cause']}
    Log Evidence: {analysis['evidence']}
    Web Research: {research}
    
    Create a step-by-step resolution plan:
    1. Immediate Fix
    2. Verification Steps
    3. Rollback Instructions
    """
    response = llm.invoke(prompt)
    return response.content




# import os
# from dotenv import load_dotenv, find_dotenv
# from langchain_groq import ChatGroq
# from langchain_community.tools import DuckDuckGoSearchRun
# # Try to find and load .env robustly
# load_dotenv(find_dotenv(usecwd=True))

# api_key = os.environ.get("GROQ_API_KEY")
# if not api_key:
#     # Fallback: manually read the .env file if load_dotenv is failing for some reason
#     try:
#         with open(os.path.join(os.path.dirname(__file__), ".env"), "r") as f:
#             for line in f:
#                 if line.startswith("GROQ_API_KEY="):
#                     api_key = line.strip().split("=", 1)[1].strip()
#                     os.environ["GROQ_API_KEY"] = api_key
#     except Exception as e:
#         pass

# if not api_key:
#     raise ValueError("GROQ_API_KEY could not be found! Please ensure it is set in the .env file.")


# llm = ChatGroq(
#     model_name="llama-3.3-70b-versatile",
#     groq_api_key=api_key,
#     temperature=0.1
# )

# def run_log_analysis(log_text):
#     prompt = f"Analyze these Linux logs. Identify root cause, provide evidence snippets, and confidence level:\n\n{log_text}"
#     response = llm.invoke(prompt)
#     return response.content

# def run_solution_research(diagnosis):
#     search = DuckDuckGoSearchRun()
#     # Extract keywords from diagnosis for better search
#     query = f"site:stackoverflow.com OR site:nginx.org fix for: {diagnosis[:200]}"
#     results = search.run(query)
#     return results

# def run_resolution_planner(diagnosis, research):
#     prompt = f"""
#     Based on Diagnosis: {diagnosis}
#     And Research: {research}
    
#     Create a production-ready Resolution Plan:
#     1. Best Solution
#     2. Step-by-step instructions
#     3. Pre-checks and Post-fix validation
#     4. Rollback plan
#     """
#     response = llm.invoke(prompt)
#     return response.content