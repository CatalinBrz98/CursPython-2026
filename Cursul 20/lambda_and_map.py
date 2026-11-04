if __name__ == "__main__":
    # mult_by_10 = lambda x: x * 10
    #
    nums = [1, 2, 3, 4, 5]
    # for num in nums:
    #     print(mult_by_10(num))
    #
    # make_full_name = lambda first, last: f'{first} {last}'
    # print(make_full_name('James', 'Smith'))
    #
    # get_sum_dif = lambda a, b: (a + b, a - b)
    # print(get_sum_dif(3, 4))

    for num in map(lambda x: x * 10, nums):
        print(num)
