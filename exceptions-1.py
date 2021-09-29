try:
    list = ['a', 'b']
    print(list[1])
    print(list[4])
    print("Try block done")
except IndexError as e:
    print("Exception caught!", type(e), e)
else:
    print("No exception caught!")
finally:
    print("Finally done!")

print("Finish")
