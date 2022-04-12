from deq import Deq
from r2point import R2Point
from check import check


class Figure:
    """ Абстрактная фигура """

    def perimeter(self):
        return 0.0

    def area(self):
        return 0.0


class Void(Figure):
    """ "Hульугольник" """

    def add(self, p):
        return Point(p)


class Point(Figure):
    """ "Одноугольник" """

    def __init__(self, p):
        self.p = p

    def add(self, q):
        return self if self.p == q else Segment(self.p, q)


class Segment(Figure):
    """ "Двуугольник" """

    def __init__(self, p, q):
        self.p, self.q = p, q

    def perimeter(self):
        return 2.0 * self.p.dist(self.q)

    def add(self, r):
        if R2Point.is_triangle(self.p, self.q, r):
            return Polygon(self.p, self.q, r)
        elif self.q.is_inside(self.p, r):
            return Segment(self.p, r)
        elif self.p.is_inside(r, self.q):
            return Segment(r, self.q)
        else:
            return self


class Polygon(Figure):
    """ Многоугольник """

    def __init__(self, a, b, c):
        self.points = Deq()
        self.points.push_first(b)
        if b.is_light(a, c):
            self.points.push_first(a)
            self.points.push_last(c)
        else:
            self.points.push_last(a)
            self.points.push_first(c)
        self._perimeter = a.dist(b) + b.dist(c) + c.dist(a)
        self._area = abs(R2Point.area(a, b, c))


    def perimeter(self):
        return self._perimeter

    def area(self):
        return self._area

    # добавление новой точки
    def add(self, t):

        # поиск освещённого ребра
        for n in range(self.points.size()):
            if t.is_light(self.points.last(), self.points.first()):
                break
            self.points.push_last(self.points.pop_first())

        # хотя бы одно освещённое ребро есть
        if t.is_light(self.points.last(), self.points.first()):


            # учёт удаления ребра, соединяющего конец и начало дека
            self._perimeter -= self.points.first().dist(self.points.last())
            self._area += abs(R2Point.area(t,
                                           self.points.last(),
                                           self.points.first()))

            # удаление освещённых рёбер из начала дека
            p = self.points.pop_first()
            while t.is_light(p, self.points.first()):
                self._perimeter -= p.dist(self.points.first())
                self._area += abs(R2Point.area(t, p, self.points.first()))
                p = self.points.pop_first()
            self.points.push_first(p)

            # удаление освещённых рёбер из конца дека
            p = self.points.pop_last()
            while t.is_light(self.points.last(), p):
                self._perimeter -= p.dist(self.points.last())
                self._area += abs(R2Point.area(t, p, self.points.last()))
                p = self.points.pop_last()
            self.points.push_last(p)

            # добавление двух новых рёбер
            self._perimeter += t.dist(self.points.first()) + \
                t.dist(self.points.last())
            self.points.push_first(t)

        return self

        # проверка точки на принадлежность к оболочке
    def is_inside_convex(self, A):
        for n in range(self.points.size()):
            if A.is_light(self.points.last(), self.points.first()):
                return False
            self.points.push_last(self.points.pop_first())
        return True

        # проверка всех рёбер оболочки на пересечение с прямой
        # и добавление точек пересения в другую оболочку Ribs Cross Add
    def RBA(self, other, A, B):
        for n in range(self.points.size()):
            point1 = self.points.first()
            point2 = self.points.last()
            if check(A.x, A.y, B.x, B.y, point1.x, point1.y,
                                    point2.x, point2.y) is not None:
                #print("Добавление")
                #print(f"({check(A.x, A.y, B.x, B.y, point1.x, point1.y,
                #                    point2.x, point2.y).x},
                #                 {check(C.x, C.y, A.x, A.y, point1.x, point1.y,
                #                                        point2.x, point2.y).y})")
                other = other.add(check(A.x, A.y, B.x, B.y, point1.x, point1.y,
                                    point2.x, point2.y))
            self.points.push_last(self.points.pop_first())

        return other

        # RBA для трёх прямых одного треугольника
    def RBA3(self, other, A, B, C):
        ab_checked = RBA(self, other, A, B)
        ab_bc_checked = RBA(self, ab_checked, B, C)
        return RBA(self, ab_bc_checked, C, A)

        # добавление к другой оболочке точек, лежащих внутри треугольника
        # Add Inside Triangle
    def AIT(self, other, A, B, C):
        default_triangle = Void()
        default_triangle = default_triangle.add(A)
        default_triangle = default_triangle.add(B)
        default_triangle = default_triangle.add(C)
        for n in range(self.points.size()):
            if default_triangle.is_inside_convex(self.points.first()):
                other = other.add(f.points.first())
                #print("Добавлена внутри Треугольника")
            self.points.push_last(self.points.pop_first())
        return other

        # добавление к другой оболочке вершины треугольника, если
        # она принадлежит оболочке f Add Inside Convex
    def AIC(self, other, A, B, C):
        if self.is_inside_convex(A):
            #print("точка A добавлена")
            other = other.add(A)
        if self.is_inside_convex(B):
            #print("точка B добавлена")
            other = other.add(B)
        if self.is_inside_convex(C):
            #print("точка C добавлена")
            other = other.add(C)
        return other


if __name__ == "__main__":
    f = Void()
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(1.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 1.0))
    print(type(f), f.__dict__)
