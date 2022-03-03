def cycle_in_range(i, start, stop):
    if start <= i <= stop:
        return i
    elif start > i:
        return stop
    return start
