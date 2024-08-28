from __future__ import annotations 
from random import randint



class Matriz:
    def __init__(self, rows,cols) -> None:
        self.rows = rows
        self.cols = cols

        self.data = []


        for c in range(self.rows):
            arr = []

            for c in range(self.cols):
                n = randint(1,10)
                arr.append(n)
            
            self.data.append(arr)

    

    def add(A: Matriz, B : Matriz):
        matriz =  Matriz(A.rows,B.cols)

        for i in range(len(A.data)):
            for j in range(len(A.data[i])):
                matriz.data[i][j] = A.data[i][j] + B.data[i][j]
        
        return matriz
        



    def sub(A: Matriz, B : Matriz):
        matriz =  Matriz(A.rows,B.cols)

        for i in range(len(A.data)):
            for j in range(len(A.data[i])):
                matriz.data[i][j] = A.data[i][j] - B.data[i][j]
        
        return matriz
    
    def mult(A: Matriz, B: Matriz):
        if A.cols != B.rows:
            raise ValueError("Number of columns in A must equal number of rows in B")
        
        result = Matriz(A.rows, B.cols)
        
        for i in range(A.rows):
            for j in range(B.cols):
                sum = 0
                for k in range(A.cols):
                    sum += A.data[i][k] * B.data[k][j]
                result.data[i][j] = sum
        
        return result



#self.data[id_i][id_n] = self.data[id_i][id_n] + b.data[id_i][id_n]



m1 = Matriz(2,2)
m2 = Matriz(2,2)


print(m1.data)
print(m2.data)
m3 =Matriz.mult(m1,m2)

print(m3.data)

    
