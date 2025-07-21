# try:
#     file = open(r"E:\sample\abc.txt","r")
#     print(file.read())
#     file.close()
# except Exception as e:
#     print("File was not found at",e)
#     file = open(r"D:\sample\abc.txt","r")
#     print(file.read())
#     file.close()




# try:
#     file=open(r"D:\sample\abc.txt","r")
#     file_content = file.read()
#     file_content = int(file_content)
#     d={"a":2,"b":3}
#     print(d["b"])
#     a= 10/0
#     print(x)


# except FileNotFoundError as e:
#     print("Please provide alternative path bcz of the error",e)

# except ValueError as e:
#     print("Arey bhai please enter only integer into txt file bcz of the error",e)



# except Exception as e:
#     print(e)







##try except else

try:
    file = open(r"D:\sample\ac.txt","r")
except FileNotFoundError as e:
    print("Error due to",e)

else:
    output = file.read()
    #transformation code

    file.close()



try:
    pass
except:
    pass

try:
    pass
except:
    pass
else:
    pass


try:
    pass
except:
    pass
finally:
    pass

try:
    pass
except:
    pass
else:
    pass
finally:
    pass