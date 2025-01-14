def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.

    maxSpeed = 0
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    if fastest:
        reverseArrayInPlace(redShirtSpeeds)

    for i in range(len(redShirtSpeeds)):
        maxSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return maxSpeed


def reverseArrayInPlace(array):
    start = 0
    end = len(array) - 1

    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1


out = tandemBicycle([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], True)
print(out)