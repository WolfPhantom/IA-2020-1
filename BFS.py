# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 09:14:04 2020

@author: USER
"""


grafo=[[(1,374),(7,253),(3,329)],
       [(0,366),(2,380)],
       [(1,374),(7,253)],
       [(0,366),(4,244)],
       [(3,329),(5,241)],
       [(4,244),(6,242)],
       [(5,241),(9,160)],
       [(0,366),(2,380),(8,193),(11,178)],
       [(7,253),(9,160),(10,98)],
       [(6,242),(8,193),(10,98)],
       [(8,193),(9,160),(12,0)],
       [(7,253),(12,0)],
       [(10,98),(11,178),(13,77),(14,80)],
       [(12,0)],
       [(12,0),(15,199),(18,151)],
       [(14,80),(16,226)],
       [(15,199),(15,234)],
       [(16,226)],
       [(14,80),(19,161)],
       [(18,151)]
       ]
grafo2=[[(1,374),(7,253),(3,329)],
       [(0,366),(2,380)]]
"""minimo=990
for i in grafo2[0]:
    if i[1]<minimo:
        minimo=i[1]"""
        
    
def FirstBest(grafo,inicio):
    camino=[]
    camino.append(inicio)
    minimo=999
    siguiente=inicio
    while(minimo!=0):
        minimo=999
        for i in grafo[siguiente]:
            if i[1]<minimo:
                siguiente=i[0]
                minimo=i[1]
        
        camino.append(siguiente)   
    print(camino)
for i in range(0,20):
    FirstBest(grafo,i)   

        