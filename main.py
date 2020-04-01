import itertools

lis = ['back', 'end', 'front', 'tree']


def can_create(lis, word):
    comb_tup = list(itertools.combinations(lis, 2))
    combination = [''.join(tups) for tups in comb_tup]
    return True if word in combination else False


if __name__ == "__main__":
    a = can_create(lis, 'backend')
    print(a)
