from agents.specialized_agents import Researcher, Writer, Critic
from utils.logger import log_event

def run_orchestrator(user_prompt):
    # Establish Shared Memory / State
    state = {
        "user_request": user_prompt,
        "research": "",
        "draft": "",
        "final_output": ""
    }

    log_event("Orchestrator", f"Workflow started for topic: {user_prompt}")

    # 1. Sequence: Researcher
    researcher = Researcher()
    state["research"] = researcher.execute(state["user_request"])

    # 2. Sequence: Writer
    writer = Writer()
    state["draft"] = writer.execute(state["research"])

    # 3. Sequence: Critic
    critic = Critic()
    state["final_output"] = critic.execute(state["draft"])

    log_event("Orchestrator", "Workflow complete.")
    
    print("\n" + "="*50)
    print("FINAL CONSOLIDATED OUTPUT")
    print("="*50)
    print(state["final_output"])
    print("="*50)

if __name__ == "__main__":
    task = input("Enter a topic for the AI Team: ")
    if task:
        run_orchestrator(task)
    else:
        print("Please enter a valid topic.")