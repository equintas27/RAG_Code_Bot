
def build_prompt(question: str, context: str) -> str:
   instruction = "Responda a questão, baseando - se no context que foi passado, caso a resposta não esteja no contexto, diz que a informação não foi encontrada"
   prompt = f"{instruction} Contexto: {context} Pergunta: {question}"
   return (prompt)