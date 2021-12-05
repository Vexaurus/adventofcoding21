#!/usr/bin/env python3.10

if __name__ == '__main__':

    with open('./input.txt') as scan:
        scans = scan.readlines()

    prev, count = 0, -1

    for res in scans:
        if int(res) > prev:
            count += 1

        prev = int(res)
    
    print(count)