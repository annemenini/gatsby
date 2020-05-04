import math


def generate_polygon(num_vertices, scale, offset):
    vertices_list = []
    for i in range(num_vertices):
        alpha = i * 2 * math.pi / num_vertices
        v = (offset[0] + scale * math.cos(alpha), offset[1] + scale * math.sin(alpha))
        vertices_list.append(v)
    return vertices_list


def generate_interior_polygon(vertices_list, step):
    new_vertices_list = []
    n = len(vertices_list)
    for i, vertex in enumerate(vertices_list):
        vx = vertices_list[(i + 1) % n][0] - vertex[0]
        vy = vertices_list[(i + 1) % n][1] - vertex[1]
        d = math.sqrt(vx ** 2 + vy ** 2)
        if d < step:
            return None
        x = vertex[0] + step * vx / d  # TODO (Anne Menini): Add check
        y = vertex[1] + step * vy / d
        new_vertices_list.append((x, y))
    return new_vertices_list


def get_direction(vertices_list):
    direction = None
    is_convex = True
    n = len(vertices_list)
    for i, vertex in enumerate(vertices_list):
        x0 = vertices_list[(i - 1) % n][0] - vertex[0]
        x1 = vertices_list[(i + 1) % n][0] - vertex[0]
        y0 = vertices_list[(i - 1) % n][1] - vertex[1]
        y1 = vertices_list[(i + 1) % n][1] - vertex[1]
        vector_product = x0 * y1 - x1 * y0
        if not vector_product == 0:
            if direction is None:
                direction = vector_product > 0
            else:
                if not direction == (vector_product > 0):
                    is_convex = False
                    break
    return is_convex, direction
