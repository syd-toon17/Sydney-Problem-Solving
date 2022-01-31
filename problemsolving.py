#Reverse a string
# def reverse_string():
#         word = 'mickey'
#         reversed_word = ''
#         for index in range(len(word) -1, -1, -1):
#                 reversed_word += word[index]
#         print(reversed_word)
# reverse_string()

#capitalize letter
# def capitalize_every_word():
#         words = input('type some words!: ')
#         last_character = " "
#         new_string = ""
#         for character in words:
#                 if last_character == " ":
#                         new_string += character.upper()
#                         last_character = character
#                 elif last_character != " ":
#                         new_string += character
#                         last_character = character
#         return new_string
        


# result = capitalize_every_word()
# print(result)

# #compress a string of charactersJ
# string = input('please input string you would like compressed: ')
# def compress(string):
#     index = 0
#     compressed = ''
#     len_str = len(string)
#     while index != len_str:
#         count = 1
#         while (index < len_str-1) and (string[index] == string[index+1]):
#             count = count + 1
#             index = index +1
#         if count ==1:
#             compressed += str(string[index])
#         else:
#             compressed += str(string[index]) + str(count)
#         index = index + 1
#     return compressed
# print(compress(string))

# # #BONUS Palindrome
# def palindrome():
#         test_word = 'madam'
#         if test_word == test_word [::-1]:
#                 print('you found one!')
#         else:
#                 print('that is not one :(')
# palindrome()




def compress_a_string(string):
        new_string = ""
        current_count = 0
        last_character = string[0]
        for character in string:
                if character == last_character:
                        current_count += 1
                else:
                        new_string += str(current_count) + last_character
                        current_count = 1
                        last_character = character
        new_string += str(current_count) + last_character
        print(new_string)
compress_a_string("aaaabbbbccccdddd")