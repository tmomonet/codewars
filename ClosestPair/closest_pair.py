import math


def closest_pair(points):
    def distance(point1, point2):
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    def closest_brute_force(points):
        min_dist = float("inf")
        p1 = None
        p2 = None
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                d = distance(points[i], points[j])
                if d < min_dist:
                    min_dist = d
                    p1 = points[i]
                    p2 = points[j]
        return p1, p2, min_dist

    def rec(xsorted, ysorted):
        n = len(xsorted)
        if n <= 3:
            return closest_brute_force(xsorted)
        else:
            midpoint = xsorted[n // 2]
            xsorted_left = xsorted[:n // 2]
            xsorted_right = xsorted[n // 2:]
            ysorted_left = []
            ysorted_right = []
            for point in ysorted:
                ysorted_left.append(point) if (point[0] <= midpoint[0]) else ysorted_right.append(point)
            (p1_left, p2_left, delta_left) = rec(xsorted_left, ysorted_left)
            (p1_right, p2_right, delta_right) = rec(xsorted_right, ysorted_right)
            (p1, p2, delta) = (p1_left, p2_left, delta_left) if (delta_left < delta_right) else (p1_right, p2_right,
                                                                                                 delta_right)
            in_band = [point for point in ysorted if midpoint[0] - delta < point[0] < midpoint[0] + delta]
            for i in range(len(in_band)):
                for j in range(i + 1, min(i + 7, len(in_band))):
                    d = distance(in_band[i], in_band[j])
                    if d < delta:
                        (p1, p2, delta) = (in_band[i], in_band[j], d)
            return p1, p2, delta

    def closest(points):
        xsorted = sorted(points, key=lambda p: p[0])
        ysorted = sorted(points, key=lambda p: p[1])
        return rec(xsorted, ysorted)

    p1, p2, _ = closest(points)
    return p1, p2

