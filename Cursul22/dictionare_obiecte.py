import random
import sys

class Vector2D:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def display_info(self):
        print(self.x, self.y)

def display_vect_info(self_dict: dict):
    print(self_dict['x'], self_dict['y'])

if __name__ == "__main__":
    vector2D = Vector2D(2, 3)
    vector2D_dict = {"x": 2, "y": 3, "display_info": display_vect_info}

    vector2D.display_info()
    vector2D_dict["display_info"](vector2D_dict)

    # vector2D_list = []
    # vector2D_dict_list = []
    #
    # n = 1000000
    #
    # for _ in range(n):
    #     x = random.randint(0, 1000)
    #     y = random.randint(0, 1000)
    #     vector2D_list.append(Vector2D(x, y))
    #     vector2D_dict_list.append({"x": x, "y": y})
    #
    # print(sys.getsizeof(vector2D_list))
    # print(sys.getsizeof(vector2D_dict_list))
