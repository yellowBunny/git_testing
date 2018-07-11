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

def room_map(board):
    r = 0
    c = 0
    for row in board:
        for column in row:
            if column == 1:
                return [r, c]
            c += 1
        else:
            c = 0
        r += 1
    return False

# cat = [1,3]
# m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def cat_coordinate(cat, room):
    row, col = cat
    if row < 0 or col < 0:
        return True
    try:
        room[row][col] = 'a'
        return False
    except:
        return True

#print(cat_coordinate(cat, m))

def solutions(start, house_map):
    s = ''
    stop = room_map(house_map)
    if not stop: return 'NoTable'
    start_row, start_col = start
    stop_row, stop_col = stop
    s += 'D' * abs(start_row - stop_row) if start_row < stop_row else 'U' * abs(start_row - stop_row)
    s += 'R' * abs(start_col - stop_col) if start_col < stop_col else 'L' * abs(start_col - stop_col)
    return s


def longest_consec(strarr, k):
    if not strarr or len(strarr) < k or k <= 0 : return ''
    result = []
    for ele in strarr:
        if ele not in result:
            result += [ele]

    return result

# k = 3
# l = ["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"]
# print(longest_consec(l, 2))
class Dictionary():
    def __init__(self):
        self.words = []
        self.definitions = []

    def newentry(self, word, definition):
        self.words += [word]
        self.definitions += [definition]

    def look(self, key):
        for i in range(len(self.words)):
            if key == self.words[i]:
                return self.definitions[i]
        else:
            return "Can't find entry for {}".format(key)


def frelancer(minutes, array):
    l = list(map(lambda x: [x[0] * 60, x[1]] , array ))
    result = [sum(arr) for arr in l]
    print(sum(result), minutes)
    return 'easy' if sum(result) >= minutes else 'need to work {}'.format(minutes - sum(result))

print(frelancer(70, [(1,20)]))