# Aku52
# class_lz
# Написать класс октагон, атрибуты: сторона и постоянные угол,к.
# Находим параметры: радиус/площать вписанной/описанной окружности, 
                                      # площадь и периметр октага
# Фигуры разных цветов на координатной плоскости

# circum - описанная окружность
# inscr - вписанная окружность
# oct - 8-угольник
from math import pi
from math import sqrt
from math import radians
from math import cos, sin

import matplotlib.pyplot as plt

# Константы
corner = 45
k = 1 + sqrt(2)

# Ввод пользователя
print('Введите длину стороны октагона(больше 33 не обрабатываю(не рисую))')
side = int(input())



class Octagon:

    # Константы
    corner = 45
    k = 1 + sqrt(2)

    # Конструктор
    def __init__(self,side):
        self.side = side # side - сторона
        self.fig, self.ax = plt.subplots()
        


    # Радиус описанной окружности 
    def circum_r (self):
        self_r_c = (self.side/2)*k
        print(f'Радиус описанной окружности{self_r_c}')
        return self_r_c
    
    # Рисуем описанную окружность
    def circum_r_ax(self, center, color):
        radius = self.circum_r()
        circum_circle = plt.Circle(center, radius, color=color, fill=False) # fill - заливка (отмена заливки)
        self.ax.add_artist(circum_circle)



    # Площадь описанной окружности
    def circum_s (self):
        self_s_c = pi*((self.side/2)*k)**2
        print(f'Площадь описанной окружности{self_s_c}')
        


    # Радиус вписанной окружности
    def inscr_r (self ):
        self_r_i = (self.side/2)*sqrt(2)
        print(f'Радиус вписанной окружности {self_r_i}')
        return self_r_i

    # Рисуем вписанную окружность
    def inscr_r_ax(self, center, color):
        radius = self.inscr_r()
        inscr_circle = plt.Circle(center, radius, color=color, fill=False) # fill - заливка (отмена заливки)
        self.ax.add_artist(inscr_circle)



     # Площадь вписанной окружности
    def inscr_s (self):
        self_s_i = pi*((self.side/2)*sqrt(2))**2
        print(f'Площадь вписанной окружности{self_s_i}')
        


    # Площадь октагона
    def oct_s (self):
        self_s_o = 2*self.side**2*k
        print(f'Площадь октагона{self_s_o}')   

    # Периметр октагона 
    def oct_p (self):
        self_p_o = 8*self.side
        print(f'Периметр октагона {self_p_o}')
        return self_p_o



    # Рисуем восьмиугольник
    def draw_octagon(self, color='blue'):
        vertices = []
        for i in range(8):
            angle = radians(i * corner) # преобразует угол в радианы (так как функции cos и sin работают с радианами)
            x = self.side * cos(angle)
            y = self.side * sin(angle)
            vertices.append((x, y))

        # Соединяем вершины
        for i in range(8):
            x_values = [vertices[i][0], vertices[(i + 1) % 8][0]]
            y_values = [vertices[i][1], vertices[(i + 1) % 8][1]]
            self.ax.plot(x_values, y_values, color=color)



    def show(self):
        self.ax.set_xlim(-40, 40)
        self.ax.set_ylim(-40, 40)
        self.ax.set_aspect('equal', adjustable='box')
        plt.grid()
        plt.show()
        plt.title('Восьмиугольник с окружностями')


        
    def __del__(self):
        print("del done")



if __name__ == "__main__":

    drawer = Octagon(side)
    drawer.draw_octagon(color='blue')  # Рисуем восьмиугольник
    drawer.inscr_r_ax(center=(0, 0), color='red')  # Вписанная окружность
    drawer.circum_r_ax(center=(0, 0), color='green')  # Описанная окружность
    drawer.show() 