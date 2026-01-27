# def series(num):
#     a, b = 0, 1
#     s = 0
#     for i in range(1, num+1):
#         print(a, end=" ")
#         s = a + b
#         a = b
#         b = s
        
    
# print("Enter the value of num:")
# num = int(input())
# (series(num))

def series(num):
    if num <= 1:
        return num
    else:
        return series(num-1) + series(num-2)
    
num = 10
for i in range(num):
    print(series(i), end=" ")