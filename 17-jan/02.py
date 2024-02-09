import sys

class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.north = None
        self.east = None
        self.south = None
        self.west = None

class Grid:
    def __init__(self, N, charging_point, gold_point):
        self.N = N
        self.grid = [[Room(x, y) for y in range(N)] for x in range(N)]
        self.charging_point = charging_point
        self.gold_point = gold_point
        self.build_grid()

    def build_grid(self):
        for x in range(self.N):
            for y in range(self.N):
                if x > 0:
                    self.grid[x][y].west = self.grid[x-1][y]
                if x < self.N - 1:
                    self.grid[x][y].east = self.grid[x+1][y]
                if y > 0:
                    self.grid[x][y].north = self.grid[x][y-1]
                if y < self.N - 1:
                    self.grid[x][y].south = self.grid[x][y+1]

    def is_valid_move(self, room):
        return not room.visited and room != self.charging_point and room != self.gold_point

class Agent:
    def __init__(self, N, X, charging_point, gold_point):
        self.N = N
        self.X = X
        self.current_room = charging_point
        self.current_room.visited = True
        self.time = 1
        self.moves = 0
        self.charging_point = charging_point
        self.gold_point = gold_point

    def move(self, direction):
        if direction == 'N':
            if self.current_room.north and self.is_valid_move(self.current_room.north):
                self.current_room = self.current_room.north
                self.moves += 1
                self.time += 1
                self.current_room.visited = True
        elif direction == 'E':
            if self.current_room.east and self.is_valid_move(self.current_room.east):
                self.current_room = self.current_room.east
                self.moves += 1
                self.time += 1
                self.current_room.visited = True
        elif direction == 'S':
            if self.current_room.south and self.is_valid_move(self.current_room.south):
                self.current_room = self.current_room.south
                self.moves += 1
                self.time += 1
                self.current_room.visited = True
        elif direction == 'W':
            if self.current_room.west and self.is_valid_move(self.current_room.west):
                self.current_room = self.current_room.west
                self.moves += 1
                self.time += 1
                self.current_room.visited = True

    def is_valid_move(self, room):
        return not room.visited and room != self.charging_point and room != self.gold_point

    def turn_left(self):
        if self.current_room.north:
            if self.is_valid_move(self.current_room.north):
                return 'N'
            else:
                return self.turn_left()
        elif self.current_room.west:
            if self.is_valid_move(self.current_room.west):
                return 'W'
            else:
                return self.turn_left()
        elif self.current_room.south:
            if self.is_valid_move(self.current_room.south):
                return 'S'
        else:
            return self.turn_left()

    def turn_right(self):
        if self.current_room.north:
            if self.is_valid_move(self.current_room.north):
                return 'N'
            else:
                return self.turn_right()
        elif self.current_room.east:
            if self.is_valid_move(self.current_room.east):
                return 'E'
            else:
                return self.turn_right()
        elif self.current_room.south:
            if self.is_valid_move(self.current_room.south):
                return 'S'
        else:
            return self.turn_right()

    def hit_wall(self):
        if self.current_room.north and self.is_valid_move(self.current_room.north):
            return 'N'
        elif self.current_room.east and self.is_valid_move(self.current_room.east):
            return 'E'
        elif self.current_room.south and self.is_valid_move(self.current_room.south):
            return 'S'
        elif self.current_room.west and self.is_valid_move(self.current_room.west):
            return 'W'
        else:
            return None

    def should_return(self):
        return self.moves >= self.X

    def explore(self):
        while not self.current_room == self.charging_point or not self.should_return():
            if self.current_room == self.gold_point:
                break
            if self.should_return():
                print(f'Total time taken: {self.time}')
                print(f'Decision to recharge taken at room ({self.current_room.x}, {self.current_room.y})')
                return
            direction = self.hit_wall()
            if direction:
                self.move(direction)
            else:
                if self.current_room.north and self.is_valid_move(self.current_room.north):
                    self.move('N')
                elif self.current_room.east and self.is_valid_move(self.current_room.east):
                    self.move('E')
                elif self.current_room.south and self.is_valid_move(self.current_room.south):
                    self.move('S')
                else:
                    self.move('W')

if __name__ == '__main__':
    N = int(sys.argv[1])
    X = int(sys.argv[2])
    charging_point = None
    gold_point = None
    for i in range(3, len(sys.argv), 2):
        if sys.argv[i] == 'C':
            charging_point = Room(int(sys.argv[i+1]), int(sys.argv[i+2]))
        elif sys.argv[i] == 'G':
            gold_point = Room(int(sys.argv[i+1]), int(sys.argv[i+2]))

    if not charging_point or not gold_point:
        print('Error: Charging point and gold point must be specified')
        sys.exit(1)

    grid = Grid(N, charging_point, gold_point)
    agent = Agent(N, X, charging_point, gold_point)
    agent.explore()