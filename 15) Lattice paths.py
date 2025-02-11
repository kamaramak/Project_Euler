def find_paths(start, end, memo):
    if start == end:
        return 1
    elif start[0] > end[0] or start[1] > end[1]:
        return 0

    r_point, b_point = (start[0] + 1, start[1]), (start[0], start[1] + 1)
    if r_point not in memo:
        memo[r_point] = find_paths(r_point, end, memo)

    if b_point not in memo:
        memo[b_point] = find_paths(b_point, end, memo)

    return memo[r_point] + memo[b_point]


print(find_paths((0, 0), (20, 20), {}))
