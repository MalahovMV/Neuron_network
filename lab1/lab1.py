from Neuron import Sigma
from Threshold import Threshold
import math

def print_weights(list_weights):
    for el in list_weights:
        print('%.3F' % el, end=', ')

    print()

def threashold_all(y_true, rate_learning, sample_learn):
    print("Threshold. Sample is full")
    neural_treashold = Threshold(y_true, rate_learning, 4)
    error_on_step = 1
    last_weight = []
    neural_treashold.choose_sample(sample_learn)
    while (error_on_step) and (neural_treashold.epochs < 100) and (last_weight != neural_treashold.weight):
        print("Epochs=", neural_treashold.epochs)
        print('W=', end='')
        print_weights(neural_treashold.weight)
        last_weight = neural_treashold.weight[:]
        error_on_step = neural_treashold.counting_errors(True)
        print('Error=', neural_treashold.error[-1])
        neural_treashold.for_epochs()
        print()

def threashold_find_sample(y_true, rate_learning, all_vectors):
    print("Threshold. Find sample")
    flag = True
    sample_size = 1
    while flag:
        for i in range(len(all_vectors)):
            sample_learn = all_vectors[i]
            neural_treashold = Threshold(y_true, rate_learning, 4)
            error_on_step = 1
            last_weight = []
            neural_treashold.choose_sample(sample_learn)
            while (error_on_step) and (neural_treashold.epochs < 100) and (last_weight != neural_treashold.weight):
                last_weight = neural_treashold.weight[:]
                error_on_step = neural_treashold.counting_errors()
                neural_treashold.for_epochs()

            if not neural_treashold.error[-1]:
                answer_vectors = all_vectors[i][:]
                print_weights(neural_treashold.weight)
                print(answer_vectors)
                print()
                return answer_vectors

        len_all_vectors = len(all_vectors)
        for i in range(len_all_vectors):
            can_be_add_with = all_vectors[i][-1] + 1
            while can_be_add_with < 16:
                all_vectors.append((all_vectors[i] + [can_be_add_with]))
                can_be_add_with += 1

        number_extra_vectors = int(
            math.factorial(16) / (math.factorial(16 - sample_size) * math.factorial(sample_size)))
        all_vectors = all_vectors[number_extra_vectors:]
        sample_size += 1


def sigma_all(y_true, rate_learning, sample_learn):
    print("Sigma. Sample is all")
    neural_sigma = Sigma(y_true, rate_learning, 4)
    error_on_step = 1
    last_weight = []
    neural_sigma.choose_sample(sample_learn)
    while (error_on_step) and (neural_sigma.epochs < 100) and (last_weight != neural_sigma.weight):
        print("Epochs=", neural_sigma.epochs)
        print('W=', end='')
        print_weights(neural_sigma.weight)
        last_weight = neural_sigma.weight[:]
        error_on_step = neural_sigma.counting_errors(True)
        print('Error=', neural_sigma.error[-1])
        neural_sigma.for_epochs()
        print()


def sigma_find_sample(y_true, rate_learning, all_vectors):
    print("Sigma. Find sample")
    flag = True
    sample_size = 1
    while flag:
        for i in range(len(all_vectors)):
            sample_learn = all_vectors[i]
            neural_sigma = Sigma(y_true, rate_learning, 4)
            error_on_step = 1
            last_weight = []
            neural_sigma.choose_sample(sample_learn)
            while (error_on_step) and (neural_sigma.epochs < 100) and (last_weight != neural_sigma.weight):
                last_weight = neural_sigma.weight[:]
                error_on_step = neural_sigma.counting_errors()
                neural_sigma.for_epochs()

            if not neural_sigma.error[-1]:
                answer_vectors = all_vectors[i][:]
                print_weights(neural_sigma.weight)
                print(answer_vectors)
                print()
                return answer_vectors

        len_all_vectors = len(all_vectors)
        for i in range(len_all_vectors):
            can_be_add_with = all_vectors[i][-1] + 1
            while can_be_add_with < 16:
                all_vectors.append((all_vectors[i] + [can_be_add_with]))
                can_be_add_with += 1

        number_extra_vectors = int(
            math.factorial(16) / (math.factorial(16 - sample_size) * math.factorial(sample_size)))
        all_vectors = all_vectors[number_extra_vectors:]
        sample_size += 1


def main():
    rate_learning = 0.3
    y_true = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    #y_true = [1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
    sample_learn = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    all_vectors = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15]]
    threashold_all(y_true, rate_learning, sample_learn)
    threashold_sample = threashold_find_sample(y_true, rate_learning, all_vectors[:])
    #print('Learning at new sample')
    #threashold_all(y_true, rate_learning, threashold_sample)
    sigma_all(y_true, rate_learning, sample_learn)
    sigma_sample = sigma_find_sample(y_true, rate_learning, all_vectors[:])
    #print('Learning at new sample')
    #sigma_all(y_true, rate_learning, sigma_sample)

if __name__ == '__main__':
    main()
