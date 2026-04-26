from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
import os

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GEMINI_API_KEY"))

def run_log_analysis(log_text):
    prompt = f"Analyze these Linux logs. Identify root cause, provide evidence snippets, and confidence level:\n\n{log_text}"
    response = llm.invoke(prompt)
    return response.content

def run_solution_research(diagnosis):
    search = DuckDuckGoSearchRun()
    # Extract keywords from diagnosis for better search
    query = f"site:stackoverflow.com OR site:nginx.org fix for: {diagnosis[:200]}"
    results = search.run(query)
    return results

def run_resolution_planner(diagnosis, research):
    prompt = f"""
    Based on Diagnosis: {diagnosis}
    And Research: {research}
    
    Create a production-ready Resolution Plan:
    1. Best Solution
    2. Step-by-step instructions
    3. Pre-checks and Post-fix validation
    4. Rollback plan
    """
    response = llm.invoke(prompt)
    return response.content