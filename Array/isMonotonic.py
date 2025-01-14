def isMonotonic(array):
    # Write your code here.
    # Consider two test scenarios - i < j or i > j throughout.
    # If it fails, it is not monotonic

    if len(array) <= 2:
        return True

    direction = array[1] - array[0]

    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i - 1]
            continue

        if breaksDirection(direction, array[i - 1], array[i]):
            return False

    return True


def breaksDirection(direction, prev, curr):
    difference = curr - prev

    if direction > 0:
        return difference < 0

    return difference > 0


out = isMonotonic([1, 5, 10, 1100, 1100])
print(out)
