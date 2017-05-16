from random import randint


def create_claster(number_clusters):
    massive_claster = []
    for i in range(number_clusters):
        coor_x = randint(5,1000)
        coor_y = randint(5,500)
        massive_claster.append([coor_x, coor_y])

    return massive_claster

class Algo_k_means:

    @staticmethod
    def manhetten_distant(point1, point2):
        distant = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        return distant

    @staticmethod
    def chebyshev_distant(point1, point2):
        sub_x = abs(point1[0] - point2[0])
        sub_y = abs(point1[1] - point2[1])
        if sub_x > sub_y :
            return sub_x

        else:
            return sub_y

    def __init__(self, massiv_claster, massiv_point, distant_type):
        self.center_claster = massiv_claster[:]
        self.massive_point = massiv_point[:]
        self.massive_acessories = []
        self.step = 0
        self.distant_type = distant_type

    def point_division(self):
        self.massive_acessories = [[],[],[],[],[],[]]
        for j in range(len(self.massive_point)):
            min_distant = 1500
            for i in range(len(self.center_claster)):
                if self.distant_type:
                    distant = self.chebyshev_distant(self.massive_point[j], self.center_claster[i])

                else:
                    distant = self.manhetten_distant(self.massive_point[j], self.center_claster[i])

                if distant < min_distant:
                    min_distant = distant
                    n_min = i

            self.massive_acessories[n_min].append(j)

        self.step += 1

    def calculate_new_center_clasters(self):
        for i in range(len(self.massive_acessories)):
            if self.massive_acessories[i]:
                new_x = 0
                new_y = 0
                kol_vo = 0
                for el in self.massive_acessories[i]:
                    new_x += self.massive_point[el][0]
                    new_y += self.massive_point[el][1]
                    kol_vo += 1

                self.center_claster[i] = [new_x // kol_vo, new_y // kol_vo]