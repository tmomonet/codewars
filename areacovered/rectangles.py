### Calculate union vs intersections?

def calculate(rectangles):
    if len(rectangles) == 0:
        return 0
    intersectArea = 0
    if len(rectangles) == 1:
        x  = (rectangles[0][2] - rectangles[0][0])
        y  = (rectangles[0][3] - rectangles[0][1])
        intersectArea += (x * y)
        return intersectArea
    for index, rect1 in enumerate(rectangles):
        j = index + 1
        while j < len(rectangles):
            overlap = area(rect1, rectangles[j])
            if overlap is not None:
                intersectArea += overlap
            j += 1

    return intersectArea
        

        
def area(a, b):  # returns None if rectangles don't intersect
    dx = min(a[2], b[2]) - max(a[0], b[0])
    dy = min(a[3], b[3]) - max(a[1], b[1])
    if (dx>=0) and (dy>=0):
        return dx*dy
    else:
        return None
