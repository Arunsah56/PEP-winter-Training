def odd_even(num):
    if num % 2 == 0:
        return "EVEN"
    else:
        return "ODD"
    
def pos_neg(num):
    if num > 0:
        return "True"
    else:
        return "False"


def main(num):
    print("The number is: ",odd_even(num))
    print("Number is Positive: ", pos_neg(num))

if __name__ == "__main__":
    main(-8)