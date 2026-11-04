import time


def decorator_greeting_func(func):

    def wrapper(*args, **kwargs):
        print("Hello!")
        return func(*args, **kwargs)

    return wrapper

def timer_decorator(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Elapsed time: ", end - start)
        return result

    return wrapper

@timer_decorator
@decorator_greeting_func
def calc_sum(nums: list[float]) -> float:
    nums_sum = 0
    for num in nums:
        nums_sum += num

    return nums_sum

@timer_decorator
def hello_world():
    print("Hello World!")

if __name__ == '__main__':
    calc_sum([x for x in range(1000000)])
    hello_world()

    # print()
    #
    # x = decorator_greeting_func(calc_sum)
    # print(x([1, 2, 3, 4, 5]))