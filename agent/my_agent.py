from langchain_g4f import G4FLLM
from g4f import models
from .motivational_quote_tool import generate_motivational_quote
from .topic_description_tool import describe_topic


class CustomAgent:
    def __init__(self):
        self.llm = G4FLLM(model=models.gpt_35_turbo)

    def generate_response(self, prompt):
        if "quote" in prompt.lower():
            return generate_motivational_quote(self.llm)
        elif "describe" in prompt.lower():
            topic = self.extract_topic_from_prompt(prompt)
            return describe_topic(topic, self.llm)
        else:
            return ("I can help you to generate  motivational quotes or describing any topic. Kindly specify your "
                    "request.")

    def extract_topic_from_prompt(self, prompt):
        return prompt.split('describe')[-1].strip()
