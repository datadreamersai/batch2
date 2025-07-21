
# count=15 #Global variable


# def greet():
#     message = "Hello!"  # Local variable
#     print(message)
#     global count
#     count=count+1
#     return count

# print(greet())


# def greet1():
#     print(count)


# greet1()






# def func1():
#     print("Hi")
#     z=3.14
#     z=z+1
#     def func2():
#         print("I am good")
#         nonlocal z
#         z=z+1
#         print(z)

#     func2()
    
# func1()



# def greet():
#     print("hello")

# print(type(greet))

# print(id(greet))

# x=greet
# x()


# l=[1,2,3,4,greet]
# l[-1]()

# del greet

# print(id(greet))




# def square(x):
#     return x**2


# def operation():
#     print("I am operating function")
#     return square


# out = operation()
# square_out = out(5)
# print(square_out)







def square(x):
    return x**2


def operation(z,x):
    print("I am operating function")
    out = z(x)
    return out


out = operation(square,5)
print(out)


