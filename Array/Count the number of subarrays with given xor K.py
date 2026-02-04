class Solution:
    def countSubarrays(self, A, k):
        freq = {0: 1}
        
        prefixXor = 0
        count = 0

        for num in A:
            prefixXor ^= num

            target = prefixXor ^ k

            if target in freq:
                count += freq[target]

            freq[prefixXor] = freq.get(prefixXor, 0) + 1

        return count


A = [4, 2, 2, 6, 4]
k = 6
sol = Solution()
print(sol.countSubarrays(A, k))
