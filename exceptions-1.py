try:
    l = ['a', 'b']
    print(l[1])
    print(l[4])
    print("Try block done")
except IndexError as e:
    print("Exception caught!", type(e), e)
else:
    print("No exception caught!")
finally:
    print("Finally done!")

print("Finish")
