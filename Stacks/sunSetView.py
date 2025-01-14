def sunsetViews(buildings, direction):
    # Write your code here.

    stack = []
    peakValue = 0

    if direction == "EAST":
        for idx in range(len(buildings) -1, -1, -1):
            if buildings[idx] > peakValue:
                stack.append(idx)
                peakValue = buildings[idx]
            elif buildings[idx] < peakValue:
                continue
    elif direction == "WEST":
        for idx in range(len(buildings)):
            if buildings[idx] > peakValue:
                stack.append(idx)
                peakValue = buildings[idx]
            elif buildings[idx] < peakValue:
                continue
    return stack[::-1] if direction == "EAST" else stack


out = sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "EAST")
print(out)
