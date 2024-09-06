from models import add_time, get_times

def adicionar_time(nome, pais, campeonatos_nacionais, campeonatos_internacionais):
    add_time(nome, pais, campeonatos_nacionais, campeonatos_internacionais)

def listar_times():
    return get_times()
