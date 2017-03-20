import math
from matplotlib import mlab, pyplot
from Window import Window

def function(a, b, N, size_window):
    step = (b - a) / N
    input_vectors = [a]
    input_matrix = []
    y_true = []
    while input_vectors[-1] < b:
        y_true.append(round(float((math.cos(input_vectors[-1])) ** 2 - 0.5), 3))
        input_vectors.append(round(float(input_vectors[-1] + step), 3))

    y_true.append(round(float((math.cos(input_vectors[-1])) ** 2 - 0.5), 3))
    for i in range(len(y_true) - size_window):
        input_matrix.append(list((1, y_true[i], y_true[i + 1], y_true[i + 2], y_true[i + 3])))

    return(input_vectors, y_true, input_matrix)

def main():
    a = -1
    b = 0.5
    N = 19
    step = (b - a) / N
    size_window = 4
    input_vectors, y_true, input_matrix = function(a, b, N, size_window - 1)
    neuron = Window(1, input_matrix)
    neuron.during_epochs()
    #x_probably = 0.5 + step
    print(neuron.weight)
    build_map(input_vectors, y_true)

def build_map(xlist, ylist):
    pyplot.plot(xlist, ylist)
    pyplot.grid(True)
    pyplot.savefig('123.png')
    pyplot.show()


if __name__ == '__main__':
    main()

