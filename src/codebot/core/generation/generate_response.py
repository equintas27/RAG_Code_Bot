from .model import tokenizer, model

def generate_response(prompt: str) -> str:
    inputs = tokenizer(prompt)
    outputs = model.generate(inputs)

