from agents.base_agent import BaseAgent

class Researcher(BaseAgent):
    def __init__(self):
        super().__init__(
            "Researcher",
            "Technical Fact-Finder",
            "Provide 3-5 specific facts about the topic provided. Use bullet points."
        )

class Writer(BaseAgent):
    def __init__(self):
        super().__init__(
            "Writer",
            "Professional Blogger",
            "Write a clear, engaging paragraph based ONLY on the facts provided by the Researcher."
        )

class Critic(BaseAgent):
    def __init__(self):
        super().__init__(
            "Critic",
            "Quality Assurance Editor",
            "Review the draft. Suggest one improvement, then provide the final polished version of the text."
        )