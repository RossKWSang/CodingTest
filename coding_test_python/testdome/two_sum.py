def find_two_sum(numbers, target):
    def binary_search(numbers, target):
        left, right = 0, len(numbers) - 1
        middle = left + (right - left) // 2
        while left <= right:
            middle = (left + right) // 2
            if numbers[middle] == target:
                return middle
            elif numbers[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return middle

    numbers = sorted(numbers)
    for index, num in enumerate(numbers):
        temp_numbers = numbers[:index] + numbers[index + 1:]
        print(num, temp_numbers[binary_search(temp_numbers, target - num)])

    print(numbers)


if __name__ == '__main__':
    find_two_sum(numbers=[2, 11, 7, 15], target=9)
    find_two_sum(numbers=[3, 1, 5, 7, 5, 9], target=10)
