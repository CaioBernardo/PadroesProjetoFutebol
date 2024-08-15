from abc import ABC, abstractmethod
from typing import List

class Componente(ABC):
    @abstractmethod
    def operacao(self) -> str:
        pass

class Jogador(Componente):
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def operacao(self) -> str:
        return self.nome

class Time(Componente):
    def __init__(self) -> None:
        self._componentes: List[Componente] = []

    def adicionar(self, componente: Componente) -> None:
        self._componentes.append(componente)

    def remover(self, componente: Componente) -> None:
        self._componentes.remove(componente)

    def operacao(self) -> str:
        resultados = [componente.operacao() for componente in self._componentes]
        return f"Equipe: {', '.join(resultados)}"
