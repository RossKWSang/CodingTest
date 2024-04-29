def count_numbers(numbers, entry):
    start = 0
    end = len(numbers) - 1
    mid = (start + end) // 2

    while start <= end - 1:
        mid = (start + end) // 2

        if numbers[mid] == entry:
            return mid

        elif numbers[mid] > entry:
            end = mid

        else:
            start = mid + 1

    return mid


print(count_numbers([1, 3, 5, 7], 4))
