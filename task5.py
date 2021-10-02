def triangle():
    e = 21
    f = 22
    g = 23
    s = (e + f + g) / 2
    area = (s*(s-e)*(s-f)*(s-g)) ** 0.5
    print("Area is %0.2f" %area)
triangle()