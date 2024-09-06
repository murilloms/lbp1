class Time:
    def __init__(self, nome, pais, campeonatos_nacionais, campeonatos_internacionais):
        self.nome = nome
        self.pais = pais
        self.campeonatos_nacionais = campeonatos_nacionais
        self.campeonatos_internacionais = campeonatos_internacionais

times = []

def add_time(nome, pais, campeonatos_nacionais, campeonatos_internacionais):
    novo_time = Time(nome, pais, campeonatos_nacionais, campeonatos_internacionais)
    times.append(novo_time)

def get_times():

    return times
