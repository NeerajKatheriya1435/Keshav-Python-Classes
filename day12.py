# for i in range(5):
#     for k in range(i+1):
#         print("*",end=" ")
#     print()
n=5
for i in range(n):
    for k in range(n-i-1):
        print(" ",end=" ")
    for l in range(i+1):
        print("*",end=" ")
    print()