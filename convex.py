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
        ab_checked = self.RBA(other, A, B)
        ab_bc_checked = self.RBA(ab_checked, B, C)
        return self.RBA(ab_bc_checked, C, A)

        # добавление к другой оболочке точек, лежащих внутри треугольника
        # Add Inside Triangle
    def AIT(self, other, A, B, C):
        default_triangle = Void()
        default_triangle = default_triangle.add(A)
        default_triangle = default_triangle.add(B)
        default_triangle = default_triangle.add(C)
        for n in range(self.points.size()):
            if default_triangle.is_inside_convex(self.points.first()):
                other = other.add(self.points.first())
                #print("Добавлена внутри Треугольника")
            self.points.push_last(self.points.pop_first())
        return other

        # добавление к другой оболочке вершины треугольника, если
        # она принадлежит оболочке  Add Inside Convex
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

        # проверка последнего добавленного рёбра фигуры
        # на пересечение с прямой и добавление новых точек пересения, если
        # такие есть
    def check_last(self, other, A, B):
        #print(f"f.points.first() = {f.points.first().x, f.points.first().y}")
        #print(f"f.points.last() = {f.points.last().x, f.points.last().y}")
        #print("проверка AB")
        if check(A.x, A.y, B.x, B.y, self.points.first().x,
                        self.points.first().y, self.points.last().x,
                        self.points.last().y) is not None:
        #print("\nДобавление")
        #print(f"f.points.first() = {f.points.first().x, f.points.first().y}")
        #print(f"f.points.last() = {f.points.last().x, f.points.last().y}")
            other = other.add(check(A.x, A.y, B.x, B.y, self.points.first().x,
                                self.points.first().y, self.points.last().x,
                                                self.points.last().y))
        return other

        # проверка двух последних добавленных рёбер
        # фигуры на пересечение рёбрами с треугольником
        # и добавление точек пересения
    def check_last_triangle(self, other, A, B, C):

        ab1 = self.check_last(other, A, B)
        self.points.push_last(self.points.pop_first())
        ab2 = self.check_last(ab1, A, B)
        bc1 = self.check_last(ab2, B, C)
        self.points.push_first(self.points.pop_last())
        bc2 = self.check_last(bc1, B, C)
        ac1 = self.check_last(bc2, A, C)
        self.points.push_last(self.points.pop_first())
        return self.check_last(ac1, A, C)

        # добавление новой точки если она лежит строго внутри треугольника
        # иначе добавление вершин треугольника, которые лежат внутри этой фигуры
    def aic_fast(self, other, w, A, C, B):
        default_triangle = Void()
        default_triangle = default_triangle.add(A)
        default_triangle = default_triangle.add(B)
        default_triangle = default_triangle.add(C)
        if default_triangle.is_inside_convex(w):
            #print( f"точка W добавлена")
            other = other.add(w)
        else:
            if self.is_inside_convex(A):
                #print("точка А добавлена")
                other = other.add(A)
            if self.is_inside_convex(B):
                #print("точка B добавлена")
                other = other.add(B)
            if self.is_inside_convex(C):
                #print("точка C добавлена")
                other = other.add(C)
        return other

        # индуктивное расширение G(F)
    def induction(self, g, w, A, B, C):
        if not self.is_inside_convex(w):
            self = self.add(w)
            other = self.check_last_triangle(g, A, B, C)
            other = self.aic_fast(g, w, A, B, C)
        return self

        # s` = 0
    def pre_induction(self, A, B, C):
        g = Void()
        g = self.RBA3(g, A, B, C)
        g = self.AIT(g, A, B, C)
        g = self.AIC(g, A, B, C)
        return g


if __name__ == "__main__":
    f = Void()
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(1.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 1.0))
    print(type(f), f.__dict__)
