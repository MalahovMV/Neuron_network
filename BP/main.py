from Neuron import neuron

def main(rate_learn):
    rate_learn = rate_learn
    y_true = 0.3
    input_x = [1, 2]
    network = neuron(rate_learn, y_true, input_x)
    while True:
        network.calculate_values()
        network.calculate_error()
        if abs(network.result_error) < 0.00001: break
        network.change_weights()

    print(network.y_calculate, network.epoch)

if __name__ == '__main__':
    main(1)