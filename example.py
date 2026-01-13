# example.py
from main import run_orchestrator

if __name__ == "__main__":
    sample_task = "Write a brief blog post about the benefits of multi-agent AI systems"
    
    print(f"Running End-to-End Example for: {sample_task}\n")
    run_orchestrator(sample_task)