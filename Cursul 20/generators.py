def my_range_func(end: float, start: float=0, step: float=1):
    my_list = []
    while start < end:
        my_list.append(start)
        start += step
    return my_list

def my_range_gen(end: float, start: float=0, step: float=1):
    while start < end:
        yield start
        start += step

def my_generator():
    yield 1

    for i in range(10, 12):
        yield i

    yield "Salut!"

if __name__ == '__main__':
    # result = my_range_func(400)
    # print(my_range(10000000000))
    # print(my_range(start=10, end=100, step=7))
    # print(result)
    # result2 = my_range_gen(10000000000)
    # print(result2)
    # for num in result2:
    #     if num % 1000 == 0:
    #         print(num)

    # gen = my_generator()
    #
    # try:
    #     print(next(gen))
    #     print(next(gen))
    #     print(next(gen))
    #     print(next(gen))
    #     print(next(gen))
    #     print(next(gen))
    # except StopIteration:
    #     print("StopIteration")
    values = (x ** 2 for x in range(99999999999) if x % 2 == 0)
    for value in values:
        print(value)
