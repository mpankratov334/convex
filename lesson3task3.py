def is_inside_triangle(x0,y0,x1,y1,x2,y2,x3,y3):
    try:
        k12 = (y2-y1) / (x2-x1)
    except(ZeroDivisionError):
        k12=0
    try:
        k23 = (y3-y2) / (x3-x2)
    except(ZeroDivisionError):
        k23=0
    try:
        k13 = (y3-y1) / (x3-x1)
    except(ZeroDivisionError):
        k13=0
    b12 = y1 - x1 * k12
    b13 = y1 - x1 * k13
    b23 = y2 - x2 * k23

    if y1>x1*k23+b23:
        if y2>x2*k13+b13:
            return y0<x0*k12+b12 and y0>x0*k13+b13 and y0>x0*k23+b23
        else:
            if y3>x3*k12+b12:
                return y0>x0*k12+b12 and y0<x0*k13+b13 and y0>x0*k23+b23
            else:
                return y0<x0*k12+b12 and y0<x0*k13+b13 and y0>x0*k23+b23
    else:
        if y2<x2*k13+b13:
            return y0<x0*k12+b12 and y0<x0*k13+b13 and y0>x0*k23+b23
        else:
            if y3>x3*k12+b12:
                return y0>x0*k12+b12 and y0>x0*k13+b13 and y0<x0*k23+b23
            else:
                return y0<x0*k12+b12 and y0>x0*k13+b13 and y0<x0*k23+b23
    return "такого треугольника не существует"
if __name__ == '__main__':
    print(is_inside_triangle(-1, 2, 0, 0, 100, 0, 0, 100))
