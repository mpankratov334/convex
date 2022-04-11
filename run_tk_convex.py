#!/usr/bin/env -S python3 -B
from tk_drawer import TkDrawer
from r2point import R2Point
from convex import Void, Point, Segment, Polygon
from check import check


def void_draw(self, tk):
    pass


def point_draw(self, tk):
    tk.draw_point(self.p)


def segment_draw(self, tk):
    tk.draw_line(self.p, self.q)


def polygon_draw(self, tk):
    for n in range(self.points.size()):
        tk.draw_line(self.points.last(), self.points.first())
        self.points.push_last(self.points.pop_first())


setattr(Void, 'draw', void_draw)
setattr(Point, 'draw', point_draw)
setattr(Segment, 'draw', segment_draw)
setattr(Polygon, 'draw', polygon_draw)


tk = TkDrawer()
f = Void()
tk.clean()

try:
    while True:

        print(f"S = {f.area()}, P = {f.perimeter()}\n")
        print("Введите 3 точки выпуклого треугольника")
        A = R2Point()
        B = R2Point()
        C = R2Point()
        tk.clean()
        default_triangle = Void()
        default_triangle = default_triangle.add(A)
        default_triangle = default_triangle.add(B)
        default_triangle = default_triangle.add(C)
        default_triangle.draw(tk)
        print("Введите фигуру")
        while f.area() == 0:
            print("площадь пересечения равна 0")
            f = f.add(R2Point())
            tk.clean()
            default_triangle.draw(tk)
            f.draw(tk)
            print(f"S = {f.area()}, P = {f.perimeter()}")

        # создание фигуры, принадлежащей фигуре f и лежащей внутри треугольника
        # площадь пересечения равна площади фигуры g
        g = Void()
        # проверка всех рёбер на пересечение с ребром треугольника
        # и добавление точек пересечения
        for n in range(f.points.size()):
            point1 = f.points.first()
            point2 = f.points.last()
            if check(A.x, A.y, B.x, B.y, point1.x, point1.y,
                                    point2.x, point2.y) is not None:
                g = g.add(check(A.x, A.y, B.x, B.y, point1.x, point1.y,
                                    point2.x, point2.y))
            f.points.push_last(f.points.pop_first())
        for n in range(f.points.size()):
            point1 = f.points.first()
            point2 = f.points.last()
            if check(B.x, B.y, C.x, C.y, point1.x, point1.y,
                                    point2.x, point2.y) is not None:
                g = g.add(check(B.x, B.y, C.x, C.y, point1.x, point1.y,
                                    point2.x, point2.y))
            f.points.push_last(f.points.pop_first())
        for n in range(f.points.size()):
            point1 = f.points.first()
            point2 = f.points.last()
            if check(C.x, C.y, A.x, A.y, point1.x, point1.y,
                                    point2.x, point2.y) is not None:
                g = g.add(check(C.x, C.y, A.x, A.y, point1.x, point1.y,
                                    point2.x, point2.y))
            f.points.push_last(f.points.pop_first())

        # добавление к оболочке g точек, лежащих внутри треугольника
        for n in range(f.points.size()):
            if default_triangle.is_inside_convex(f.points.first()):
                g = g.add(f.points.first())
            f.points.push_last(f.points.pop_first())
        # добавление к оболочке g вершины треугольника, если она принадлежит
        # оболочке f
        if f.is_inside_convex(A):
            #print("точка A добавлена")
            g = g.add(A)
        if f.is_inside_convex(B):
            #print("точка B добавлена")
            g = g.add(B)
        if f.is_inside_convex(C):
            #print("точка C добавлена")
            g = g.add(C)


        while True:
            print(f"площадь пересечения : {g.area()} ")
            w = R2Point()
            if not f.is_inside_convex(w):
                f = f.add(w)
                tk.clean()
                default_triangle.draw(tk)
                f.draw(tk)
                # проверка двух последних добавленных рёбер на пресечение с
                # рёбрами треугольника ABC и добавление новых точек пересеничя
                # AB
                #print(f"f.points.first() = {f.points.first().x, f.points.first().y}")
                #print(f"f.points.last() = {f.points.last().x, f.points.last().y}")
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
                # print(f"f.points.first() = {f.points.first().x, f.points.first().y}")
                # print(f"f.points.last() = {f.points.last().x, f.points.last().y}")

                if check(A.x, A.y, B.x, B.y, f.points.first().x,
                                f.points.first().y, f.points.last().x,
                                f.points.last().y) is not None:
                    # print("\nДобавление")
                    # print(f"f.points.first() = {f.points.first().x, f.points.first().y}")
                    # print(f"f.points.last() = {f.points.last().x, f.points.last().y}")
                    g = g.add(check(A.x, A.y, B.x, B.y, f.points.first().x,
                                        f.points.first().y, f.points.last().x,
                                                        f.points.last().y))
                # BC
                if check(B.x, B.y, C.x, C.y, f.points.first().x,
                                f.points.first().y, f.points.last().x,
                                f.points.last().y) is not None:
                    # print("\nДобавление")
                    # print(f"f.points.first() = {f.points.first().x, f.points.first().y}")
                    # print(f"f.points.last() = {f.points.last().x, f.points.last().y}")
                    g = g.add(check(B.x, B.y, C.x, C.y, f.points.first().x,
                                        f.points.first().y, f.points.last().x,
                                                        f.points.last().y))

                f.points.push_first(f.points.pop_last())
                # print(f"f.points.first() = {f.points.first().x, f.points.first().y}")
                # print(f"f.points.last() = {f.points.last().x, f.points.last().y}")

                if check(B.x, B.y, C.x, C.y, f.points.first().x,
                                f.points.first().y, f.points.last().x,
                                f.points.last().y) is not None:
                    # print("\nДобавление")
                    # print(f"f.points.first() = {f.points.first().x, f.points.first().y}")
                    # print(f"f.points.last() = {f.points.last().x, f.points.last().y}")
                    g = g.add(check(B.x, B.y, C.x, C.y, f.points.first().x,
                                        f.points.first().y, f.points.last().x,
                                                        f.points.last().y))
                # AC (ООП.в.дей(ств).ии)
                if check(C.x, C.y, A.x, A.y, f.points.first().x,
                                f.points.first().y, f.points.last().x,
                                f.points.last().y) is not None:
                    # print("\nДобавление")
                    # print(f"f.points.first() = {f.points.first().x, f.points.first().y}")
                    # print(f"f.points.last() = {f.points.last().x, f.points.last().y}")
                    g = g.add(check(C.x, C.y, A.x, A.y, f.points.first().x,
                                        f.points.first().y, f.points.last().x,
                                                        f.points.last().y))

                f.points.push_last(f.points.pop_first())

                if check(C.x, C.y, A.x, A.y, f.points.first().x,
                                f.points.first().y, f.points.last().x,
                                f.points.last().y) is not None:
                    # print("\nДобавление")
                    # print(f"f.points.first() = {f.points.first().x, f.points.first().y}")
                    # print(f"f.points.last() = {f.points.last().x, f.points.last().y}")
                    g = g.add(check(C.x, C.y, A.x, A.y, f.points.first().x,
                                        f.points.first().y, f.points.last().x,
                                                        f.points.last().y))


            # добавление новой точки если она лежит строго внутри треугольника
                if default_triangle.is_inside_convex(w):
                    # print( f"точка W добавлена")
                    g = g.add(w)
                else:
                    if f.is_inside_convex(A):
                        g = g.add(A)
                    if f.is_inside_convex(B):
                        g = g.add(B)
                    if f.is_inside_convex(C):
                        g = g.add(C)
            print(f"S = {f.area()}, P = {f.perimeter()}")
            print()
except(EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
