# import random

# # for i in range(3):
# #     print(random.randint(3, 15))
# class Dice:
#     def roll(self):
#         first = random.randint(1,6)
#         second = random.randint(1,6)
#         return first, second
    

# dice = Dice()
# print(dice.roll())

# from pathlib import Path

# path = Path()
# for file in path.glob("*"):
#     print(file)

# Caculating Area of a rectangle
# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter width of the rectangle: "))
# area_of_rectangle = length * width
# print(area_of_rectangle)

# temperature = float(input("Enter the temperature of the room: "))
# convertion_rate = input("(C)elcius or (F)areiheit: ").upper()

# if convertion_rate == "C":
#     fahrenheit = (temperature * 9/5) + 32
#     print(fahrenheit)
# elif convertion_rate == "F":
#     celcius = (temperature - 32) * 5/9
#     print(celcius)
# else:
#     print("wrong unit")

# number_of_vowels = 0
# vowels = set("aeiouAEIOU")
# sentence = input("Enter a sentence:\n")
# for vowel in sentence: 
#     if vowel in vowels:
#         number_of_vowels+=1
# print(number_of_vowels)

# print("Welcome to Python!")
# name = "Prince"
# age = 25
# likes_programming = True
# print(name)
# print(age)
# print(likes_programming)
# print(f"{name} is {age} years old")

# student={
#     "name": "Alice",
#     "age": 22,
#     "major": "Computer Science"
# }
# student["graduation year"] = 2024
# del student["age"]
# print(student.get("name"))
# print(student)

# favourite_movies = {
#     "1":"Far from Home",
#     "2": "Hercules",
#     "3": "Black in beauty"
# }
# print(favourite_movies["1"])
# print(favourite_movies["3"])
# favourite_movies["4"] = "Ananse in the land of idiots"
# favourite_movies["5"] = "The wretched"
# print(favourite_movies)

# favourite_movie_details ={
#     "Title": "Far from Home",
#     "Director": "Sonia Uche",
#     "Year": 2024
# }
# print(favourite_movie_details)


# favorite_movies = ["Far from Home", "Hercules", "Black in Beauty"]
# print(favorite_movies[0])
# print(favorite_movies[2])
# favorite_movies.append("Ananse in the land of idiots")
# for num, movie in enumerate(favorite_movies, start=1):
#     print(f"{num}. {movie}")

# favourite_movie_details ={
#     "Title": "Far from Home",
#     "Director": "Sonia Uche",
#     "Year": 2024
# }
# print(favourite_movie_details)

# number = float(input("Enter any number, negative or positive"))
# if number > 0:
#     print(f"{number} is positive")
# elif number == 0:
#     print(f"{number} is zero")
# elif number < 0:
#     print(f"{number} is negative")
# else:
#     print("Type a number!")

# for i in range(1,11):
#     print(i)

# count = 1
# while count <= 10:
#     print(count)
#     count+=1
    
# def greet(name):
#     print(f"Hello {name}")
# greet("Prince")
    
# def number_square(number):
#     return number**2
# answer = number_square(int(input("Enter any number: ")))
# print(answer)

# def print_fruits(fruits):
#     for idx, fruit in enumerate(fruits, start=1):
#         print(f"{idx}.{fruit}")

# fruits = ["wallock", "apple", "strawberry"]
# print_fruits(fruits)



# def get_even_numbers(numbers):
#     even_numbers = []
#     for num in numbers:
#         if num % 2 == 0:
#             even_numbers.append(num)
#     return even_numbers

# numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(get_even_numbers(numbers_list))



# def calculate_average(numbers):
#     return sum(numbers)/len(numbers)


# numbers_list = [2, 4, 3, 6, 5, 7, 0, 8]
# print(calculate_average(numbers_list))

# def get_odd_numbers(numbers):
#     odd_numbers = []
#     for num in numbers:
#         if num % 2 == 1:
#             odd_numbers.append(num)
#     return odd_numbers


# numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(get_odd_numbers(numbers_list))

# def add_numbers(num1, num2):
#     return num1 + num2

# answer = add_numbers(int(input("Enter 1stnumber: ")),int(input("Enter a number: ")))
# print(answer)





def get_even_numbers(numbers):
    even_numbers= []
    for num in numbers:
        if num % 2== 0:
            even_numbers.append(num)
    return even_numbers

number_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even=get_even_numbers(number_list)
print(even)


def get_odd_numbers(numbers):
    odd_numbers =[]
    for num in numbers:
        if num % 2 ==1:
            odd_numbers.append(num)
    return odd_numbers

numbers = [10, 21, 33, 46, 60, 75, 91, 108, 126, 135]
oddnumbers = get_odd_numbers(numbers)
print(oddnumbers)





def get_vowels(alphabets):
    vowels = []
    for alphabet in alphabets:
        if alphabet in set("aeiouAEIOU"):
            vowels.append(alphabet)
    return vowels

alphabets = ["a","b","c","d","e","f","g","h","i","j","k","z","t","o"]
vowel = get_vowels(alphabets)
for idx, item in enumerate(vowel, start=1):
    print(f"{idx}.{item}")


def get_consonant(alphabets):
    consonants = []
    for alphabet in alphabets:
        if alphabet not in set("aeiouAEIOU"):
            consonants.append(alphabet)
    return consonants

alphabets = ["a","b","c","d","e","f","g","h","i","J","k","z","t","o"]
consonant = get_consonant(alphabets)
print(consonant)