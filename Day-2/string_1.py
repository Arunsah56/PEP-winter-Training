def vowel_count(text):
    count = 0
    for ch in text:
        if ch in "aeiouAEIOU":
            count += 1
    return count

def word_count(text):
    word = text.split()
    print("Number of words: ",len(word)) # Method 1

    count = 0
    for i in word:
        count += 1
    return count  # method 2 

def con_break():
    for i in range(1, 10):
        if i == 5:
            continue
            print(i)
        if i >= 8:
            break
            print(i)
if __name__ == "__main__":
    print("Count of Vowel in Given Text is: ",vowel_count("python programming"))
    print("The count of word in this given sentence is: ",word_count("i am a good boy and i can not do any bad things"))
    con_break()