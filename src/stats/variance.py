from src.stats.mean import mean
from src.mathx.sqrt_newton import sqrt_newton


def variance(x):
    '''
    Calculate the variance of a list of numbers.
    Mean of squared differences from the mean.
    '''
    if not x:
        raise ValueError("variance() of an empty sequence is undefined")

    mean_x = mean(x)
    sum_of_squared_diff = 0
    count_x = 0

    for num in x:
        sum_of_squared_diff += (num - mean_x) ** 2
        count_x += 1

    # A single value has no spread to compare, so variance is undefined here.
    if count_x <= 1:
        raise ValueError("variance() requires at least two data points")

    # Population variance divides by n, not n - 1; sample variance is a later extension.
    return sum_of_squared_diff / count_x


def std_dev(x):
    '''
    Calculate the standard deviation of a list of numbers.
    Square root of the variance, in the data's units.
    '''
    return sqrt_newton(variance(x))


if __name__ == "__main__":
    tol = 1e-6

    try:
        variance([])
        assert False, "empty input should have raised"
    except ValueError:
        pass

    try:
        variance([7])
        assert False, "single-element input should have raised"
    except ValueError:
        pass

    assert abs(variance([2, 4, 6, 8]) - 5) < tol
    assert abs(variance([0, 5, 25]) - (350 / 3)) < tol
    assert abs(variance([10, 10, 10]) - 0) < tol
    assert abs(variance([1, 5, 9]) - (32 / 3)) < tol
    assert abs(variance([4, 5, 6]) - (2 / 3)) < tol

    assert abs(variance([100, 105, 125]) - variance([0, 5, 25])) < tol
    assert abs(variance([0, 10, 50]) - (4 * variance([0, 5, 25]))) < tol

    assert abs(std_dev([2, 4, 6, 8]) - (5 ** 0.5)) < tol
    assert abs(std_dev([10, 10, 10]) - 0) < tol

    dataset_a = [0, 5, 25]
    squares = []
    for value in dataset_a:
        squares.append(value ** 2)
    mean_of_squares = mean(squares)

    x_bar = mean(dataset_a)
    assert abs((mean_of_squares - (x_bar ** 2)) - variance(dataset_a)) < tol

    print("all passed")




