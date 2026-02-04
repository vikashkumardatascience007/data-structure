class Solution:
    def subarraySum(self, arr, k):
        n = len(arr)
        count = 0
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += arr[j]
                if total == k:
                    count += 1
        return count


if __name__ == "__main__":
    arr = [3, 1, 2, 4]
    k = 6

    sol = Solution()
    result = sol.subarraySum(arr, k)
    print("The number of subarrays is:", result)
