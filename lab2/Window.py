class Window:

    def __init__(self, rate_learning, input_matrix):
        self.y_true = []
        self.rate_learning = rate_learning
        self.epochs = 0
        self.input_matrix = input_matrix
        self.weight = [0, 0, 0, 0, 0]
        self.error_on_last_epochs = 0

    def during_epochs(self):
        y_calculate_vector = []
        for i in range(len(self.input_matrix)):
            y_calculate = 0
            for j in range(len(self.input_matrix[i])):
                y_calculate = self.weight[j] * self.input_matrix[i][j]

            y_calculate_vector.append(y_calculate)
            for j in range(len(self.input_matrix[i])):
                self.weight[j] += (y_calculate - self.input_matrix[i + 1][-1]) * self.rate_learning * self.input_matrix[i][j]

    #def next_calculate(self, x_vector):
        #return

