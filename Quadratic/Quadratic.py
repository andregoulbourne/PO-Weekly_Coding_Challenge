import math


def quadratic_plus(a, b, c):
    try:
        (-1 * b + math.pow(math.pow(b, 2) - 4 * a * c, .5)) / 2 * a;
    except Exception:
        pass
        return
    else:
        return (-1 * b + math.pow(math.pow(b, 2) - 4 * a * c, .5)) / 2 * a;


def quadratic_minus(a, b, c):
    try:
        (-1 * b - math.pow(math.pow(b, 2) - 4 * a * c, .5)) / 2 * a;
    except Exception:
        pass
        return
    else:
        return (-1 * b - math.pow(math.pow(b, 2) - 4 * a * c, .5)) / 2 * a;


def roots(a, b, c):
    result = []
    minus_root = quadratic_minus(a, b, c)
    plus_root = quadratic_plus(a, b, c)
    if minus_root != None:
        result.append(minus_root)
    if plus_root != None and plus_root != minus_root:
        result.append(plus_root)
    return result;


def number_solutions(a, b, c):
    result = 0
    minus_root = quadratic_minus(a, b, c)
    plus_root = quadratic_plus(a, b, c)
    if minus_root != None:
        result += 1;
    if plus_root != None and plus_root != minus_root:
        result += 1;
    return result;


# Utility functions


def pretty_root(a, b, c):
    result = ""
    root_list = roots(a, b, c)


def list_to_string(list):
    result = ""
    for i in list:
        result += i + ","
    real_result = ""
    for i in range(len(result) - 1):
        real_result += result[i]
    return real_result;
