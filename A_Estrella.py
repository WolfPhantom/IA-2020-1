grafo=[[(1,75),(7,140),(3,118)],
       [(0,75),(2,71)],
       [(1,71),(7,151)],
       [(0,118),(4,111)],
       [(3,111),(5,70)],
       [(4,70),(6,75)],
       [(5,75),(9,120)],
       [(0,140),(2,151),(8,80),(11,99)],
       [(7,80),(9,146),(10,97)],
       [(6,120),(8,146),(10,138)],
       [(8,97),(9,138),(12,101)],
       [(7,11),(12,211)],
       [(10,101),(11,211),(13,90),(14,85)],
       [(12,90)],
       [(12,85),(15,142),(18,98)],
       [(14,152),(16,92)],
       [(15,92),(15,87)],
       [(16,87)],
       [(14,98),(19,86)],
       [(18,86)]
       ]

h = [366,374,380,329,244,241,242,253,193,160,98,178,0,77,80,199,226,234,151,161 ]
def volor_recorrido(grafo1,camino):
    camino_recorrtido_v=0

    contador=0
    for i in camino:
        for n,w in grafo1[i]:
            if contador==len(camino)-1:
                break        
            if n==camino[contador+1] :
                camino_recorrtido_v+=w
        contador+=1
        
    return camino_recorrtido_v
def A(grafo,inicio,final):
    f=[]
    Abiertos=[inicio]
    Cerrados=[]
    f_inicial=h[inicio]
    solucion=[]
    f.append(f_inicial)
    MejorNodo_v_A=-1
    print("Primera Iteracion")
    print("Abiertos: ", Abiertos)
    print("Cerrados: " , Cerrados)
    print("F de los abiertos: " , f)
    print("===============")
    while solucion==[]:
        if Abiertos==[]:
            return False
        else:
            MejorNodo_I_F=f.index(min(f))
            MejorNodo_v_A=Abiertos[MejorNodo_I_F]
            
            Abiertos.remove(MejorNodo_v_A)
            Cerrados.append(MejorNodo_v_A)
            
        if MejorNodo_v_A==final:
            print("Encontrado")
            print("Abiertos: ", Abiertos)
            print("Cerrados: " , Cerrados)
            return True
        else:
            f.remove(min(f))
            for n,w in grafo[MejorNodo_v_A]:
                
                if n not in Abiertos and n not in Cerrados:
                    Abiertos.append(n)
                    g_n=volor_recorrido(grafo,Cerrados)
                    Fl=h[n]+ w+g_n
                    f.append(Fl)
                
        print("MejorNodo: " , MejorNodo_v_A)  
        
        print("Abiertos: ", Abiertos)
        print("Cerrados: " , Cerrados)
        print("F de los abiertos: " , f)
        print("========================")
        """if contador ==5:
            break
        contador+=1"""
        
camino=[0,7]
"""g_n=volor_recorrido(grafo,camino)
print(g_n)"""
A(grafo,0,12)
