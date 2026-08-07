class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pairs = sorted(zip(position, speed), reverse=True)
        position, speed = map(list, zip(*sorted_pairs))
        times = [0]*(len(position))
        stack = []
        for i in range(len(position)):
            times[i] = (target - position[i]) / speed[i]
        for time in times:
            if stack != [] and time <= stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack)

