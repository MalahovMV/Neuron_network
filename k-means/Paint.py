from tkinter import *
from Neuron import create_claster, Algo_k_means

def first_start_global_constant(event):
    try:
        root.destroy()

    except:
        pass

    global root
    global field
    global choose_colors
    global flag_before_work
    global massiv_claster
    global massive_point
    number_clusters = int(input('Введите количество кластеров, не больше 6 = '))
    root = Tk()
    root.title("Алгоритм k-means")
    field = Canvas(width=1000, height=500, bg='white')
    choose_colors = ('red', 'green', 'blue', 'gold', 'pink', 'purple')
    flag_before_work = True
    massiv_claster = create_claster(number_clusters)
    massive_point = []
    main()

def main():
    button_Manhetten = Button(text='Manhetten')
    button_Chebyshev = Button(text='Chebyshev')
    button_Recoil = Button(text='Recoil')
    button_Restart = Button(text='Restart')
    field.pack()
    button_Chebyshev.pack(side=LEFT)
    button_Manhetten.pack(side=LEFT)
    button_Restart.pack(side=RIGHT)
    button_Recoil.pack(side=RIGHT)
    claster_paint()
    button_Manhetten.bind('<Button-1>', manhetten)
    button_Chebyshev.bind('<Button-1>', chebyshev)
    button_Recoil.bind('<Button-1>', recoil)
    button_Restart.bind('<Button-1>', first_start_global_constant)
    field.bind('<Button-1>', coor_print)
    root.mainloop()

def claster_paint():
    for i in range(len(massiv_claster)):
        field.create_oval(massiv_claster[i][0] - 5, massiv_claster[i][1] - 5, massiv_claster[i][0] + 5,
                          massiv_claster[i][1] + 5, outline=choose_colors[i], fill=choose_colors[i])

def coor_print(event):
    if flag_before_work:
        field.create_oval(event.x, event.y, event.x + 4, event.y + 4, outline="black", fill='black', width=1)
        massive_point.append([event.x + 2, event.y + 2])

def manhetten(event):
    global flag_before_work
    flag_before_work = False
    k_means = Algo_k_means(massiv_claster, massive_point, 0)
    massiv_from_last_step = []
    while True:
        k_means.point_division()
        if (k_means.massive_acessories == massiv_from_last_step) or (k_means.step > 100) :
            break

        else:
            massiv_from_last_step = k_means.massive_acessories

        k_means.calculate_new_center_clasters()

        field.delete('all')
        for i in range(len(massiv_from_last_step)):
            for elem in massiv_from_last_step[i]:
                field.create_oval(massive_point[elem][0] - 2, massive_point[elem][1] - 2, massive_point[elem][0] + 2,
                            massive_point[elem][1] + 2, outline=choose_colors[i], fill=choose_colors[i], width=1)

        for i in range(len(k_means.center_claster)):
                field.create_oval(k_means.center_claster[i][0] - 5, k_means.center_claster[i][1] - 5, k_means.center_claster[i][0] + 5,
                                k_means.center_claster[i][1] + 5, outline=choose_colors[i], fill=choose_colors[i], width=1)

def chebyshev(event):
    global flag_before_work
    flag_before_work = False
    k_means = Algo_k_means(massiv_claster, massive_point, 1)
    massiv_from_last_step = []
    while True:
        k_means.point_division()
        if (k_means.massive_acessories == massiv_from_last_step) or (k_means.step > 100) :
            break

        else:
            massiv_from_last_step = k_means.massive_acessories

        k_means.calculate_new_center_clasters()

        field.delete('all')
        for i in range(len(massiv_from_last_step)):
            for elem in massiv_from_last_step[i]:
                field.create_oval(massive_point[elem][0] - 2, massive_point[elem][1] - 2, massive_point[elem][0] + 2,
                            massive_point[elem][1] + 2, outline=choose_colors[i], fill=choose_colors[i], width=1)

        for i in range(len(k_means.center_claster)):
                field.create_oval(k_means.center_claster[i][0] - 5, k_means.center_claster[i][1] - 5, k_means.center_claster[i][0] + 5,
                                k_means.center_claster[i][1] + 5, outline=choose_colors[i], fill=choose_colors[i], width=1)

def recoil(event):
    field.delete('all')
    for i in range(len(massiv_claster)):
        field.create_oval(massiv_claster[i][0] - 5, massiv_claster[i][1] - 5, massiv_claster[i][0] + 5,
                          massiv_claster[i][1] + 5, outline=choose_colors[i], fill=choose_colors[i])

    for el in massive_point:
        field.create_oval(el[0] - 2, el[1] - 2, el[0] + 2, el[1] + 2, outline="black", fill='black', width=1)

if __name__ == '__main__':
    first_start_global_constant(1)