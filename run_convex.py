#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void
from check import check

f = Void()
try:
    print(f"S = {f.area()}, P = {f.perimeter()}\n")
    print("Введите 3 точки выпуклого треугольника")
    A = R2Point()
    B = R2Point()
    C = R2Point()
    print("Введите фигуру")
    while f.area() == 0:
        print("площадь пересечения равна 0")
        f = f.add(R2Point())
        print(f"S = {f.area()}, P = {f.perimeter()}")

    # создание фигуры, принадлежащей фигуре f и лежащей внутри треугольника
    # площадь пересечения равна площади фигуры g
    g = Void()
    # проверка всех рёбер на пересечение с ребром треугольника
    # и добавление точек пересечения
    g = f.RBA3(g, A, B, C)
    # добавление к оболочке g точек, лежащих внутри треугольника
    g = f.AIT(g, A, B, C)
    # добавление к оболочке g вершины треугольника, если она принадлежит
    # оболочке f
    g = f.AIC(g, A, B, C)

    while True:
        print(f"площадь пересечения : {g.area()} ")
        w = R2Point()
        if not f.is_inside_convex(w):
            f = f.add(w)
            # проверка двух последних добавленных рёбер на пресечение с
            # рёбрами треугольника ABC и добавление новых точек пересеничя
            # AB
            #print(f"f.points.first() = {f.points.first().x, f.points.first().y}")
            #print(f"f.points.last() = {f.points.last().x, f.points.last().y}")
            #print("проверка AB")
            if check(A.x, A.y, B.x, B.y, f.points.first().x,
                            f.points.first().y, f.points.last().x,
                            f.points.last().y) is not None:
                #print("\nДобавление")
                #print(f"f.points.first() = {f.points.first().x, f.points.first().y}")
                #print(f"f.points.last() = {f.points.last().x, f.points.last().y}")
                g = g.add(check(A.x, A.y, B.x, B.y, f.points.first().x,
                                    f.points.first().y, f.points.last().x,
                                                    f.points.last().y))


            f.points.push_last(f.points.pop_first())
            #print("повернули")
            #print(f"f.points.first() = {f.points.first().x, f.points.first().y}")
            #print(f"f.points.last() = {f.points.last().x, f.points.last().y}")

            if check(A.x, A.y, B.x, B.y, f.points.first().x,
                            f.points.first().y, f.points.last().x,
                            f.points.last().y) is not None:
                #print("\nДобавление")
                g = g.add(check(A.x, A.y, B.x, B.y, f.points.first().x,
                                    f.points.first().y, f.points.last().x,
                                                    f.points.last().y))
            # BC
            #print("проверка BC")
            if check(B.x, B.y, C.x, C.y, f.points.first().x,
                            f.points.first().y, f.points.last().x,
                            f.points.last().y) is not None:
                #print("\nДобавление")
                g = g.add(check(B.x, B.y, C.x, C.y, f.points.first().x,
                                    f.points.first().y, f.points.last().x,
                                                    f.points.last().y))

            f.points.push_first(f.points.pop_last())
            #print("повернули")
            #print(f"f.points.first() = {f.points.first().x, f.points.first().y}")
            #print(f"f.points.last() = {f.points.last().x, f.points.last().y}")

            if check(B.x, B.y, C.x, C.y, f.points.first().x,
                            f.points.first().y, f.points.last().x,
                            f.points.last().y) is not None:
                #print("\nДобавление")
                g = g.add(check(B.x, B.y, C.x, C.y, f.points.first().x,
                                    f.points.first().y, f.points.last().x,
                                                    f.points.last().y))
            # AC (ООП.в.дей(ств).ии)
            #print("проверка AC")
            if check(C.x, C.y, A.x, A.y, f.points.first().x,
                            f.points.first().y, f.points.last().x,
                            f.points.last().y) is not None:
                #print("\nДобавление")
                #print(f"f.points.first() = {f.points.first().x, f.points.first().y}")
                #print(f"f.points.last() = {f.points.last().x, f.points.last().y}")
                g = g.add(check(C.x, C.y, A.x, A.y, f.points.first().x,
                                    f.points.first().y, f.points.last().x,
                                                    f.points.last().y))

            f.points.push_last(f.points.pop_first())
            #print("повернули")
            #print(f"f.points.first() = {f.points.first().x, f.points.first().y}")
            #print(f"f.points.last() = {f.points.last().x, f.points.last().y}")

            if check(C.x, C.y, A.x, A.y, f.points.first().x,
                            f.points.first().y, f.points.last().x,
                            f.points.last().y) is not None:
                #print("\nДобавление")
                #print(f"f.points.first() = {f.points.first().x, f.points.first().y}")
                #print(f"f.points.last() = {f.points.last().x, f.points.last().y}")
                g = g.add(check(C.x, C.y, A.x, A.y, f.points.first().x,
                                    f.points.first().y, f.points.last().x,
                                                    f.points.last().y))


        # добавление новой точки если она лежит строго внутри треугольника
            if default_triangle.is_inside_convex(w):
                #print( f"точка W добавлена")
                g = g.add(w)

            else:
                if f.is_inside_convex(A):
                    #print("точка А добавлена")
                    g = g.add(A)
                if f.is_inside_convex(B):
                    #print("точка B добавлена")
                    g = g.add(B)
                if f.is_inside_convex(C):
                    #print("точка C добавлена")
                    g = g.add(C)
        print(f"S = {f.area()}, P = {f.perimeter()}")
        print()
except(EOFError, KeyboardInterrupt):
    print("\nStop")
