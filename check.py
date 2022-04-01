def check(ax, ay, bx, by):
    dx, dy, c = ax - bx, ay - by, ay * (ax - bx) - ax * (ay - by)
    x1, y1 = int(input("x1 -> ")), int(input("y1 -> "))
    x2, y2 = int(input("x2 -> ")), int(input("y2 -> "))
    dy12, dx12 = y1 - y2, x1 - x2
    c12 = y1 * dx12 - x1 * dy12
    # print(f"1-2: {dx12}y = {dy12}x + {c12}")
    # print(f"a-b: {dx}y = {dy}x + {c}")
    determinant = dx12 * dy - dx * dy12
    # print(f"determinant = {determinant}")
    if determinant != 0:
        if dy == 0:
            p_y = c / dx
            p_x = (p_y * dx12 - c12) / dy12
            if ( min(x1, x2) <= p_x <= max(x1, x2) and
                min(y1, y2) <= p_y <= max(y1, y2) and
                min(ax, bx) <= p_x <= max(bx, ax) and
                min(by, ay) <= p_y <= max(by, ay) ):
                # g.add(R2Point(x, y))
                print(f"точка пресечения ({p_x}, {p_y}) добавлена")
            # else:
                # print(f"({p_x}, {p_y})")
            return
        if dy12 == 0:
            p_y = c12 / dx12
            p_x = (p_y * dx - c) / dy
            if ( min(x1, x2) <= p_x <= max(x1, x2) and
                min(y1, y2) <= p_y <= max(y1, y2) and
                min(ax, bx) <= p_x <= max(bx, ax) and
                min(by, ay) <= p_y <= max(by, ay) ):
                # g.add(R2Point(x, y))
                print(f"точка пресечения ({p_x}, {p_y}) добавлена")
            # else:
                #print(f"({p_x}, {p_y})")

            return
        p_y = (c12 * dy - c * dy12) / determinant
        print(p_y)
        print(dx)
        print(dy)
        print(c)
        p_x = (p_y * dx - c) / dy
        if ( min(x1, x2) <= p_x <= max(x1, x2) and
            min(y1, y2) <= p_y <= max(y1, y2) and
            min(ax, bx) <= p_x <= max(bx, ax) and
            min(by, ay) <= p_y <= max(by, ay) ):
            # g.add(R2Point(x, y))
            print(f"точка пресечения ({p_x}, {p_y}) добавлена")
        else:
            print(f"({p_x}, {p_y})")

if __name__ == '__main__':
    while True:
        ax = int(input("A.x -> "))
        ay = int(input("A.y -> "))
        bx = int(input("B.x -> "))
        by = int(input("B.y -> "))
        check(ax, ay, bx, by)
