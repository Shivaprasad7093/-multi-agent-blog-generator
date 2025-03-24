from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

class ReviewAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-4", temperature=0.5)

    def review_content(self, content):
        prompt = PromptTemplate(
            input_variables=["content"],
            template="Proofread and improve this content for clarity and grammar: {content}"
        )
        return self.llm(prompt.format(content=content))

if __name__ == "__main__":
    reviewer = ReviewAgent()
    sample_content = "AI in HR is effective but have challenges."
    print(reviewer.review_content(sample_content))
