#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void
from check import check

f = Void()
try:
    print("Введите 3 точки выпуклого треугольника")
    A = R2Point()
    B = R2Point()
    C = R2Point()
    print("Введите фигуру")
    while f.area() == 0:
        print("площадь пересечения равна 0")
        f = f.add(R2Point())
        print(f"S = {f.area()}, P = {f.perimeter()}")

    # создание фигуры g, принадлежащей фигуре f и лежащей внутри треугольника.
    # площадь пересечения равна площади фигуры g.
    # проверка всех рёбер на пересечение с ребром треугольника
    # и добавление точек пересечения.
    # добавление к оболочке g точек, лежащих внутри треугольника.
    # добавление к оболочке g вершины треугольника, если она принадлежит
    # оболочке f
    g = f.pre_induction(A, B, C)
    print(f"площадь пересечения : {g.area()} ")

    while True:
        w = R2Point()
        # проверка двух последних добавленных рёбер на пресечение с
        # рёбрами треугольника ABC и добавление новых точек пересеничя
        # добавление новой точки если она лежит строго внутри треугольника
        f = f.induction(g, w, A, B, C)
        print(f"S = {f.area()}, P = {f.perimeter()}")
        print(f"площадь пересечения : {g.area()} ")
        print()
except(EOFError, KeyboardInterrupt):
    print("\nStop")
