import math
import sys

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def read_circle_data(circle_filename):
    with open(circle_filename, 'r') as circle_file:
        center_x, center_y = map(int, circle_file.readline().split())
        radius = int(circle_file.readline())
    return center_x, center_y, radius

def read_points_data(points_filename):
    points = []
    with open(points_filename, 'r') as points_file:
        for line in points_file:
            point_x, point_y = map(int, line.split())
            points.append((point_x, point_y))
    return points

def point_position(center_x, center_y, radius, point_x, point_y):
    dist = distance(center_x, center_y, point_x, point_y)
    if dist < radius:
        return 1  # Точка внутри окружности
    elif dist == radius:
        return 0  # Точка на окружности
    else:
        return 2  # Точка снаружи окружности

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python task2.py circle.txt points.txt")
    else:
        path1 = sys.argv[1] # Получаем данные окружности и точек из файлов
        path2 = sys.argv[2]

        center_x, center_y, radius = read_circle_data(path1)
        points = read_points_data(path2)

# Определяем положение каждой точки относительно окружности и выводим результат
for point_x, point_y in points:
    print(point_position(center_x, center_y, radius, point_x, point_y))