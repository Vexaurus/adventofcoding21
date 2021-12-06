if __name__ == '__main__':
    with open('../tests/sonar_input.txt') as raw:
        scans = raw.readlines()
        scans = list(map(int, scans))

    # with open('../tests/testing.txt', 'r') as raw:
    #     scans = raw.readlines()
    #     scans = list(map(int, scans))

    count = 0

    for i in range(len(scans)):
        # Get rolling sum
        a = sum(scans[i:i+3])
        b = sum(scans[i+1:i+4])

        # Check that the sum is at least 3.
        if len(scans[i+1:i+4]) < 3:
            break

        # Add to the count if larger
        count += 1 if b > a else 0
    
    # return count
    print(count)