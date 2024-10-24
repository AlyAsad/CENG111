


def forward_pass(Network,X):

    import math

    def linear(Weights,X):
        
        length1 = len(Weights)
        length2 = len(Weights[0])
        result = [0]*length1
        
        for i in range(0,length1):

            for u in range(0,length2):
                result[i] += X[u]*Weights[i][u]

        return result
                

    def relu(X):

        length= len(X)

        for i in range(0,length):
            if X[i]<0:
                X[i]=0

        return X

    def sigm(X):

        length= len(X)

        for i in range(0,length):

            if X[i] <= -700:
                X[i] = 0

            elif X[i] >= 700:
                X[i] = 1

            else:
                X[i] = 1/(1+ math.exp(-X[i]))

        return X



    length = len(Network)
    index = 0

    while index < length:

        layer = Network[index]

        if type(layer) == type([]):
            X= linear(Network[index][1],X)

        else:
            underscore = layer.find("_")
            layer = layer[:underscore]

            if layer == "relu":
                X= relu(X)

            elif layer == "sigmoid":
                X= sigm(X)

        index += 1
    return X























        
