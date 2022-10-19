#import module numpy
import numpy as np

#deklarasi varibel 
inputs = [2, 10, 1, 3, 9, 4.5, 8, 7, 7.5, 6]

#deklarasi bobot per neuron
weights = [1.1, 1.3, 1.5, 1.7, 2.9, -3.2, -3.1, 0.3, 0.2, -0.1]

#jumlah bias per neuron
bias = 9

#kalkulasi output dengan menggunakan bantuan module numpy
output = np.dot(weights, inputs) + bias

#tampilkan output
print(output)

#develop @mahendrarendi
