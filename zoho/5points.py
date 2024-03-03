from collections import defaultdict

def maxPoints(points):
    if len(points) < 3:
        return len(points)

    max_points = 0

    for i, (x1, y1) in enumerate(points):
        slopes = defaultdict(int)
        overlap = 0
        current_max = 0

        for j in range(i + 1, len(points)):
            x2, y2 = points[j]

            if x1 == x2 and y1 == y2:
                overlap += 1
                continue

            dx = x2 - x1
            dy = y2 - y1

            # Calculate the slope without gcd
            if dx == 0:  # vertical line
                slope = float('inf')
            else:
                slope = dy / dx

            slopes[slope] += 1
            current_max = max(current_max, slopes[slope])

        max_points = max(max_points, current_max + overlap + 1)

    return max_points

# Example usage:
points = [[1,1],[2,2],[3,3]]
print(maxPoints(points))  # Output: 3
