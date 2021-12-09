
def count_current_bit(numbers, index):
    counts = 0

    for num in numbers:
        counts += 1 if num[index] == '1' else 0
    
    return counts

# def clear_bits(numbers, index):
#     for 


if __name__ == '__main__':
    # with open('./report.txt') as report:
    #     nums = report.read().splitlines()

    with open('./test.txt') as report:
        nums = report.read().splitlines()

        oxygen, co2 = nums, nums
    length = len(nums[0])

    for i in range(length):
        amt = count_current_bit(oxygen, i)
        print(amt)
        if len(oxygen) == 1: break

        if amt >= length//2:
            print('in amt')
            oxygen = [num for num in oxygen if num[i] == '1']
    
    print(oxygen, nums)