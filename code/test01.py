import nltk

sentenca = """As oito horas de manhã da terça-feira...
Carlos não estava sentindo-se muito bem!"""

palavras = nltk.word_tokenize(sentenca)

print(palavras)