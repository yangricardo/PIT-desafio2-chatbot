# -*- coding: utf-8 -*-
import aiml
import time
import random


class aimlManager():
    # Create the kernel and learn AIML files

    def __init__(self):
        self.kernel = aiml.Kernel()
        self.kernel.learn("script.aiml")
        print(self.kernel.respond("START"))

    def mensagem(self, text):
        return self.kernel.respond(text)
