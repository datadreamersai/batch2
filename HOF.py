
# out = lambda x:x**0.5
# print(out(25))



#map


def square(x):
    return x**2




# map_out = map(lambda x:x**2,range(1,11))

# for i in map_out:
#     print(i)



# map_out = list(map(lambda x,y:x*y,range(1,5)))

# print(map_out)



# filter(function,iterable)

# filter_out = list(filter(lambda x:x>0,range(1,5)))

# print(filter_out)



# from functools import reduce

# reduce_out = reduce(lambda x,y:x*y,range(1,6))
# print(reduce_out)






logs = [
    "2025-01-27 10:15:30 0.2 ERROR 500 Internal Server Error",
    "2025-01-27 10:16:10 0.3 ERROR 404 Not Found",
    "2025-01-27 10:17:45 0.5 ERROR 503 Service Unavailable",
    "2025-01-27 10:18:00 0.7 INFO 200 Service Started"
]



# def error_exractor(x):
#     out = x.split(" ")[5:]
#     out = " ".join(out)
#     return out


print(list(map(lambda x:" ".join(x.split(" ")[5:]),logs)))


# print(list(map(error_exractor,logs)))

# s="2025-01-27 10:15:30 0.2 ERROR 500 Internal Server Error"
# l = s.split(" ")
# sliced_l = l[5:]
# out = " ".join(sliced_l)
# print(out)


# print(" ".join(s.split(" ")[5:]))
