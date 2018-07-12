
def frelancer(minutes, array):
    l = list(map(lambda x: [x[0] * 60, x[1]] , array ))
    result = [sum(arr) for arr in l]
    print(sum(result), minutes)
    return 'easy' if sum(result) >= minutes else 'need to work {}'.format(minutes - sum(result))

print(frelancer(70, [(1,20)]))