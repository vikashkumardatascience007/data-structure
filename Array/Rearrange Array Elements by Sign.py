class ArrayManipulator:
    def rearrange_by_sign(self, A):
        n = len(A)
        ans = [0] * n  

        pos_index = 0  
        neg_index = 1  

        for i in range(n):
            if A[i] < 0:
                ans[neg_index] = A[i]
                neg_index += 2
            else:
                ans[pos_index] = A[i]
                pos_index += 2

        return ans

if __name__ == "__main__":
    A = [1, 2, -4, -5]
    obj = ArrayManipulator()
    result = obj.rearrange_by_sign(A)
    print(" ".join(map(str, result)))
