from mean import mean
from code.mathx.sqrt_newton import sqrt_newton

def variance(x):
    if not x:
        raise ValueError("variance() of an empty sequence is undefined")
    
if __name__ == "__main__":
    pass
    
    mean_x = mean(x)
    sqrt_newton(sum((xi - mean_x) ** 2 for xi in x) / len(x))