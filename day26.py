

# f1=open("sample.txt","rb")

# f1=open("sample.txt","w")

# f1=open("sample.txt","a")

# print(f1.read())

# f1.close()

# print(f1.read())

# f1.write("My content by keshav\n")
# f1.write("Dobara maine kuch type kiya\n")

# with open("sample.txt","r") as f:
#     print(f.read())

# f1=open("sample.txt","r")

# print(f1.readline())
# print(f1.readline())
# print(f1.readline())

# f1=open("sample.txt","r")

# while True:
#     line=f1.readline()
#     if not line:
#         break
#     print(line)

# f1=open("abhinay.txt","w")

# userInpu1=input("Enter the first line conetent: ")
# userInpu2=input("Enter the second line conetent: ")
# userInpu3=input("Enter the third line conetent: ")

# list1=[userInpu1+"\n",userInpu2+"\n",userInpu3+"\n"]
# list1=[userInpu1,userInpu2,userInpu3]

# for item in list1:
#     f1.write(item+"\n")

# f1.close()

# f1=open("sample.txt","r")

# print(len(f1.readline()))

# f1.seek(15)
# print(f1.readline())

# print(f1.tell())

f1=open("sample1.txt","w")
f1.write("My name is abhinay")
f1.truncate(5)