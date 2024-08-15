from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Observer:
    def update(self, time, jogador, minuto):
        raise NotImplementedError("O método update deve ser implementado.")

class Comentarista(Observer):
    def update(self, time, jogador, minuto):
        print(f"Comentarista: Gol do {time}! {jogador} marcou aos {minuto} minutos.")

class Torcedor(Observer):
    def update(self, time, jogador, minuto):
        print(f"Torcedor: Gol do {time}! {jogador} fez aos {minuto} minutos. Que emoção!")
