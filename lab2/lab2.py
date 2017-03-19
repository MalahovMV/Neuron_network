import math

def function(a, b, N, size_window):
    step = (b - a) / N
    input_vectors = [a]
    input_matrix = []
    y_true = []
    while input_vectors[-1] < b:
        y_true.append(round(float((math.cos(input_vectors[-1])) ** 2 - 0.5), 3))
        input_vectors.append(round(float(input_vectors[-1] + step), 3))

    #print(y_true)
    for i in range(len(input_vectors) - size_window):
        input_matrix.append(list((input_vectors[i], input_vectors[i + 1], input_vectors[i + 2], input_vectors[i + 3])))

    print(input_matrix)

def main():
    a = -1
    b = 0.5
    N = 20
    size_window = 4
    function(a,b,N, size_window - 1)

if __name__ == '__main__':
    main()
