def conquer_island(sea_map):
    coordinates = {"u":[],"m":[]}
    for index, value in enumerate(sea_map):
        for i, j in enumerate(value):
            if j in coordinates.keys():
                coordinates[j].append([index,i])
                
    def coordinate_sum(coord):
        return sum(coord)
    
    if coordinates['u']:
        min_sum_u = min(map(coordinate_sum, coordinates['u']))
        return [tuple(i) for i in coordinates['u'] if coordinate_sum(i) == min_sum_u]
    elif coordinates['m']:
        min_sum_m = min(map(coordinate_sum, coordinates['m']))
        return [tuple(i) for i in coordinates['m'] if coordinate_sum(i) == min_sum_m]
    return []