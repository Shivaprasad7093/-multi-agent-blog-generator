from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

class ContentPlanner:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def generate_outline(self, topic):
        prompt = PromptTemplate(
            input_variables=["topic"],
            template="Create a detailed blog outline for the topic: {topic}"
        )
        return self.llm(prompt.format(topic=topic))

if __name__ == "__main__":
    planner = ContentPlanner()
    topic = "AI in HR"
    print(planner.generate_outline(topic))
