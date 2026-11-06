




class Answer:
    class Map:
        N_vertical: int
        M_horizontal: int
        mapping: list[list[str]]
        def __init__(self) -> None:
            self.N_vertical, self.M_horizontal = map(int, input().split())
            self.mapping = []
            for _ in range(self.N_vertical):
                self.mapping.append(list(list(input())))
        
        def print_map(self) -> None:
            for i in range(self.N_vertical):
                for j in range(self.M_horizontal):
                    print(self.mapping[i][j], end=' ')
                print()

        def get_cord_X(self) -> list[int]:
            for i in range(self.N_vertical):
                for j in range(self.M_horizontal):
                    if self.mapping[i][j] == 'X':
                        return [i, j]
                    
        def create_rase_Down_Right(self, x: int, y: int) -> None:
            Answer.Map.mapping[x][y] = '\\'
        
        def create_rase_Up_Right(self, x: int, y: int) -> None:
            Answer.Map.mapping[x][y] = "/"
        
        def create_rase_Up_Left(self, x: int, y: int) -> None:
            Answer.Map.mapping[x][y] = '\\'
        
        def create_rase_Down_Left(self, x: int, y: int) -> None:
            Answer.Map.mapping[x][y] = "/"
                    
        def create_rase(self):
            rays = []
            x, y = self.get_cord_X()
            if self.check_field(x - 1, y - 1):
                rays.append(Answer.Ray(x - 1, y - 1, 'Up_Left'))
                Answer.Map.create_rase_Up_Left(self, x - 1, y - 1)
            if self.check_field(x - 1, y + 1):
                rays.append(Answer.Ray(x - 1, y + 1, 'Up_Right'))
                Answer.Map.create_rase_Up_Right(self, x - 1, y + 1)
            if self.check_field(x + 1, y - 1):
                rays.append(Answer.Ray(x + 1, y - 1, 'Down_Left'))
                Answer.Map.create_rase_Down_Left(self, x + 1, y - 1)
            if self.check_field(x + 1, y + 1):
                rays.append(Answer.Ray(x + 1, y + 1, 'Down_Right'))
                Answer.Map.create_rase_Down_Right(self, x + 1, y + 1)
        def get_status_cord(self, x: int, y: int) -> str:
            return self.mapping[x][y]

        def check_field(self, x: int, y: int) -> bool:
            if x < 0 or x >= self.N_vertical or y < 0 or y >= self.M_horizontal or self.mapping[x][y] == '*':
                return False
            return True
    
    class Ray:
        x: int
        y: int
        direction: str

        def __init__(self, x: int, y: int, direction: str) -> None:
            self.x, self.y, self.direction = x, y, direction
            self.x = int(self.x)
            self.y = int(self.y)








m = Answer.Map()
m.create_rase()
m.print_map()

