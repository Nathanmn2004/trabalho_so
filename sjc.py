
def sjc(lista_de_listas):
    lista_ordenada = sorted(lista_de_listas, key=lambda x: (x[0],x[1]))

    

   #VALOR TEMPO RESPOSTAS
    respostas = []
    i=0
    soma =0
    while 1:
        
        if i == len(lista_ordenada):
            break

        
        try:
            if ((lista_ordenada[i+1][1] < lista_ordenada[i][1]) and soma >= lista_ordenada[i+1][0]):
                aux = lista_ordenada[i].copy()
                lista_ordenada[i] = lista_ordenada[i+1].copy()
                lista_ordenada[i+1] = aux.copy()
        except:
            pass
        
        

        respostas.append(soma - lista_ordenada[i][0])
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

     
    
#VALOR TEMPO RETORNO
    respostas = []
    i=0
    soma =0
    while 1:
        
        if i == len(lista_ordenada):
            break
        

        respostas.append(soma - lista_ordenada[i][0]+ lista_ordenada[i][1])
        

        try:
            if ((lista_ordenada[i+1][1] < lista_ordenada[i][1]) and soma >= lista_ordenada[i+1][0]):
                aux = lista_ordenada[i].copy()
                lista_ordenada[i] = lista_ordenada[i+1].copy()
                lista_ordenada[i+1] = aux.copy()
        except:
            pass
        
        
        soma += lista_ordenada[i][1]
        
    
        i+=1

    
    nelem = len(respostas)
    sumresp = 0
    for valor in respostas:
        sumresp += valor
    tretorno = sumresp/nelem
    del respostas

    tespera = trespmedio 

    print(f"SJF {tretorno:.1f}, {trespmedio:.1f}, {tespera:.1f}")

        