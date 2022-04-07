from itertools import combinations


def get_combinations(input):
    # print("comb in",input)
    output = sum([list(map(list, combinations(input, i))) for i in range(len(input) + 1)], [])
    result = []
    for each in output:
        result.append(" ".join(each).strip())
    result.reverse()
    # print(result[1:])
    return result[:-1]
