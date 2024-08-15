from subject import Subject

class GerenciadorDeCompeticoes(Subject):
    def __init__(self):
        super().__init__()
        self.gols = []

    def registrar_gol(self, time, jogador, minuto):
        self.gols.append((time, jogador, minuto))
        self.notificar_observers(time, jogador, minuto)

    def exibir_gols(self):
        for gol in self.gols:
            time, jogador, minuto = gol
            print(f"{time}: {jogador} aos {minuto} minutos")
