
def build_prompt(question: str, context: str) -> str:
   instruction = "Responda a questão, baseando - se no contexto que foi passado, caso a resposta não esteja no contexto, diz que a informação não foi encontrada"
   prompt = f"{instruction}\n\nContexto:\n{context}\n\nPergunta:\n{question}"
   return (prompt)