# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    '''returns the minimum number of refils required along stops on a trip'''
    n = len(stops)
    stops = [0] + stops + [d] #Since starting from 0  AND ending at D, add 0(n0) and d(n+1) to the list
    numRefills = 0
    currentRefill = 0
    while currentRefill <= n:
        lastRefill = currentRefill
        while (currentRefill<=n) and (stops[currentRefill+1]-stops[lastRefill] <=m):
            currentRefill += 1
        if currentRefill == lastRefill:
            return -1
        if currentRefill<=n:
            numRefills+=1
    return numRefills



if __name__ == '__main__':

    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
