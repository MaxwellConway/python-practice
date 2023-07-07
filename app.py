# age = 20
# price = 19.95
# first_name = "Max"
# is_online = True
# print(age)

# name = input("What is your name? ")
# print("Hello " + name)

# birth_year = input("Enter your birth year: ")
# age = 2023 - int(birth_year)
# print(age)
# int()
# float()
# bool()
# str()

# First = 10.1
# Second = 20
# Sum = First + Second
# print(Sum)

# first = float(input("First: "))
# second = float(input("Second: "))
# sum = first + second
# print("Sum is " + str(sum))

# course = 'Python for Beginners'
# print('Python' in course)

# course = 'Python for Beginners'
# print(course.replace('for', '4'))

# x = 10
# x = x + 3
# x += 3
# x *= 3

# x = (10 + 3) * 2
# print(x)

# x = 3 > 2
# x = 3 >= 2
# x = 3 < 2
# x = 3 <= 2
# x = 3 == 2
# x = 3 != 2
# print(x)

# price = 25
# print(price > 10 and price < 30)
# print(price > 26 and price < 26)
# print(price > 26 or price < 26)

# price = 5
# print(not price > 4)
# print(not price > 10)

# temperature = 9
# if temperature > 30:
#     print("It's a hot day.")
#     print("Drink plenty of water.")
# elif temperature > 20:  # (20, 30]
#     print("It's a nice day.")
# elif temperature > 10:  # (10, 20]
#     print("It's a bit cold.")
# else:
#     print("It's cold.")
# print("Done")


# weight = int(input("Weight: "))
# unit = input("(K)g or (L)bs: ")
# if unit.upper() == "K":
#     print("Weight in Lbs: " + str(weight * 2.205))
# elif unit.upper() == "L":
#     print("Weight in Kgs: " + str(weight / 2.205))
# print("Done.")

# i = 1
# while i <= 10:
#     print(i * '*')
#     i = i + 1


# 1
# 1.1
# True
# 'a'

# names = ["John", "Bob", "Mary", "Chris", "Max"]
# names[0] = "Jon"
# print(names[0:3])
# print(names)

# numbers = [1, 2, 3, 4, 5]
# for item in numbers:
#     print(item)

# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i = i + 1

# for number in range(5):
#     print(number)

# def count_vowels(string):
#     counter = 0
#     for letter in string:
#         if letter in 'aeiou':
#             counter += 1
#     return counter


# result = count_vowels("The quick brown fox! Letter eeaaoo")
# print(result)

# def reverse_words(string):
#     words = string.split()
#     reversed_words = words[::-1]
#     reversed_sentence = " ".join(reversed_words)
#     return reversed_sentence


# result = reverse_words(
#     "I wonder what it means to be human. Will I ever truly live?")
# print(result)

# below requires import
# def is_palindrome(string):
#     string = string.lower()
#     string = string.replace(" ", "")
#     string = string.translate(str.maketrans("", "", string.punctuation))
#     reversed_string = string[::-1]
#     return reversed_string == string


# result = is_palindrome("Racecar")
# print(result)

# def is_anagram(string1, string2):
#     string1 = string1.replace(" ", "")
#     string2 = string2.replace(" ", "")
#     string1 = string1.lower()
#     string2 = string2.lower()

#     if len(string1) != len(string2):
#         return False
#     for letter in string1:
#         if letter in string2:
#             string2 = string2.replace(letter, "", 1)
#         else:
#             return False

#     return True

# result = is_anagram("listen", "SileNT")
# print(result)


# def calculate_average(array):
#     total = 0
#     for number in array:
#         total += number
#     length = len(array)
#     average = total/length
#     return average


# result = calculate_average([3, 3, 6])
# print(result)

input = "Hello my name is Maxwell"


def longest_even(string):
    longest_length = 0
    longest_word = ""

    words = string.split()
    for word in words:
        if len(word) % 2 == 0:
            if len(word) > longest_length:
                longest_length = len(word)
                longest_word = word

    return longest_word


result = longest_even(input)
print(result)
