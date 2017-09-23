# -*- coding: utf-8 -*-
import aiml
import time
import random


class aimlManager():
    # Create the kernel and learn AIML files

    def __init__(self):
        self.kernel = aiml.Kernel()
        self.kernel.learn("script_consumidor.aiml")
        print(self.kernel.respond("INICIO"))

    def mensagem(self, text):
        return self.kernel.respond(text)
