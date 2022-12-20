def gen(x):
    for i in range(x):
        yield i**2
    if x == 0:
        print("x is 0")
    else:
        print("x is not 0")

def main():
    for x in gen(10):
        print("Val is", x)

main()