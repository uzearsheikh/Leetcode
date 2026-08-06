class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        
        summ = 0
        while n>0:
            rem = n%10
            product *= rem
            summ += rem
            n//=10
        return product - summ
    
        

        