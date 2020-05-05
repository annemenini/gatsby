def tile_hhvv(dim_x, dim_y, num_x, num_y):
    tile_x = dim_x / num_x
    tile_y = dim_y / num_y
    polygon_list = []
    for x in range(num_x):
        for y in range(num_y):
            is_vertical = (x + y) % 2 == 0
            if is_vertical:
                tile_0 = [(x * tile_x, y * tile_y),
                          ((x + 0.5) * tile_x, y * tile_y),
                          ((x + 0.5) * tile_x, (y + 1) * tile_y),
                          (x * tile_x, (y + 1) * tile_y)]
                tile_1 = [((x + 1) * tile_x, y * tile_y),
                          ((x + 0.5) * tile_x, y * tile_y),
                          ((x + 0.5) * tile_x, (y + 1) * tile_y),
                          ((x + 1) * tile_x, (y + 1) * tile_y)]
                polygon_list.extend([tile_0, tile_1])
            else:
                tile_0 = [(x * tile_x, y * tile_y),
                          ((x + 1) * tile_x, y * tile_y),
                          ((x + 1) * tile_x, (y + 0.5) * tile_y),
                          (x * tile_x, (y + 0.5) * tile_y)]
                tile_1 = [(x * tile_x, (y + 1) * tile_y),
                          ((x + 1) * tile_x, (y + 1) * tile_y),
                          ((x + 1) * tile_x, (y + 0.5) * tile_y),
                          (x * tile_x, (y + 0.5) * tile_y)]
                polygon_list.extend([tile_0, tile_1])
    return polygon_list
