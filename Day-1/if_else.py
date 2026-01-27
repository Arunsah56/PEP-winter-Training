def conditional_statement(a, b, c):
    if(a == b and b == c):
        print("A, B and C are equal.")
    elif(a > b and a > c):
        print("A is the greatest element.")
    elif(b > a and b > c):
        print("B is the greatest element.")
    else:
        print("C is the greatest element.")

def sum_of_num(num):
    sum = 0
    for i in range(1, num+1):
        sum += i
    return sum

if __name__ == "__main__":
    conditional_statement(90, 90, 90)
    sum = sum_of_num(89)
    print("The sum of num is:",sum)