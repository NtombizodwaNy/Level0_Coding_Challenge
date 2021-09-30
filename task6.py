def max( e, f ):
    if e > f:
       return e
    return f
def maxx( e, f, j ):
    return max( e, max( f, j ) )
print("max number is ",maxx(6, 9, 99))