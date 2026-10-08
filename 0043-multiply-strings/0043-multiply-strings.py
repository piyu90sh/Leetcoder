class Solution(object):
    def multiply(self, num1, num2):
        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                a = ord(num1[i]) - ord('0')
                b = ord(num2[j]) - ord('0')

                total = a * b + result[i + j + 1]
                result[i + j + 1] = total % 10
                result[i + j] += total // 10

        result = ''.join(map(str, result)).lstrip('0')
        return result if result else '0'