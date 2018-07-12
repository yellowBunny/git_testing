
def frelancer(minutes, array):
    l = list(map(lambda x: [x[0] * 60, x[1]], array))
    result = sum(sum(arr) for arr in l)
    print(minutes, result)
    time = 0 if minutes - result < 0 else abs(minutes - result)
    print(time)
    h = time // 60
    m = time - h * 60
    print(h, m)
    return 'Easy Money!' if minutes <= result else 'I need to work {} hour(s) and {} minute(s)'.format(h, m)


print(frelancer(60, [(0,0)]))