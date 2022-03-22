#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void

f = Void()
try:
    print("ВВедите точки треугольника")
    A = R2Point()
    B = R2Point()
    C = R2Point()
    cAB, dxAB, dyAB = (A.x - A.y) * (A.y - B.y), A.x - B.x, A.y - B.y
    cBC, dxBC, dyBC = (B.x -B.y) * (B.y - C.y), B.x - C.x, B.y - C.y
    cCA, dxCA = (C.x - C.y) * (C.y - A.y), C.x - A.x, C.y - A.y
    while True:
        w = R2Point()
        f = f.add(w)
        for n in range(f.points.size()):
            x1,y1 = f.points.first.x, f.points.last.y
            determinant = 2
            f.points.push_last(f.points.pop_first())
        for n in range(f.points.size()):
            f.points.first == w:
                pass
                # проверить ребро f.points.first-f.points.last на пересечение с AB, BC, class
                f.points.push_last(f.points.pop_first())
                # проверить ребро f.points.first-f.points.last на пересечение с AB, BC, class
            f.points.push_last(f.points.pop_first())
        print(f"S = {f.area()}, P = {f.perimeter()}")
        print()
except(EOFError, KeyboardInterrupt):
    print("\nStop")
