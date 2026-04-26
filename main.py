from dotenv import load_dotenv
load_dotenv()
from utils import load_logs
from agents import run_log_analysis, run_solution_research, run_resolution_planner

def main():
    print("--- Starting Incident Response Workflow ---")
    
    # 1. Ingest
    logs = load_logs()
    
    # 2. Agent 1
    print("[Agent 1] Analyzing Logs...")
    diagnosis = run_log_analysis(logs)
    
    # 3. Agent 2
    print("[Agent 2] Researching Solutions...")
    research = run_solution_research(diagnosis)
    
    # 4. Agent 3
    print("[Agent 3] Drafting Resolution Plan...")
    final_report = run_resolution_planner(diagnosis, research)
    
    # Output
    with open("incident_report.md", "w") as f:
        f.write(final_report)
    print("--- Workflow Complete. Report saved to incident_report.md ---")

if __name__ == "__main__":
    main()