# -*- coding: utf-8 -*-	
import sys
import aimlManager

aimlMgr = aimlManager.aimlManager()

while True:

    text = sys.stdin.readline()
    text = text.strip()

    if text == "quit":
        print("---------------")
        print("- Fim de chat")
        print("---------------")
        break

    resposta = aimlMgr.mensagem(text)
    resposta = resposta.replace('\\n', '\n')
    if not resposta == "":
        print(">> " + resposta)
        print("---------------")
