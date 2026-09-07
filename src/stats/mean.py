def mean(x):
    
    if not x:
        # raise an error if the list is empty better than returning None or 0, as mean is undefined for empty lists
        raise ValueError("mean() of an empty list is undefined.") 

    total = 0
    count = 0
    
    for num in x:
        total += num
        count += 1
    return total / count

if __name__ == "__main__":
    assert mean([4, 8, 6, 2]) == 5.0
    assert mean([40, 45, 55, 60, 20, 80]) == 50.0

                