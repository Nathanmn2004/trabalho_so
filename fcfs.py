def fcfs(lista_de_listas):
    
    # Ordena a lista de processos com base no tempo de chegada
    lista_ordenada = sorted(lista_de_listas, key=lambda x: x[0])

    # Inicializa listas para armazenar os tempos de resposta e retorno
    respostas = []
    resp_retorno = []
    
    # Inicializa variáveis de controle
    soma = lista_ordenada[0][0]  # Inicia a soma no tempo de chegada do primeiro processo
    i = 0
    
    while i < len(lista_ordenada):
        
        # Ajusta 'soma' caso o próximo processo chegue depois do término do processo atual
        if soma < lista_ordenada[i][0]:
            soma = lista_ordenada[i][0]

        # Calcula o tempo de resposta
        respostas.append(soma - lista_ordenada[i][0])

        # Calcula o tempo de retorno
        resp_retorno.append(soma - lista_ordenada[i][0] + lista_ordenada[i][1])

        # Atualiza a soma com a duração do processo atual
        soma += lista_ordenada[i][1]
        
        i += 1
  
    # Calcula os tempos médios
    nelem = len(respostas)
    
    trespmedio = sum(respostas) / nelem
    tretorno = sum(resp_retorno) / nelem
    tespera = trespmedio

    # Exibe os resultados
    print(f"FCFS {tretorno:.1f}, {trespmedio:.1f}, {tespera:.1f}")