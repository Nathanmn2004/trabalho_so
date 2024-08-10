from fcfs import fcfs
from sjc import sjc

chegadas = []
tamanhos = []
    
with open('dados.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()  # Remove espaços em branco e quebras de linha
        if linha == "0 0":
            break
        numero1, numero2 = linha.split()
        chegadas.append(float(numero1))
        tamanhos.append(float(numero2))
    


lista_combinada = [[chegada, tamanho] for chegada, tamanho in zip(chegadas, tamanhos)]
    





fcfs(lista_combinada)
sjc(lista_combinada)