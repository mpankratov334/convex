from pytest import approx
from r2point import R2Point
from convex import Void


class TestModification:
    # Модификация: Вычисляется сумма квадратов расстояний
    # от начала координат до середин рёбер выпуклой оболочки.

    # У нульугольника сумма равна нулю
    def test_void(self):
        self.f = Void()
        assert self.f.sum_squares() == approx(0.0)

    # У одноугольника сумма равна нулю
    def test_point(self):
        self.f = Void()
        self.f = self.f.add(R2Point(1, 0))
        assert self.f.sum_squares() == approx(0.0)

    # У двуугольника сумма равна координатам его середины
    def test_segment_1(self):
        self.f = Void()
        self.f = self.f.add(R2Point(1, 1))
        self.f = self.f.add(R2Point(-1, -1))
        assert self.f.sum_squares() == approx(0.0)

    def test_segment_2(self):
        self.f = Void()
        self.f = self.f.add(R2Point(2, 2))
        self.f = self.f.add(R2Point(0, 0))
        assert self.f.sum_squares() == approx(2.0)

    # Проверка у треугольника
    def test_polygon_1(self):
        self.triangle = Void()
        self.triangle = self.triangle.add(R2Point(1, 1))
        self.triangle = self.triangle.add(R2Point(1, 0))
        self.triangle = self.triangle.add(R2Point(0, 1))
        assert self.triangle.sum_squares() == approx(3.0)

    # Проверка при удалении одной стороны
    def test_polygon_2(self):
        self.quadro = Void()
        self.quadro = self.quadro.add(R2Point(1, 1))
        self.quadro = self.quadro.add(R2Point(-1, 1))
        self.quadro = self.quadro.add(R2Point(1, -1))
        # Далее удаляется сторона
        self.quadro = self.quadro.add(R2Point(-1, -1))
        assert self.quadro.sum_squares() == approx(4)

    # Проверка при удалении трёх сторон
    def test_polygon_3(self):
        self.quadro = Void()
        self.quadro = self.quadro.add(R2Point(1, 1))
        self.quadro = self.quadro.add(R2Point(1, -1))
        self.quadro = self.quadro.add(R2Point(-1, 1))
        self.quadro = self.quadro.add(R2Point(-1, -1))
        self.quadro = self.quadro.add(R2Point(-1, 2))
        assert self.quadro.sum_squares() == approx(5.5)
        self.quadro = self.quadro.add(R2Point(-1, -2))
        assert self.quadro.sum_squares() == approx(6.5)
        self.quadro = self.quadro.add(R2Point(3, 0))
        assert self.quadro.sum_squares() == approx(5)
