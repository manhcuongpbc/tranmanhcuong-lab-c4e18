def is_inside(point, rectangle):
    x_min = rectangle[0]
    x_max = x_min + rectangle[2]
    y_min = rectangle[1]
    y_max = x_min + rectangle[3]

    if x_min <= point[0] <= x_max and y_min <= point[1] <= y_max:
        return True
    else:
        return False

print(is_inside([100, 120], [140, 60, 100, 200]))
