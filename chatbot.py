import re
import random
from nltk.chat.util import Chat, reflections

class FociChatbot(Chat):
    def __init__(self):
        super().__init__([], reflections)

    def add(self, input, output):
        if isinstance(output, str):
            o = [output]
        else:
            o = output
        self._pairs.append((re.compile(input, re.IGNORECASE), o))

def add_response(input, output):
    f.add(input, output)

def converse():
    f.converse()

def respond(input):
    print(f.respond(input))

def reset():
    global f
    f = FociChatbot()

f = FociChatbot()

# Adicione todas as respostas antes de iniciar a conversa
add_response('Olá', 'Olá, como vai?')
add_response("Estou bem e você?", 'também estou bem')
add_response("Se é você que vai pagar", 'Eu tô dentro')
add_response('Eu gosto de (.*)', 'o que você gosta sobre ele?')
print("Digite quit para sair")
# Inicie a conversa depois de adicionar todas as respostas
converse()
