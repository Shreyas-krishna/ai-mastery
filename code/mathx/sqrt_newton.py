def sqrt_newton(x):
    '''
    Square root of x by Newton's iteration.
    If g² > x, then g > x/g, so the two values sit on opposite sides of √x and their average moves inward.
    If g² < x, the inequality flips: g < x/g, and the pair still brackets √x from opposite sides.
    '''
    if x == 0:
        return 0

    if x < 0:
        raise ValueError("Input must be a positive number")

    guess = x / 2
    tolerance = 1e-6

    while True:
        new_guess = (guess + x/guess)/2
        if abs(new_guess - guess) < tolerance:
            return new_guess

        guess = new_guess


if __name__ == "__main__":

    try:
        sqrt_newton(-4)
        assert False, "negative input should have raised"
    except ValueError:
        pass


    for x in [25, 49, 5, 2, 0.25, 0, 1e6]:
        assert abs(sqrt_newton(x) - x ** 0.5) < 1e-6, x

    print("all passed")
