from collections import deque

class Processo:
    def __init__(self, t_chegada, t_duracao):
        self.t_chegada = t_chegada
        self.t_duracao = t_duracao

        self.t_resposta = None
        self.t_espera = 0

        self.t_saida = t_chegada


def round_robin(lista_processos):
    
    q_total = len(lista_processos)

    # Organiza os processos em ordem de chegada e cria sua estrutura
    lista_processos = sorted(lista_processos, key=lambda t_chegada: t_chegada[0])

    for i in range(q_total):
        lista_processos[i] = Processo(lista_processos[i][0], lista_processos[i][1])

    # Cria uma estrutura fila com o primeiro da lista de chegada
    fila_de_prontos = deque()

    # Configura o escalonador
    t = lista_processos[0].t_chegada
    processo = None
    q = 0
    q_processos = 0
    q_encerrados = 0

    media_retorno = 0
    media_resposta = 0
    media_espera = 0

    while (q_encerrados < q_total):
        # Insere na fila de prontos os processos que chegaram
        for _processo in lista_processos[q_processos : q_total]:
            if (t == _processo.t_chegada):
                fila_de_prontos.append(_processo)
                q_processos += 1
            else:
                break

        #print(t, processo, fila_de_prontos)
        if (q == 0):
            if (processo != None):
                # Retorna atual processo à fila de prontos
                processo.t_saida = t
                fila_de_prontos.append(processo)

            # Tira da fila de prontos o processo a ser usado
            processo = fila_de_prontos.popleft()

            # Calcula o tempo de resposta
            if (processo.t_resposta == None):
                processo.t_resposta = t - processo.t_chegada 

            # Calcula o tempo de espera
            processo.t_espera += t - processo.t_saida
            
        # Atualiza os valores de tempo
        t += 1
        q = (q+1) % 2
        if (q < 2):
            processo.t_duracao -= 1

        # Produz o resultado se o processo terminou
        if (processo.t_duracao == 0):
            media_retorno += t - processo.t_chegada
            media_resposta += processo.t_resposta
            media_espera += processo.t_espera
            q_encerrados += 1
            q = 0
            processo = None

    media_retorno /= q_total
    media_resposta /= q_total
    media_espera /= q_total

    print(f"RR {media_retorno:.1f}, {media_resposta:.1f}, {media_espera:.1f}")