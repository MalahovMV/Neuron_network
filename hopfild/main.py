from neuron import Hopfild

def main(lis_letter):
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
    for el in list_letter:
        from_massiv_to_letter(el, neuron.indification_letter(el))

def read_data(file='Letter'):
    f = open(file, 'r')
    list_letter = []
    chek_letter = []
    i = 0
    while True:
        if i == 5:
            i = 0
            s = f.readline()
            list_letter.append(chek_letter)
            chek_letter = []
            print(list_letter)
            continue

        s = f.readline()
        if not s:
            break

        chek_letter = from_letter_to_massiv(chek_letter, s)
        i += 1

    return list_letter


def from_letter_to_massiv(beginning_letter, s):
    for el in s[:-1]:
        if el == ' ':
            beginning_letter.append(-1)

        elif el == '*':
            beginning_letter.append(1)

        else:
            raise Exception("Error symbol", el)

    return beginning_letter

def from_massiv_to_letter(letter_vector1, letter_vector2):
        i = 0
        j = 0
        for el in letter_vector1:
            i += 1
            if i % 3:
                if el == 1:
                    print('*', end='')

                else:
                    print(' ', end='')

            else:
                if el == 1:
                    print('*', end='')

                else:
                    print(' ', end='')

                if i == 9:
                    print('  --->  ', end='')

                else:
                    print(8*' ', end='')

                k = 0
                while k < 3:
                    if letter_vector2[0][j] == 1:
                        print('*', end='')

                    else:
                        print(' ', end='')

                    j += 1
                    k += 1

                print()

if __name__ == '__main__':
    #chek_letter = [-1, 1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, 1]
    list_letter = read_data()
    main(list_letter)
