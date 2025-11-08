import math


def fi1(x):
    return math.e ** ((1 / 6) * (5 * x - 7))


def fi1_deriv(x):
    return math.e ** ((1 / 6) * (5 * x - 7)) * (5 / 6)


def fi2(x):
    return 0.2 * (6 * math.log(x) + 7)


def fi2_deriv(x):
    return 6 / (5 * x)


def Root1(eps, q, x):
    delta = 1 # чтобы больше eps была изначально
    while (delta > eps):
        x_next = fi1(x)
        delta = (q) / (1 - q) * abs(x_next - x)
        x = x_next
    
    return x


def Root2(eps, q, x):
    delta = 1 # чтобы больше eps была изначально
    while (delta > eps):
        x_next = fi2(x)
        delta = (q) / (1 - q) * abs(x_next - x)
        x = x_next
    
    return x


def main():
    eps = 0.01
    q1 = fi1_deriv(1)
    q2 = fi2_deriv(2)

    print(f"x_1 = {Root1(eps, q1, 0.5)}")
    print(f"x_2 = {Root2(eps, q2, 2.5)}")


if __name__ == "__main__":
    main()


#x_1 = 0.45749516467331935
#x_2 = 2.4995488782489863