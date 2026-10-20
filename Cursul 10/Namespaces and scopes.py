# x = "x global"
#
# def test():
#     x = "x local"
#     print(x)
#
# test()

# x = "x global"
# y = "y global"
# my_list = [1,2,3,4,5,6]
#
# def test():
#     my_list.append(7)
#     print(my_list)
#
# test()
# print(my_list)

# import builtins
#
# print(dir(builtins))

# x = "x global"
#
# def test1():
#     x = "x outer"
#     print(f"Exemplu 1: {x}")
#
#     def test2():
#         x = "x inner"
#         print(f"Exemplu 2: {x}")
#
#     test2()
#     print(f"Exemplu 3: {x}")
#     return test2
#
# my_test_func = test1()
# print(f"Exemplu 4: {x}")
#
# my_test_func()

# def mult_by_2(n):
#     return n*2
#
# def mult_by_3(n):
#     return n*3
#
# def mult_by_10(n):
#     return n*10
#
# def mult_by_100(n):
#     return n*100
#
# for i in [1, 10, 15, 20, 3]:
#     print(mult_by_2(i), mult_by_3(i), mult_by_10(i), mult_by_100(i))

# def mult_by_x(n, x):
#     return n*x
#
# for i in [1, 10, 15, 20, 3]:
#     print(mult_by_x(i, 2), mult_by_x(i, 3), mult_by_x(i, 10), mult_by_x(i, 100))

def make_mult_by_x(x):

    def mult_by_x(n):
        return n * x

    return mult_by_x

mult_by_2 = make_mult_by_x(2)
mult_by_3 = make_mult_by_x(3)
mult_by_10 = make_mult_by_x(10)
mult_by_100 = make_mult_by_x(100)

for i in [1, 10, 15, 20, 3]:
    print(mult_by_2(i), mult_by_3(i), mult_by_10(i), mult_by_100(i))