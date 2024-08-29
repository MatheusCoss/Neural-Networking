from matriz import Matriz
import math




class RedeNeural:
    def __init__(self, i_nodes, h_nodes, o_nodes):
        self.i_nodes = i_nodes
        self.h_nodes = h_nodes
        self.o_nodes = o_nodes

        self.bias_ih = Matriz(self.h_nodes, 1)
        self.bias_ih.rand()
        self.bias_ho = Matriz(self.o_nodes, 1)
        self.bias_ho.rand()

        self.weights_ih = Matriz(self.h_nodes, self.i_nodes)
        self.weights_ih.rand()
        self.weights_ho = Matriz(self.o_nodes, self.h_nodes)
        self.weights_ho.rand()



    def feedforward(self, imp):

        # Input para Hidden Layer
        minput = Matriz.arryToMatrix(imp)
        print(minput.data)

        hidden = Matriz.mult(self.weights_ih, minput)
        hidden = Matriz.add(hidden,self.bias_ih)

        hidden.set_sigmoid()

        # Hidden para Output Layer
        output = Matriz.mult(self.weights_ho, hidden)
        output = Matriz.add(output, self.bias_ho)
        output.set_sigmoid()

        print(output.data)
        



nn = RedeNeural(1,3,1)


nn.feedforward([1,2,65,43])

