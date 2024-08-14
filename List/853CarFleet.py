class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pairing positions and speeds and sorting them based on position
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        slowest_time = 0

        for pos, spd in cars:
            # Calculate time to reach the destination
            time = (target - pos) / spd
            # If the time is greater than the slowest time, this car forms a new fleet
            if time > slowest_time:
                fleets += 1
                slowest_time = time

        return fleets
