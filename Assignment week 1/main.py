def bound_value(value, minimum_value=0, maximum_value=100):
    if value < minimum_value:
        return minimum_value
    elif value > maximum_value:
        return maximum_value
    else:
        return value