# def nested(arr):
#     result = []
#     f = lambda x: ([k,v] for k,v in ele.items())
#     for ele in arr:
#         if type(ele) == list or type(ele) == tuple or type(ele) == set:
#             result += nested(ele)
#         elif type(ele) == dict:
#             result += nested(ele.items())
#         else:
#             result += [ele]
#     return result


def h_map(house_map):
    r = 0
    c = 0
    for row in house_map:
        for column in row:
            if column == 1:
                return r, c
            c += 1
        else:
            c = 0
        r += 1
    return False

def solutions(start, house_map):
    s = ''
    stop = h_map(house_map)
    if not stop: return 'NoTable'
    start_row, start_col = start
    stop_row, stop_col = stop
    s += 'D' * abs(start_row - stop_row) if start_row < stop_row else 'U' * abs(start_row - stop_row)
    s += 'R' * abs(start_col - stop_col) if start_col < stop_col else 'L' * abs(start_col - stop_col)
    return s

# cat = [0,0]
# m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#
# print(solutions(cat, m))