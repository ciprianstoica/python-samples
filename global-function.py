def outer():
    global inner
    def inner():
        print("Inner function")

    print("Outer function")


outer()
inner()

