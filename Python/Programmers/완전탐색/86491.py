def solution(sizes):
    return max(list(map(max, sizes))) * max(list(map(min, sizes)))