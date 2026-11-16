def process_params(*args, **kwargs):
    print(args)
    print(kwargs)

if __name__ == "__main__":
    # process_params(1,2,3,4,5,6,7,8,9,10)
    # process_params(a=1, b=2, c=3)
    process_params(1,2,3,4,5,6,7,8,9,10, a=1, b=2, c=3)