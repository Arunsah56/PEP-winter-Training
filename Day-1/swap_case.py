def swap_case(s):
    t = ''
    for i in s:
        if i.islower():
            t += i.upper()
        else:
            t += i.lower()
    return t
if __name__ == "__main__":
    print(swap_case('Arun0'))