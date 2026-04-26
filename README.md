# Phoneme Incident Response 

An automated, AI-driven Site Reliability Engineering (SRE) tool that accelerates the incident response process. When production goes down, this system ingests raw logs, diagnoses the root cause, searches the web for technical solutions, and automatically drafts a comprehensive Incident Resolution Plan.

##  Architecture

The workflow is powered by **LangChain** and **Groq (Llama 3.3)**, operating through a three-agent pipeline:

1. **Agent 1: Log Analysis** 
   - Ingests `app-error.log`, `nginx-access.log`, and `nginx-error.log`.
   - Diagnoses the root cause, extracts exact log snippets as evidence, and determines confidence levels.
2. **Agent 2: Solution Research**
   - Uses the `DuckDuckGoSearchRun` tool to query the web (e.g., StackOverflow, Nginx docs) based on the specific technical diagnosis to find industry-standard fixes.
3. **Agent 3: Resolution Planner**
   - Synthesizes the log diagnosis and search research into a formal, actionable Markdown Runbook containing immediate fixes, verification steps, and a rollback plan.

## Tech Stack

- **Python 3**
- **LangChain** (Agent framework)
- **Groq API** (Fast LLM Inference using `llama-3.3-70b-versatile`)
- **DuckDuckGo Search** (Live web research)
- **python-dotenv** (Environment variable management)

##  Getting Started

### Prerequisites

You need a free API key from [Groq Console](https://console.groq.com/keys).

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ayush-pandey047/phoneme-incident-response.git
   cd phoneme-incident-response
   ```

2. **Set up a Virtual Environment (Optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install langchain-groq python-dotenv duckduckgo-search
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in the root directory (or edit the existing one) and add your Groq API key:
   ```env
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```

## Usage

To run the automated incident triage, simply execute the main script:

```bash
python main.py
```

### Output

The system will print its progress to the console:
```text
--- Starting Incident Response Workflow ---
[Agent 1] Analyzing Logs...
[Agent 2] Researching Solutions...
[*] Agent 2 (Research) Searching: sqlalchemy connection pool exhaustion session leak
[Agent 3] Drafting Resolution Plan...
--- Workflow Complete. Report saved to incident_report.md ---
```

Once complete, a new file named `incident_report.md` will be generated in your directory containing the full step-by-step resolution plan.

## File Structure

- `main.py` - The entry point that orchestrates the agent workflow.
- `agents.py` - Contains the LangChain setup and the prompts for Agents 1, 2, and 3.
- `utils.py` - Helper functions to load and concatenate the raw log files.
- `logs/` - Directory containing the raw production logs (`app-error.log`, `nginx-access.log`, `nginx-error.log`).
- `incident_report.md` - The generated output runbook (created after running the script).
