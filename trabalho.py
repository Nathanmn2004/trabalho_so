from fcfs import fcfs
from sjc import sjc
from rr import round_robin

chegadas = []
tamanhos = []

with open('dados.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()

        tempo_chegada, tempo_duracao = linha.split()

        chegadas.append(float(tempo_chegada))
        tamanhos.append(float(tempo_duracao))

lista_combinada = [[chegada, tamanho] for chegada, tamanho in zip(chegadas, tamanhos)]

fcfs(lista_combinada)
sjc(lista_combinada)
round_robin(lista_combinada)