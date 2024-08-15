class Subject:
    def __init__(self):
        self._observers = []

    def adicionar_observer(self, observer):
        self._observers.append(observer)

    def remover_observer(self, observer):
        self._observers.remove(observer)

    def notificar_observers(self, time, jogador, minuto):
        for observer in self._observers:
            observer.update(time, jogador, minuto)
