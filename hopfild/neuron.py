import numpy as np

class Hopfild:
    @staticmethod
    def activation_function(letter_vector, chek_letter):
        for i in range(len(letter_vector[0])):
            if letter_vector[0][i] < 0:
                letter_vector[0][i] = -1

            elif letter_vector[0][i] > 0:
                letter_vector[0][i] = 1

            else:
                letter_vector[0][i] = chek_letter[0][i]

        return letter_vector

    @staticmethod
    def comparsion_vector(vector1, vector2):
        for i in range(len(vector1[0])):
            if vector1[0][i] != vector2[0][i]:
                return False

        return True

    def __init__(self, letter1, letter2, letter3):
        self.letter1 = np.array([letter1[:]])
        self.letter2 = np.array([letter2[:]])
        self.letter3 = np.array([letter3[:]])
        self.weight = np.zeros((len(letter1), len(letter1)))

    def calculate_weight(self):
        self.weight += self.letter1.T.dot(self.letter1) + self.letter2.T.dot(self.letter2) + (
            self.letter3.T.dot(self.letter3))

        for i in range(len(self.weight)):
            self.weight[i][i] = 0

        print(self.weight)

    def is_education_finally(self):
        letter_vector1 = self.letter1.dot(self.weight)
        letter_vector2 = self.letter2.dot(self.weight)
        letter_vector3 = self.letter3.dot(self.weight)
        letter_vector1 = Hopfild.activation_function(letter_vector1, self.letter1)
        letter_vector2 = Hopfild.activation_function(letter_vector2, self.letter2)
        letter_vector3 = Hopfild.activation_function(letter_vector3, self.letter3)
        if (Hopfild.comparsion_vector(letter_vector1, self.letter1)) and (Hopfild.comparsion_vector(letter_vector2, self.letter2)) and (
                Hopfild.comparsion_vector(letter_vector3, self.letter3)):

            return True

        else:
            return False

    def indification_letter(self, chek_letter):
        chek_letter = np.array([chek_letter[:]])
        letter_vector = chek_letter.dot(self.weight)
        letter_vector = Hopfild.activation_function(letter_vector, chek_letter)
        return letter_vector


