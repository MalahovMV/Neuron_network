from neuron import Hopfild

def main(chek_letter):
    letter1 = [1, 1, -1, 1, -1, 1, 1, 1, -1, 1, -1, 1, 1, 1, -1]
    letter2 = [1, 1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1]
    letter3 = [1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, 1, 1]
    neuron = Hopfild(letter1, letter2, letter3)
    i = 0
    while True:
        i += 1
        neuron.calculate_weight()
        flag = neuron.is_education_finally()
        if flag :
            break

        if i > 100: break

    print()
    print(neuron.indification_letter(chek_letter))

if __name__ == '__main__':
    chek_letter = [-1, 1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, 1]
    main(chek_letter)
