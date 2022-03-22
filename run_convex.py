#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void
from lesson3task3 import is_inside_triangle

f = Void()
try:
    print("Введите 3 точки выпуклого треугольника")
    A = R2Point()
    B = R2Point()
    C = R2Point()
    cAB = (A.x - A.y) * (A.y - B.y)
    cCA = (C.x - C.y)* (C.y - A.y)
    cBC = (B.x - B.y) * (B.y - C.y)
    dyAB, dyCA, dyBC = A.y - B.y, C.y - A.y, B.y - C.y
    dxAB, dxCA, dxBC = A.x - B.x, C.x - A.x, B.x - C.x
    print("Введите фигуру")
    while f.area() == 0:
        print("площадь пересечения равна 0")
        f = f.add(R2Point())
        print(f"S = {f.area()}, P = {f.perimeter()}")
    # создание фигуры, принадлежащей фигуре f и лежащей внутри триугольника
    # площадь пересечения равна площади фигуры g
    g = Void()
    # проверка всех рёбер на пересечение с ребром треугольника
    # и добавление точек пересечения
    def check(A, B):
        x1, x2 = f.points.first().x, f.points.last().x
        y1, y2 = f.points.first().y, f.points.last().y
        D = Void(R2Point(x1, y1), A, B)
        j = R2Point(x2, y2).is_light(D.points.last(), D.points.first())
        print(j)
        D.points.push_last(self.points.pop_first())
        k = R2Point(x2,y2).is_light(D.points.last(), D.points.first())
        print(k)
        D.points.push_last(self.points.pop_first())
        l = R2Point(x2,y2).is_light(D.points.last(), D.points.first())
        print(l)
        if j and not k and not l:
            if 

        print(f"точка пресечения ({x}, {y}) добавлена")
    for n in range(f.points.size()):
        check(dxAB, dyAB, cAB)
        f.points.push_last(f.points.pop_first())
    for n in range(f.points.size()):
        check(dxBC, dyBC, cBC)
        f.points.push_last(f.points.pop_first())
    for n in range(f.points.size()):
        check(dxCA, dyCA, cCA)
        f.points.push_last(f.points.pop_first())

    # добавление к оболочке g точек лежащих внутри триугольника
    for n in range(f.points.size()):
        if is_inside_triangle(f.points.first().x, f.points.first().y,
                              A.x, A.y, B.x, B.y, C.x, C.y):
            g.add(f.first())
            print(f"точка внутри треугольника {f.points.first().x}, \
             {f.points.first().y} добавлена")
        f.points.push_last(f.points.pop_first())
    while True:
        print(f"площадь пересечения : {g.area()} ")
        w = R2Point()
        if f.add(w).area() != f.area():
            f = f.add(w)
            if is_inside_triangle(w.x, w.y, A.x, A.y, B.x, B.y, C.x, C.y):
                g.add(w)
            else:
                if f.add(A).area() == f.area():
                    g.add(A)
                if f.add(B).area() == f.area():
                    g.add(B)
                if f.add(C).area() == f.area():
                    g.add(C)
                # проверка последних добавленных рёбер на пресечение с рёбрами
                # треугольника и добавление новых точек пересеничя
                check(dxAB, dyAB, cAB)
                check(dxBC, dyBC, cBC)
                check(dxCA, dyCA, cCA)
        print(f"S = {f.area()}, P = {f.perimeter()}")
        print()
except(EOFError, KeyboardInterrupt):
    print("\nStop")
