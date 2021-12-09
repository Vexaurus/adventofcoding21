if __name__ == '__main__':
    with open('./report.txt') as report:
        nums = report.read().splitlines()

    # with open('./test.txt') as report:
    #     nums = report.read().splitlines()

    length = len(nums)
    counts = {}
    for num in nums:
        for ind, bit in enumerate(num):
            counts[str(ind)] = counts.get(str(ind), 0) + (1 if bit == '1' else 0)
    
    gamma = '0b'
    epsilon = '0b'
    for c in counts.values():
        gamma += '1' if c > (length // 2) else '0'
        epsilon += '0' if c > (length // 2) else '1'

    print(int(gamma, base=2) * int(epsilon, base=2))

