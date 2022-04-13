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
    print("Введите 3 точки выпуклого треугольника")
    A = R2Point()
    B = R2Point()
    C = R2Point()
    tk.clean()
    default_triangle = Void()
    default_triangle = default_triangle.add(A).add(B).add(C)
    default_triangle.draw(tk)
    print("Введите фигуру")
    while f.area() == 0:
        f = f.add(R2Point())
        tk.clean()
        default_triangle.draw(tk)
        f.draw(tk)
        print(f"S = {f.area()}, P = {f.perimeter()}")

        # создание фигуры, принадлежащей фигуре f и лежащей внутри треугольника
        # площадь пересечения равна площади фигуры g
        # проверка всех рёбер на пересечение с ребром треугольника
        # и добавление точек пересечения
        # добавление к оболочке g точек, лежащих внутри треугольника
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
        tk.clean()
        default_triangle.draw(tk)
        f.draw(tk)
        print(f"S = {f.area()}, P = {f.perimeter()}")
        print(f"площадь пересечения : {g.area()} ")
        print()
except(EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
