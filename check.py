from r2point import R2Point


def check(ax, ay, bx, by, x1, y1, x2, y2):
    dx, dy, c = ax - bx, ay - by, (ax - ay) * (ay - by)
    dy12, dx12 = y1 - y2, x1 - x2
    c12 = y1 * dx12 - x1 * dy12
    #print(f"1-2: {dx12}y = {dy12}x + {c12}")
    #print(f"a-b: {dx}y = {dy}x + {c}")
    determinant = dx12 * dy - dx * dy12
    #print(f"determinant = {determinant}")
    if determinant != 0:
        if dy == 0:
        #p_x и p_y - координаты пересечения двух прямых
            p_y = (ax - x1) * dy * dy12 - ay * dx * dy12 + y1 * dx12 * dx
            p_x = (p_y * dx12 - c12) / dy12
            if ( min(x1, x2) <= p_x <= max(x1, x2) and
                min(y1, y2) <= p_y <= max(y1, y2) and
                min(ax, bx) <= p_x <= max(bx, ax) and
                min(by, ay) <= p_y <= max(by, ay) ):
                # g.add(R2Point(x, y))
                #print( f"точка ({p_x}, {p_y}) добавлена")
                return R2Point(p_x, p_y)
            return None
        if dy12 == 0:
            p_y = c12 / dx12
            p_x = (p_y * dx - c) / dy
            if ( min(x1, x2) <= p_x <= max(x1, x2) and
                min(y1, y2) <= p_y <= max(y1, y2) and
                min(ax, bx) <= p_x <= max(bx, ax) and
                min(by, ay) <= p_y <= max(by, ay)):
                #print( f"точка ({p_x}, {p_y}) добавлена")
                return R2Point(p_x, p_y)
            return None
        p_y = (c12 * dy - c * dy12) / determinant
        p_x = (p_y * dx - c) / dy
        if (min(x1, x2) <= p_x <= max(x1, x2) and
            min(y1, y2) <= p_y <= max(y1, y2) and
            min(ax, bx) <= p_x <= max(bx, ax) and
            min(by, ay) <= p_y <= max(by, ay)):
            # g.add(R2Point(x, y))
            #print( f"точка ({p_x}, {p_y}) добавлена")
            return R2Point(p_x, p_y)
    return None

if __name__ == '__main__':
    while True:
        A = R2Point()
        B = R2Point()
        p1 = R2Point()
        p2 = R2Point()
        check(A.x, A.y, B.x, B.y, p1.x, p1.y, p2.x, p2.y)
