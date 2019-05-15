import itertools

def fit1(cx, cy, bx, by):
    """
    Function accepts container dimensions cx and cy together with box dimensions bx, by
    and calcualtes how many boxes fit in a container.

    x-axis and y-axis of the container and the box are aligned in this example
    """
    vertical_fit_count = cx // bx
    horizontal_fit_count = cy // by

    return vertical_fit_count * horizontal_fit_count


def fit2(cx, cy, bx, by):
    """
    Function accepts container dimensions cx and cy together with box dimensions bx, by
    and calcualtes how many boxes fit in a container.

    In this case all boxes can be turned 90 degrees to maximise the fit count
    """
    fit = fit1(cx, cy, bx, by)
    rotated_fit = fit1(cx, cy, by, bx)

    return max(fit, rotated_fit)


def fit3(cx, cy ,cz, bx, by,bz):
    # Generate all posible box orientation permutations and find maximal
    box_dim_permuatations = itertools.permutations([bx, by, bz])
    max_fit = 0

    for bx, by, bz in box_dim_permuatations:
        fit = (cx//bx) * (cy//by) * (cz//bz)
        if fit > max_fit:
            max_fit = fit
    return max_fit


def fitn(c, b):
    b_permutations = list(itertools.permutations(b))
    max_fit = 0

    for p in b_permutations:
        fit = 1
        for cd, bd in zip(c, p):
            fit *= (cd // bd)
        if fit > max_fit:
            max_fit = fit

    return max_fit