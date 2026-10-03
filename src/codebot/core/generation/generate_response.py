from .model import tokenizer, model

def generate_response(prompt: str) -> str:
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs)
    input_length = inputs["input_ids"].shape[-1]
    generated_tokens = outputs[0][input_length:]
    response = tokenizer.decode(generated_tokens, skip_special_tokens=True)
    #print("INPUT LENGTH:", input_length)
    #print("OUTPUTS:", outputs)
    #print("GENERATED TOKENS:", generated_tokens)
    return (response)

