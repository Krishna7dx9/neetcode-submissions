class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]):

        fleets = 1
        cars = []

        for i in range(len(position)):
            arrival_time = (target - position[i]) / speed[i]
            cars.append((position[i], arrival_time))

        cars.sort(key=lambda x: x[0], reverse=True)  # Sort by position descending

        for i in range(len(cars) - 1):
            if cars[i][1] >= cars[i + 1][1]:
                next_pos = cars[i + 1][0]
                cars[i + 1] = (next_pos, cars[i][1])
            else:
                fleets += 1 

        return fleets