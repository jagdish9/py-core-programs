def logger(funcv):
    def wrapper():
        print("Before function")
        funcv()
        print("After function")
    return wrapper

@logger
def hello():
    print("hello")

def main():
    hello()

if __name__ == '__main__':
    main()

#Used for:
#   logging
#   authentication
#   timing
#   caching