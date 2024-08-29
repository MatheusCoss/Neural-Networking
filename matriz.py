from __future__ import annotations 
from random import randint, random
import math
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

class Matriz:
    def __init__(self, rows,cols) -> None:
        self.rows = rows
        self.cols = cols

        self.data = []


        for c in range(self.rows):
            arr = []
            for c in range(self.cols):
                arr.append(0)
            
            self.data.append(arr)
    

    def rand(self):
        self.data = []
        for c in range(self.rows):
            arr = []

            for c in range(self.cols):
                n = random() * 2 - 1
                arr.append(n)
            self.data.append(arr)
    

    def print(self):
        print(self.data)
    

    def arryToMatrix(arr):
        matriz = Matriz(len(arr), 1)

        for i in range(len(arr)):
            matriz.data[i][0] = arr[i]
        
        return matriz
    

    def set_sigmoid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = sigmoid(self.data[i][j])


    

    def add(A: Matriz, B : Matriz) -> Matriz:
        matriz =  Matriz(A.rows,B.cols)

        for i in range(len(A.data)):
            for j in range(len(A.data[i])):
                matriz.data[i][j] = A.data[i][j] + B.data[i][j]
        
        return matriz
        



    def sub(A: Matriz, B : Matriz) -> Matriz:
        matriz =  Matriz(A.rows,B.cols)

        for i in range(len(A.data)):
            for j in range(len(A.data[i])):
                matriz.data[i][j] = A.data[i][j] - B.data[i][j]
        
        return matriz
    
    def mult(A: Matriz, B: Matriz) -> Matriz:
        #if A.cols != B.rows:
            #raise ValueError("Numero de colunas do A não é igual ao número de linhas do B")
        
        result = Matriz(A.rows, B.cols)
        
        for i in range(A.rows):
            for j in range(B.cols):
                sum = 0
                for k in range(A.cols):
                    sum += A.data[i][k] * B.data[k][j]
                result.data[i][j] = sum
        
        return result



#self.data[id_i][id_n] = self.data[id_i][id_n] + b.data[id_i][id_n]


    
