class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:

            for i in range(l, r):

                offset = i - l
                top = l
                bottom = r

                # save top-left
                topLeft = matrix[top][i]

                # bottom-left -> top-left
                matrix[top][i] = matrix[bottom - offset][l]

                # bottom-right -> bottom-left
                matrix[bottom - offset][l] = matrix[bottom][r - offset]

                # top-right -> bottom-right
                matrix[bottom][r - offset] = matrix[i][r]

                # top-left -> top-right
                matrix[i][r] = topLeft

            l += 1
            r -= 1