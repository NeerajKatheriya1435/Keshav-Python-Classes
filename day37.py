
import time

# Current time in seconds

# print("Epoch time:", time.time())

# start1=time.time() # 30
# for i in range(2000000):
#     a=8
#     b=9
#     a+b
# end1=time.time() # 40


# i=0
# start2=time.time() # 30
# while(i<2000000):
#     a=8
#     b=9
#     a+b
#     i+=2
# end2=time.time() # 40

# print(end1-start1)
# print(end2-start2)

# print(time.time())
# print(time.localtime())
# str1=time.localtime()

# Local time
# local = time.localtime()

# print("Local time tuple:", local)
# print("Formatted:", time.strftime("%Y-%B-%d %H:%M:%S %p", local))

time_str = "2025-07-16 11:00:00"
parsed = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
print("Parsed time tuple:", parsed)
# print(time_str)
time.sleep(2)
print("hello")