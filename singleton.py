class SingletonMeta(type):
    _instancias = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instancias:
            instancia = super().__call__(*args, **kwargs)
            cls._instancias[cls] = instancia
        return cls._instancias[cls]


class GerenciadorDeCompeticoes(metaclass=SingletonMeta):
    def __init__(self):
        self.competicoes = []

    def adicionar_competicao(self, competicao):
        self.competicoes.append(competicao)

    def listar_competicoes(self):
        print("Competições:")
        for competicao in self.competicoes:
            print(f"- {competicao}")


if __name__ == "__main__":
    # Teste do Singleton
    g1 = GerenciadorDeCompeticoes()
    g2 = GerenciadorDeCompeticoes()

    if id(g1) == id(g2):
        print("Singleton funciona, ambas as variáveis contêm a mesma instância.")
    else:
        print("Singleton falhou, as variáveis contêm instâncias diferentes.")
