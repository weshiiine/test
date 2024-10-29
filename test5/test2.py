import math
import sys

def brute_force(points):
    min_distance = sys.maxsize
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
            if dist < min_distance:
                min_distance = dist
                closest_pair = (points[i], points[j])
    return min_distance, closest_pair

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def closest_pair_recursive(points_sorted_by_x, points_sorted_by_y):
    if len(points_sorted_by_x) <= 3:
        return brute_force(points_sorted_by_x)
    
    mid = len(points_sorted_by_x) // 2
    midpoint = points_sorted_by_x[mid]

    left_by_x = points_sorted_by_x[:mid]
    right_by_x = points_sorted_by_x[mid:]
    left_by_y = list(filter(lambda x: x in left_by_x, points_sorted_by_y))
    right_by_y = list(filter(lambda x: x in right_by_x, points_sorted_by_y))

    (left_distance, left_pair) = closest_pair_recursive(left_by_x, left_by_y)
    (right_distance, right_pair) = closest_pair_recursive(right_by_x, right_by_y)

    if left_distance <= right_distance:
        min_distance, closest_pair = left_distance, left_pair
    else:
        min_distance, closest_pair = right_distance, right_pair

    # Check for cross-boundary pairs
    (cross_distance, cross_pair) = closest_cross_pair(points_sorted_by_x, points_sorted_by_y, midpoint, min_distance)
    if cross_distance < min_distance:
        return cross_distance, cross_pair

    return min_distance, closest_pair

def closest_cross_pair(points_sorted_by_x, points_sorted_by_y, midpoint, delta):
    strip = [p for p in points_sorted_by_y if abs(p[0] - midpoint[0]) < delta]
    min_distance = delta
    closest_pair = None
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) >= delta:
                break
            dist = distance(strip[i], strip[j])
            if dist < min_distance:
                min_distance = dist
                closest_pair = (strip[i], strip[j])
    return min_distance, closest_pair

def closest_pair(points):
    points_sorted_by_x = sorted(points, key=lambda x: x[0])
    points_sorted_by_y = sorted(points, key=lambda x: x[1])
    return closest_pair_recursive(points_sorted_by_x, points_sorted_by_y)

# 测试代码
points = [(1, 2), (4, 6), (7, 8), (2, 3), (5, 1)]
distance, pair = closest_pair(points)
print(f"The closest pair is: {pair} with a distance of {distance}")

