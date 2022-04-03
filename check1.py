from r2point import R2Point


def is_croses(point1, point2, A, B):
    vectorAB = R2Point(B.x - A.x, B.y - A.y)
    vector12 = R2Point(point2.x - point1.x, point2.y - point1.y)
    vectorA1 = R2Point(point1.x - A.x, point1.y - A.y)
    vectorA2 = R2Point(point2.x - A.x, point2.y - A.y)
    vector1A = R2Point(A.x - point1.x, A.y - point1.y)
    vector1B = R2Point(B.x - point1.x, B.y - point1.y)
    Z1 = vectorAB.x * vectorA1.y - vectorA1.x * vectorAB.y
    Z2 = vectorAB.x * vectorA2.y - vectorA2.x * vectorAB.y
    Z3 = vector12.x * vector1A.y - vector1A.x * vector12.y
    Z4 = vector12.x * vector1B.y - vector1B.x * vector12.y
    return Z1 * Z2 >= 0 and Z3 * Z4 >= 0

def cros(point1, point2, A, B):
    vectorAB = R2Point(B.x - A.x, B.y - A.y)
    vector12 = R2Point(point2.x - point1.x, point2.y - point1.y)
    vectorA1 = R2Point(point1.x - A.x, point1.y - A.y)
    vectorA2 = R2Point(point2.x - A.x, point2.y - A.y)
    vector1A = R2Point(A.x - point1.x, A.y - point1.y)
    vector1B = R2Point(B.x - point1.x, B.y - point1.y)
    Z1 = vectorAB.x * vectorA1.y - vectorA1.x * vectorAB.y
    Z2 = vectorAB.x * vectorA2.y - vectorA2.x * vectorAB.y
    Z3 = vector12.x * vector1A.y - vector1A.x * vector12.y
    Z4 = vector12.x * vector1B.y - vector1B.x * vector12.y
    cross = R2Point(point1.x + (point2.x - point1.x) * abs(Z1 / (Z2 - Z1)),
    point1.y + (point2.y - point1.y) * abs(Z1 / (Z2 - Z1)))
    return cross


if __name__ == '__main__':
    while True:
        point1 = R2Point()
        point2 = R2Point()
        A = R2Point()
        B = R2Point()
        print(is_croses(point1, point2, A, B))
        if is_croses(point1, point2, A, B):
            print(cros(point1, point2, A, B).x, cros(point1, point2, A, B).y)
