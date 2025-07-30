class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # Solution - Chatgpt (simple and easy) Prblem is hard to understand
        total_gas, current_tank, start_index = 0, 0, 0
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]

            if current_tank < 0:
                current_tank = 0
                start_index = i + 1
        
        return start_index if total_gas >= 0 else - 1

sol = Solution(gas = [1,2,3,4,5], cost = [3,4,5,1,2])
print(sol)
