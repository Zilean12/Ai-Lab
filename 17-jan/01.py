import random

class Agent:
    def __init__(self, size, storage,  ReCharging_place, Sone_locat):
        self.size = size
        self.storage = storage
        self.Point = (0, 0)
        self.ReCharging_place = ReCharging_place
        self.Sone_locat = Sone_locat
        self.visited_rooms = set()
        self.path = []
        self. storage_capacity = storage

    def move(self, disha):
        x, y = self.Point
        if disha == "aage":
            x += 1
        elif disha == "peeche":
            x -= 1
        elif disha == "daayein":
            y += 1
        elif disha == "baayein":
            y -= 1

        if 0 <= x < self.size and 0 <= y < self.size:
            self.Point = (x, y)
            self.path.append(self.Point)
            self.visited_rooms.add(self.Point)
            self.storage -= 1

            if self.Point == self.Sone_locat:
                print("Sone ki khoj mili!  Total time taken:", len(self.path))
                return True

            if self.Point == self.ReCharging_place and self.storage < self. storage_capacity:
                print(f"Charging at {self.Point}. Total time taken:", len(self.path))
                return True

        else:
            self.turn(disha)

    def turn(self, disha):
        if disha == "aage":
            self.move("peeche")
        elif disha == "peeche":
            self.move("aage")
        elif disha == "daayein":
            self.move("baayein")
        elif disha == "baayein":
            self.move("daayein")

    def explore(self):
        charging_decision = None
        while self.storage > 0:
            if self.move_randomly():
                return

        charging_decision = self.Point if self.storage <= 0 else None
        print("Low battery; heading back to the charging station..", charging_decision)
        print("Total time taken:", len(self.path))

    def move_randomly(self):
        possible_moves = ["aage", "peeche", "daayein", "baayein"]
        random.shuffle(possible_moves)

        for move in possible_moves:
            if self.move(move):
                return True  # Stop exploration if gold found or charging needed
        return False

while True:
    Size_of_Grid = int(input("Specify the size of the grid.: "))
    storage_capacity = int(input("Please input the battery capacity: "))
    recharging_Station = tuple(map(int, input("Provide the coordinates for the charging station (x y): ").split()))
    Sone_locat = tuple(map(int, input("Input the coordinates for the gold location (x y): ").split()))

    agent = Agent(Size_of_Grid,  storage_capacity, recharging_Station, Sone_locat)
    agent.explore()

    play_again = input("Would you like to initiate the simulation again? (yes/no)")
    if play_again.lower() != "yes":
        break
