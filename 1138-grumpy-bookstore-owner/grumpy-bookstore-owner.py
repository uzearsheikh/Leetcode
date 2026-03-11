class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        # Step 1: Calculate the number of satisfied customers without using the secret technique
        satisfied_customers = 0
        for i in range(n):
            if not grumpy[i]:
                satisfied_customers += customers[i]
        
        # Step 2: Calculate the additional satisfied customers using the sliding window
        max_additional_satisfied = 0
        additional_satisfied = 0
        
        # Calculate the additional satisfied customers for the first 'minutes' window
        for i in range(minutes):
            if grumpy[i]:
                additional_satisfied += customers[i]
        
        max_additional_satisfied = additional_satisfied
        
        # Slide the window across the rest of the array
        for i in range(minutes, n):
            if grumpy[i]:
                additional_satisfied += customers[i]
            if grumpy[i - minutes]:
                additional_satisfied -= customers[i - minutes]
            max_additional_satisfied = max(max_additional_satisfied, additional_satisfied)
        
        # Step 3: Return the total maximum satisfied customers
        return satisfied_customers + max_additional_satisfied

            