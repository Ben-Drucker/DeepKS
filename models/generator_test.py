def gen_func(x):
    print("preparing x...")
    for i in range(x):
        yield i

def main_func(y):
    print("preparing y...")
    for _ in range(y):
        gen_func(2)

main_func(10)