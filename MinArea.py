def minArea(points, k):

    points.sort()  

    min_area = float('inf')
    for i in range(len(points) - k + 1):
        for j in range(i + k - 1, len(points)):

            side = max(points[j][0] - points[i][0], points[j][1] - points[i][1]) + 1
            square_area = side * side

            enclosed_points = 0
            for x, y in points:
                if points[i][0] < x < points[i][0] + side and points[i][1] < y < points[i][1] + side:
                    enclosed_points += 1
                    if enclosed_points >= k:
                        min_area = min(min_area, square_area)
                        break

    return min_area