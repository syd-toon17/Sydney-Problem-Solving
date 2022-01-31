#problem solving steps
    #a.	Go to computer
    #b.	Open vs code
    #c.	Create new python file
    #d.	Write code that takes in string
    #e.	Open search engine
            #i.	Google ”how to ~insert problem here~ python”
            #ii. Find best example that works for you
    # f.Test results in vs code
            # i. Write code that research returned
            # ii. Print to console
            # iii. Debug (if necessary)
            # iv. Test code
    # v.Save

#Reverse a string
def reverse_string():
    txt = input('Type a word or two!: ') [::-1]
    print(txt)
reverse_string()

#capitalize letter
def capitalize_every_word():
    words = input('type some words!: ')
    some_words = words.title()
    print(some_words)
capitalize_every_word()
    

# #compress a string of characters
string = input('please input string you would like compressed: ')
def compress(string):
    index = 0
    compressed = ''
    len_str = len(string)
    while index != len_str:
        count = 1
        while (index < len_str-1) and (string[index] == string[index+1]):
            count = count + 1
            index = index +1
        if count ==1:
            compressed += str(string[index])
        else:
            compressed += str(string[index]) + str(count)
        index = index + 1
    return compressed
print(compress(string))

#BONUS Palindrome







