"""
You are given two integer arrays num1 and num2,
sorted in non-decreasing order, and two integers m and n,
representing the number of elements num1 and num2 respectively.

Merge num1 and num2 into a single array sorted in nom-decreasing order.

The final sorted array should not be returned by the function,
but instead be stored inside the array num1.

To accommodate this,num1 has a length of m + n, where the first m elements
denote the elements that should be merged,
"""

class Solution:
    @staticmethod
    def merge(num1: list[int], m: int, num2: list[int], n: int) -> None:
        # Deep Copy를 통해 별도의 메모리를 참조하는 첫번째 배열을 만든다.
        num1_copy = num1[0: m][:]
        num2 = num2[0: n]

        # 배열을 스택처럼 사용하여 맨 처음 원소를 pop하는 방법도 생각해 보았으나
        # pop함수는 시간복잡도가 O(n)이므로 사용하지 않는다.
        num_1_index = 0
        num_2_index = 0

        current_index = 0

        while num_1_index + num_2_index + 1 <= len(num1):
            if num_1_index == m:
                num1[current_index] = num2[num_2_index]
                num_2_index += 1

            elif num_2_index == n:
                num1[current_index] = num1_copy[num_1_index]
                num_1_index += 1

            else:
                if num1_copy[num_1_index] >= num2[num_2_index]:
                    num1[current_index] = num2[num_2_index]
                    num_2_index += 1
                else:
                    num1[current_index] = num1_copy[num_1_index]
                    num_1_index += 1

            current_index += 1

Solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
Solution.merge([1], 1, [], 0)
Solution.merge([0], 0, [1], 1)
