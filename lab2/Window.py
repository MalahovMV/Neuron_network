class Window:

    def __init__(self, rate_learning, y_true, size_window):
        self.y_true = y_true
        self.rate_learning = rate_learning
        self.epochs = 0
        self.weight = [0, 0, 0, 0]
        self.error_on_last_epochs = 0
        self.size_window = size_window
        self.vector_ans_on_epoch = []

    def during_epochs(self):
        for i in range(self.size_window, len(self.y_true) - 1):
            y_calculate = 0
            for j in range(self.size_window):
                y_calculate += self.y_true[-1 * self.size_window + i + j]*self.weight[j]

            for j in range(self.size_window):
                self.weight[j] += (self.y_true[i] - y_calculate) * self.rate_learning * self.y_true[-1 * self.size_window + i + j]

        self.epochs += 1

    def neuron_prediction(self, number):
        y_prediction = self.y_true[-1 * self.size_window:]
        for i in range(number):
            next_prediction = 0
            for j in range(self.size_window):
                next_prediction += y_prediction[-1 * self.size_window + j]*self.weight[j]

            y_prediction.append(next_prediction)

        return y_prediction[self.size_window:]

    def calculate_errors(self):
        self.error_on_last_epochs = 0
        self.vector_ans_on_epoch = []
        for i in range(self.size_window, len(self.y_true) - 1):
            y_calculate = 0
            for j in range(self.size_window):
                y_calculate += self.y_true[-1 * self.size_window + i + j] * self.weight[j]

            self.vector_ans_on_epoch.append(y_calculate)

        for i in range(len(self.vector_ans_on_epoch)):
            self.error_on_last_epochs += (self.vector_ans_on_epoch[i] - self.y_true[self.size_window + i]) ** 2

        self.error_on_last_epochs = self.error_on_last_epochs ** (0.5)
        return self.error_on_last_epochs