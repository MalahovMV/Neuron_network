import math
from matplotlib import pyplot
from Window import Window
import random

def function(a, b, N):
    step = (b - a) / N
    input_vectors = [a]
    y_true = []
    while input_vectors[-1] < (2 * b - a):
        y_true.append((math.cos(input_vectors[-1]) ** 2 - 0.5))
        input_vectors.append((input_vectors[-1] + step))

    y_true.append(round(float((math.cos(input_vectors[-1])) ** 2 - 0.5), 3))
    return(input_vectors, y_true)

def find_rate_learning(y_true, size_window):
    good_rate = 0
    min_epochs = 3000
    for i in range(1000):
        rate = random.random()
        neuron = Window(1, y_true[:20], size_window)
        error = 1
        while error > (0.1 ** (10)):
            neuron.during_epochs()
            error = neuron.calculate_errors()

        if neuron.epochs < min_epochs:
            min_epochs = neuron.epochs
            good_rate = rate

    print(good_rate, min_epochs)

def main(size_window = 4):
    a = -1
    b = 0.5
    N = 20
    step = (b - a) / N
    size_window = size_window
    input_vectors, y_true = function(a, b, N)
    neuron = Window(1, y_true[:20], size_window)
    error = 1
    while error > (0.1 ** (10)):
        neuron.during_epochs()
        error = neuron.calculate_errors()

    x_probality = [input_vectors[20]]
    while x_probality[-1] < (2 * b - a):
       x_probality.append(round(float(x_probality[-1] + step), 3))

    print('Epochs=', neuron.epochs)
    print('W=', neuron.weight)
    print("Error=", neuron.error_on_last_epochs)
    y_probality = neuron.neuron_prediction(21)
    build_map(input_vectors, y_true, x_probality, y_probality)
    #find_rate_learning(y_true[20:], size_window)

def build_map(xlist, ylist, x_probality, y_probality):
    pyplot.plot(xlist, ylist)
    pyplot.plot(x_probality, y_probality)
    pyplot.grid(True)
    pyplot.savefig('123.png')
    pyplot.show()

def test_size_window():
    for i in range(3,17):
        print(i)
        try:
            main(i)

        except:
            print("Learning is impossible")

        print()

if __name__ == '__main__':
    main()
    test_size_window()

