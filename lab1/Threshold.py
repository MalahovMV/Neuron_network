import math

class Threshold:
    def __init__(self, y_true, rate_learning, number_input):
        self.weight = [0, 0, 0, 0, 0]
        self.y_true = y_true
        self.input = self.generate_input(number_input)
        self.epochs = 0
        self.rate_learning = rate_learning
        self.error = []
        self.sample_learn = []
        self.y_true_sample = []

    def counting_errors(self, flag = False):
        error = 0
        ans_epoch =[]
        for i in range(len(self.input)):
            y_calculate = 0
            for j in range(len(self.weight)):
                y_calculate += self.weight[j] * self.input[i][j]

            if y_calculate < 0:
                y_calculate = 0

            else:
                y_calculate = 1

            ans_epoch.append(y_calculate)
            if y_calculate != self.y_true[i]:
                error += 1

        if flag: print('y=',ans_epoch)

        self.error.append(error)
        return error

    def for_epochs(self):
        for i in range(len(self.sample_learn)):
            y_calculate = 0
            for j in range(len(self.weight)):
                y_calculate += self.weight[j] * self.sample_learn[i][j]

            if y_calculate < 0:
                y_calculate = 0

            else:
                y_calculate = 1

            if y_calculate != self.y_true_sample[i]:
                for j in range(len(self.sample_learn[i])):
                    self.weight[j] += round(float((self.y_true_sample[i] - y_calculate) * self.rate_learning * self.sample_learn[i][j]), 3)

        self.epochs += 1

    def choose_sample(self, number_set):
        for el in number_set:
            self.sample_learn.append(self.input[el])
            self.y_true_sample.append(self.y_true[el])

    def generate_input(self, number_input):
        input_massive = []
        for i in range(2 ** number_input):
            string_input_massive = []
            digit = i
            for h in range(number_input, 0, -1):
                string_input_massive.append(digit % 2)
                digit = digit // 2

            string_input_massive.append(1)
            string_input_massive.reverse()
            input_massive.append(string_input_massive)

        return input_massive