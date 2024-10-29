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

# 测试代码
points = [(1, 2), (4, 6), (7, 8), (2, 3), (5, 1)]
distance, pair = brute_force(points)
print(f"The closest pair is: {pair} with a distance of {distance}")

