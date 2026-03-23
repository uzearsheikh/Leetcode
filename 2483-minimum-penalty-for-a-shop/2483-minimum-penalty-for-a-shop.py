class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        
        # Initial penalty: if we close at hour 0 (all 'Y' are missed)
        penalty = customers.count('Y')
        min_penalty = penalty
        best_hour = 0
        
        for i in range(n):
            # If customer is 'Y', we reduce penalty (we serve them now)
            if customers[i] == 'Y':
                penalty -= 1
            else:
                
                penalty += 1
            
            # Update best hour
            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = i + 1
        
        return best_hour