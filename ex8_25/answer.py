def triangle(a):
  return recursiveTriangle(a, a)


def recursiveTriangle(b, c):
    if (b == 1):
        e = ""
        for i in range(c-b):
            e += " "
        e += "*\n"
        return e
    else:
        f = ""
        for i in range(c-b):
            f += " "
        for i in range(b):
            f += "*"
        f += "\n"
        return f + recursiveTriangle(b-1, c)



print(recursiveTriangle(3, 5))
print(triangle(8))
