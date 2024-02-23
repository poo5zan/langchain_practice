from langchain_community.llms import Ollama
llm = Ollama(model="llama2")

p = llm.invoke("how can langsmith help with testing?")
print('response ', p)