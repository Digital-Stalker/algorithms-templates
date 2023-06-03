def len_flower_beds(cord, count):
    result = []
    flowerbeds = sorted(cord, key=lambda j: [j[0], j[1]])
    for i in range(count-1):
        if flowerbeds[i][1] >= flowerbeds[i + 1][0]:
            flowerbeds[i+1][0] = min(flowerbeds[i][0], flowerbeds[i+1][0])
            flowerbeds[i+1][1] = max(flowerbeds[i][1], flowerbeds[i+1][1])
        else:
            result.append(flowerbeds[i])
    result.append(flowerbeds[-1])
    for i in result:
        print(*i)


if __name__ == '__main__':
    gardeners = int(input())
    beds = [list(map(int, input().split())) for _ in range(gardeners)]
    len_flower_beds(beds, gardeners)
