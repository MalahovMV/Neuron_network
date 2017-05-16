from random import randint


def create_claster():
    number_clusters = 6
    massive_claster = []
    for i in range(number_clusters):
        coor_x = randint(5,1000)
        coor_y = randint(5,500)
        massive_claster.append([coor_x, coor_y])

    return massive_claster