from builder import ConstrutorDeTime, Jogador, Tecnico
from observer import Comentarista, Torcedor
from gerenciador import GerenciadorDeCompeticoes

def main():
    # Criando os times
    jogadores_flamengo_titulares = [
        Jogador("Diego Alves", "Goleiro"),
        Jogador("Rafinha", "Lateral Direito"),
        Jogador("Rodrigo Caio", "Zagueiro"),
        Jogador("Pablo Marí", "Zagueiro"),
        Jogador("Filipe Luís", "Lateral Esquerdo"),
        Jogador("Willian Arão", "Volante"),
        Jogador("Gerson", "Meia"),
        Jogador("Arrascaeta", "Meia"),
        Jogador("Everton Ribeiro", "Meia"),
        Jogador("Gabigol", "Atacante"),
        Jogador("Bruno Henrique", "Atacante")
    ]

    tecnico_flamengo = Tecnico("Jorge Jesus")

    jogadores_river_plate_titulares = [
        Jogador("Franco Armani", "Goleiro"),
        Jogador("Gonzalo Montiel", "Lateral Direito"),
        Jogador("Lucas Martínez Quarta", "Zagueiro"),
        Jogador("Javier Pinola", "Zagueiro"),
        Jogador("Milton Casco", "Lateral Esquerdo"),
        Jogador("Enzo Pérez", "Volante"),
        Jogador("Nicolás De La Cruz", "Meia"),
        Jogador("Leo Ponzio", "Volante"),
        Jogador("Gonzalo Martínez", "Meia"),
        Jogador("Matías Suárez", "Atacante"),
        Jogador("Rafael Santos Borré", "Atacante")
    ]

    tecnico_river_plate = Tecnico("Marcelo Gallardo")

    # Criando times usando o ConstrutorDeTime
    flamengo = ConstrutorDeTime().nome_time("Flamengo").tecnico(tecnico_flamengo).adicionar_jogadores(jogadores_flamengo_titulares).construir()
    river_plate = ConstrutorDeTime().nome_time("River Plate").tecnico(tecnico_river_plate).adicionar_jogadores(jogadores_river_plate_titulares).construir()

    # Exibindo os times
    flamengo.exibir_time()
    print()
    river_plate.exibir_time()
    print()

    # Criando o gerenciador de competições e adicionando observers
    gerenciador = GerenciadorDeCompeticoes()
    comentarista = Comentarista()
    torcedor = Torcedor()

    gerenciador.adicionar_observer(comentarista)
    gerenciador.adicionar_observer(torcedor)

    # Simulando gols
    gerenciador.registrar_gol("River Plate", "Rafael Santos Borré", 14)
    gerenciador.registrar_gol("Flamengo", "Gabigol", 89)
    gerenciador.registrar_gol("Flamengo", "Gabigol", 92)

    # Exibindo informações dos gols
    print("Informações do Jogo:")
    print("Fase: Final")
    print("Placar: Flamengo 2x1 River Plate")
    print("\nGols da partida:")
    gerenciador.exibir_gols()

if __name__ == "__main__":
    main()
