import math

class neuron:
    def __init__(self, rate_learn, y_true, input_x):
        self.rate_learn = rate_learn
        self.input_x = input_x
        self.y_true = y_true
        self.intermediant_values = []
        self.weights_first_segment = [[0, 0], [0, 0]]
        self.weights_end_segment = [0.5, 0.3]
        self.end_error = 0
        self.intermediant_error = [0, 0]
        self.y_calculate = 0
        self.net_first = []
        self.net_end = 0
        self.epoch = 0
        self.result_error = 0

    def activasion_function(self, net):
        return (1 - math.exp(-1 * net)) / (1 + math.exp(-1 * net))

    def calculate_values(self):
        self.net_first = []
        self.intermediant_values = []
        for i in range(len(self.weights_first_segment)):
            net = 0
            for j in range(len(self.weights_first_segment[i])):
                net += self.weights_first_segment[i][j] * self.input_x[j]

            self.intermediant_values.append(self.activasion_function(net))
            self.net_first.append(net)

        net = 0
        for i in range(len(self.intermediant_values)):
            net += self.intermediant_values[i] * self.weights_end_segment[i]

        self.net_end = net
        self.y_calculate = self.activasion_function(net)

    def calculate_error(self):
        self.result_error =self.y_true - self.y_calculate
        self.end_error = (self.y_true - self.y_calculate) * 0.5 * (1 - (self.activasion_function(self.net_end)) ** 2)
        self.intermediant_error = []
        for i in range(len(self.weights_end_segment)):
            self.intermediant_error.append(0.5 * (1 - (self.activasion_function(self.net_first[i])) ** 2) * (
            self.weights_end_segment[i] * self.end_error))

    def change_weights(self):
        for i in range(len(self.weights_first_segment)):
            for j in range(len(self.weights_first_segment[i])):
                self.weights_first_segment[i][j] += self.rate_learn * self.intermediant_error[i] * self.input_x[j]

        for i in range(len(self.weights_end_segment)):
            self.weights_end_segment[i] += self.rate_learn * self.end_error * self.intermediant_values[i]

        self.epoch += 1