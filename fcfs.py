def fcfs(lista_de_listas):
    
    lista_ordenada = sorted(lista_de_listas, key=lambda x: x[0])

    #VALOR TEMPO DE RESPOSTA
    respostas = []
    resp_retorno = []
    i=0
    soma =0
    while 1:
        
        if i == len(lista_ordenada):
            break

        respostas.append(soma - lista_ordenada[i][0])
        resp_retorno.append(soma - lista_ordenada[i][0] + lista_ordenada[i][1])
        soma += lista_ordenada[i][1]

        if respostas[0] != 0:
            respostas[0] = 0
        i+=1
  
    nelem = len(respostas)
    sumresp = 0
    for valor in respostas:
        sumresp += valor
    trespmedio = sumresp/nelem
    del respostas

    sumresp = 0
    for valor in resp_retorno:
        sumresp += valor
    tretorno = sumresp/nelem
    del resp_retorno

    tespera= trespmedio

    print(f"FCFS {tretorno:.1f}, {trespmedio:.1f}, {tespera:.1f}")
