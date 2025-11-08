import math


def fi1(x):
    return (1 / 2) * (3 - 2 * math.log(x))


def fi1_deriv(x):
    return (-1) * (1 / x)


def Root1(eps, q, x):
    delta = 1 # чтобы больше eps была изначально
    while (delta > eps):
        x_next = fi1(x)
        delta = (q) / (1 - q) * abs(x_next - x)
        x = x_next
    
    return x

def main():
    eps = 0.01
    left_edge = 1.1
    right_edge = 2
    x = 1.5 # произвольное x в отрезке изоляции
    q1 = abs(fi1_deriv(left_edge))

    print(f"x_1 = {Root1(eps, q1, x)}")


if __name__ == "__main__":
    main()


# x_1 = 1.2645651980694472