from Neuron import neuron

def main(rate_learn):
    rate_learn = rate_learn
    e = 0.00001
    y_true = 0.3
    input_x = [1, 2]
    network = neuron(rate_learn, y_true, input_x)
    while True:
        network.calculate_values()
        network.calculate_error()
        print("Epoch= %2d" % network.epoch, "  y=%7F" % network.y_calculate, '  Error=', network.result_error)
        if abs(network.result_error) < e: break
        network.change_weights()

    #print(network.y_calculate, network.epoch)

if __name__ == '__main__':
    main(1)