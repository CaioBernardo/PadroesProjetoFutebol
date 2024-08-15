from typing import List, Dict

class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

class Tecnico:
    def __init__(self, nome):
        self.nome = nome

class Time:
    def __init__(self, nome, tecnico, jogadores):
        self.nome = nome
        self.tecnico = tecnico
        self.jogadores = jogadores

    def exibir_time(self):
        print(f"Time: {self.nome}")
        print(f"Técnico: {self.tecnico.nome}")
        print("Jogadores:")
        for jogador in self.jogadores:
            print(f"{jogador.nome} - {jogador.posicao}")

class ConstrutorDeTime:
    def __init__(self):
        self._time = Time(None, None, [])

    def nome_time(self, nome):
        self._time.nome = nome
        return self

    def tecnico(self, tecnico):
        self._time.tecnico = tecnico
        return self

    def adicionar_jogadores(self, jogadores):
        self._time.jogadores = jogadores
        return self

    def construir(self):
        return self._time
