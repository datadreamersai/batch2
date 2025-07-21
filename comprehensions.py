
#squaring numbers using without list comprehension
l=[1,2,3,4,5]

squared_l =[]

def square(x):
    out = x**2
    return out

for i in l:
    out = square(i)
    squared_l.append(out)

print(squared_l)



#squaring numbers using  list comprehension

out = [i**2 for i in l]
print("using list comprehension:",out)



#filter even numbers using without list comprehension
l=[1,2,3,4,5]

even_l =[]

def even(x):
    if x%2==0:
        return x
    

for i in l:
    out = even(i)
    if out:
        even_l.append(out)

print("even numbers using without list comprehension:",even_l)


#filter even numbers using list comprehension

out = ["even" if i%2==0 else "odd" for i in l]

print("even numbers using list comprehension",out)


x=["xyz@gmail.com","iuo@yahoo.com","gjhgf@outlook.com","jhfkjg@outlook.com","dfhdig@yahoo.com"]

out = {i.split("@")[1] for i in x}
print("unique domains: ",out)
print("no of domains",len(out))



