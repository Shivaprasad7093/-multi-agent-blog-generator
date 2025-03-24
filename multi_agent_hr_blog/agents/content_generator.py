from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

class ContentGenerator:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def generate_blog(self, outline):
        prompt = PromptTemplate(
            input_variables=["outline"],
            template="Write a detailed, engaging, and SEO-friendly blog based on this outline: {outline}"
        )
        return self.llm(prompt.format(outline=outline))

if __name__ == "__main__":
    generator = ContentGenerator()
    sample_outline = "Introduction -> AI in HR -> Benefits -> Conclusion"
    print(generator.generate_blog(sample_outline))
