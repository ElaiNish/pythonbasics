def mystery(index):
    print("z" * len(index))

def remainder(base, divide_by=2, show_greeting=True):
    if show_greeting:
        print("Welcome to my function")
    print(base % divide_by)


def last_early(str1):
    str1 = str1.lower()
    last_char = str1[-1]
    if last_char in str1[:-1]:
        return True
    else:
        return False


def distance(num1, num2, num3):
    def is_close(a, b):
        return abs(a - b) == 1

    def is_far(a, b, c):
        return abs(a - b) >= 2 and abs(a - c) >= 2

    if is_close(num1, num2) and is_far(num3, num1, num2):
        return True
    elif is_close(num1, num3) and is_far(num2, num1, num3):
        return True
    else:
        return False


def filter_teens(a=13, b=13, c=13):
    a= fix_age(a)
    b= fix_age(b)
    c=fix_age(c)
    return a+b+c

def fix_age(age):
    if(age >=13 and age<=19 and age!=15 and age!=16):
        return 0
    return age

def chocolate_maker(small, big, x):
    """
    Create a line of chocolate cubes of length x using given small and large chocolate cubes.

    Args:
    small (int): the number of small chocolate cubes available, each 1 cm long
    big (int): the number of large chocolate cubes available, each 5 cm long
    x (int): the desired length of the chocolate line in cm

    Returns:
    bool: True if it is possible to create a line of length x using the given number of chocolate cubes, False otherwise
    """
    # Use up large chocolate cubes first
    while big != 0 and x >= 5:
        big -= 1
        x -= 5

    # Use up small chocolate cubes next
    while small != 0 and x > 0:
        small -= 1
        x -= 1

    # If x is zero, the chocolate line was successfully created
    return x == 0

def shift_left(my_list):
    return my_list[1:] + my_list[0]


def format_list(my_list):
    my_str = ", ".join(my_list[::2])
    my_str += " and " + my_list[-1]

    return my_str

def extend_list_x(list_x, list_y):
    list_x[:0] = list_y
    return list_x

def are_lists_equal(list1, list2):
    list1.sort()
    list2.sort()
    return list1==list2

def longest(my_list):
     return max(my_list, key=len)

def squared_numbers(start, stop):
    my_list = []
    num = start
    while num <= stop:
        my_list.append(num ** 2)
        num += 1
    return my_list

def is_greater(my_list, n):
    result = []
    for x in my_list:
        if x > n:
            result.append(x)
    return result

def numbers_letters_count(my_str):
    digits = sum(c.isdigit() for c in my_str)
    letters = sum(c.isalpha() for c in my_str)
    return [digits, letters]



def seven_boom(end_number):
    result = []
    for num in range(end_number+1):
        if num % 7 == 0 or '7' in str(num):
            result.append('BOOM')
        else:
            result.append(num)
    return result

def sequence_del(my_str):
    result = ''
    prev = None
    for x in my_str:
        if x != prev:
            result += x
            prev = x
    return result

# def print_products(products):
#     print("Products:", ", ".join(products))
#
# def print_num_products(products):
#     print("Number of products:", len(products))
#
# def check_product(products):
#     product = input("Enter product name: ")
#     if product in products:
#         print("The product is on the list.")
#     else:
#         print("The product is not on the list.")
#
# def count_product(products):
#     product = input("Enter product name: ")
#     count = products.count(product)
#     print(f"The product appears {count} times.")
#
# def delete_product(products):
#     product = input("Enter product name to delete: ")
#     if product in products:
#         products.remove(product)
#         print(f"{product} was removed from the list.")
#     else:
#         print(f"{product} is not on the list.")
#
# def add_product(products):
#     product = input("Enter product name to add: ")
#     products.append(product)
#     print(f"{product} was added to the list.")
#
# def print_invalid_products(products):
#     invalid_products = [p for p in products if len(p) < 3 or not p.isalpha()]
#     if invalid_products:
#         print("Invalid products:", ", ".join(invalid_products))
#     else:
#         print("No invalid products.")
#
# def remove_duplicates(products):
#     unique_products = list(set(products))
#     products.clear()
#     products.extend(unique_products)
#     print("Duplicates removed.")
#
# def main():
#     products_str = input("Enter a comma-separated list of products: ")
#     products = products_str.split(",")
#     print("Menu:")
#     print("1. Print products")
#     print("2. Print number of products")
#     print("3. Check if product is on the list")
#     print("4. Count how many times a product appears")
#     print("5. Delete a product from the list")
#     print("6. Add a product to the list")
#     print("7. Print invalid products")
#     print("8. Remove duplicates from the list")
#     print("9. Exit")
#
#     while True:
#         choice = int(input("Enter your choice (1-9): "))
#
#
#         if choice == 1:
#             print_products(products)
#         elif choice == 2:
#             print_num_products(products)
#         elif choice == 3:
#             check_product(products)
#         elif choice == 4:
#             count_product(products)
#         elif choice == 5:
#             delete_product(products)
#         elif choice == 6:
#             add_product(products)
#         elif choice == 7:
#             print_invalid_products(products)
#         elif choice == 8:
#             remove_duplicates(products)
#         elif choice == 9:
#             print("Exiting...")
#             break
#         else:
#             print("Invalid choice.")

def arrow(my_char, max_length):
    lines = []
    for i in range(1, max_length+1):
        line = my_char * i
        lines.append(line)
    for i in range(max_length-1, 0, -1):
        line = my_char * i
        lines.append(line)
    return '\n'.join(lines)

# def get_price(item):
#     return float(item[1])
#
# def sort_prices(list_of_tuples):
#     return sorted(list_of_tuples, key=get_price, reverse=True)

def mult_tuple(tuple1, tuple2):
    result = ()
    for i in tuple1:
        for j in tuple2:
            result += ((i,j), (j,i))
    return result

def sort_anagrams(list_of_strings):
    anagram_list = []
    for string in list_of_strings:
        found_group = False
        for group in anagram_list:
            if sorted(group[0]) == sorted(string):
                group.append(string)
                found_group = True
                break
        if not found_group:
            anagram_list.append([string])
    return anagram_list

def count_chars(my_str):
    result_dict = {}
    for char in my_str:
        if char != " ":
            if char in result_dict:
                result_dict[char] += 1
            else:
                result_dict[char] = 1
    return result_dict

def inverse_dict(my_dict):
    new_dict = {}
    for key, value in my_dict.items():
        if value not in new_dict:
            new_dict[value] = [key]
        else:
            new_dict[value].append(key)
    for key in new_dict:
        new_dict[key].sort()
    return new_dict

def are_files_equal(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        return f1.read() == f2.read()

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def sort_words(lines):
    words = set()
    for line in lines:
        words.update(line.split())
    return sorted(words)

def reverse_lines(lines):
    return [line[::-1] for line in lines]

def print_last_lines(lines, n):
    for line in lines[-n:]:
        print(line)

file_path = input("Enter a file path: ")
task = input("Enter a task: ")

lines = read_file(file_path)

if task == 'sort':
    words = sort_words(lines)
    print(words)
elif task == 'rev':
    reversed_lines = reverse_lines(lines)
    for line in reversed_lines:
        print(line)
elif task == 'last':
    n = int(input("Enter a number: "))
    print_last_lines(lines, n)
else:
    print("Unknown task")




def copy_file_content(source, destination):
    with open(source, 'r') as file1, open(destination, 'w') as file2:
        content = file1.read()
        file2.write(content)

def who_is_missing(file_name):
    with open(file_name) as file:
        numbers = file.read().strip().split(',')
        numbers = [int(num) for num in numbers]
        n = len(numbers) + 1
        full_sum = sum(range(1, n))
        actual_sum = sum(numbers)
        missing_num = full_sum - actual_sum
        with open('found.txt', 'w') as found_file:
            found_file.write(str(missing_num))
        return missing_num

def my_mp3_playlist(file_path):
    with open(file_path, "r") as file1:
        longest_song_name = ""
        longest_song_length = 0
        num_songs = 0
        operations = {}
        for line in file1:
            song_data = line.strip().split("; ")
            song_name, performer, song_length = song_data
            minutes, seconds = song_length.split(":")
            song_length_sec = int(minutes) * 60 + int(seconds)
            if song_length_sec > longest_song_length:
                longest_song_name = song_name
                longest_song_length = song_length_sec
            num_songs += 1
            if performer in operations:
                operations[performer] += 1
            else:
                operations[performer] = 1
        most_frequent_operation = max(operations, key=operations.get)
        return (longest_song_name, num_songs, most_frequent_operation)


def my_mp4_playlist(file_path, new_song):
    with open(file_path, "r") as file1:
        lines = file1.readlines()

    while len(lines) < 3:
        lines.append("\n")

    lines[2] = f"{new_song};Unknown;4:15;\n"

    with open(file_path, "w") as file1:
        file1.writelines(lines)

    with open(file_path, "r") as file1:
        print(file1.read())


if __name__ == '__main__':
    fairy_tale = "The Ugly Duckling"
    # swan_height = 90.7
    # eggs_num = 4
    # surprise = bool(eggs_num)
    # print(str(surprise))
    # func = mystery
    # func("python")
    # remainder(9)
    # print(filter_teens(2, 1, 15))
    # print(chocolate_maker(3, 2, 10))
    # x=[3,4]
    # y=[1,2]
    # print(extend_list_x(x,y))
    # list1 = [0.6, 1, 2, 3]
    # list2 = [3, 2, 0.6, 1]
    # list3 = [9, 0, 5, 10.5]
    # print(are_lists_equal(list1,list3))
    # list1 = ["111", "234", "2000", "goru", "birthday", "09"]
    # print(longest(list1))

    # print(seven_boom(17))
    # print( sequence_del("ppyyyyythhhhhooonnnnn"))

    # magic_str = "abra cadabra"
    # print( count_chars(magic_str))
    # course_dict = {'elai': 10, 'nishri': 10, 'liam': 0}
    # result = inverse_dict(course_dict)
    # print(result)

    # data = ("self", "py", 1.543)
    # format_string = "Hello {}.{} learner, you have only {:.1f} units left before you master the course!"
    #
    # print(format_string.format(*data))
    #
    # products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    # sorted_products = sort_prices(products)
    # print(sorted_products)

    # first_tuple = (1, 2)
    # second_tuple = (4, 5)
    # print(mult_tuple(first_tuple, second_tuple))

    # elai = {
    #     "first_name": "Elai",
    #     "last_name": "Nishri",
    #     "birth_date": "14.03.2004",
    #     "hobbies": ["Reading", "Running", "gym"]
    # }
    # selection = int(input("Enter a number between 1 and 7: "))
    #
    # if selection == 1:
    #     print(elai['last_name'])
    # elif selection == 2:
    #     birth_month = elai['birth_date'][3:5]
    #     print(birth_month)
    # elif selection == 3:
    #     num_hobbies = len(elai['hobbies'])
    #     print(num_hobbies)
    # elif selection == 4:
    #     last_hobby = elai['hobbies'][-1]
    #     print(last_hobby)
    # elif selection == 5:
    #     elai['hobbies'].append('Cooking')
    #     print(elai['hobbies'])
    # elif selection == 6:
    #     birth_date = elai['birth_date'].split('.')
    #     birth_tuple = tuple(int(d) for d in birth_date)
    #     print(birth_tuple)
    # elif selection == 7:
    #     birth_year = int(elai['birth_date'][-4:])
    #     age = 2023 - birth_year
    #     elai['age'] = age
    #     print(elai)

# bricks = int(input("Enter the number of bricks collected by each pig (three-digit number): "))
# total_bricks = bricks // 100 + (bricks // 10) % 10 + bricks % 10
# pig_bricks = total_bricks // 3
# what_left = total_bricks % 3
# print("Total number of bricks collected:", total_bricks)
# print("Number of bricks for each pig:", pig_bricks)
# print("what left of the distribution:", what_left)
# print("Sum is divided without remainder:", (what_left == 0))
# print("He" + "l" * 2 + "o" + " Python " + str(7.2 / 2) + "." + str(3))
# print('"Shuffle, Shuffle, Shuffle", say it together!\nChange colors and directions,\nDon\'t back down and stop the player!\n\t Do you want to play Taki?\n\t Press y\\n')
numbers = "123456789"
print(numbers[-1:-10])
# string = input("enter string: ")
# first_char = string[0]
# new_string = first_char + string[1:].replace(first_char, 'e')
# print(new_string)
# string = input("Please enter a string: ")
# mid = len(string) // 2
# new_string = string[:mid].lower() + string[mid:].upper()
# print(new_string)
# string = input("Enter a string: ")
# string = string.replace(" ", "").lower()
# if string == string[::-1]:
#     print("OK")
# else:
#     print("NOT")

# str = input("Insert the temperature: ")
# val = float(str[:-1])
# unit = str[-1].upper()
# if unit == 'C':
#     temp_conv = (9/5) * val + 32
#     new_unit = 'F'
# elif unit == 'F':
#     temp_conv = (5/9) * (val - 32)
#     new_unit = 'C'
# else:
#     print("Invalid temperature unit entered!")
#     exit()
#
# print(temp_conv,new_unit)

# import calendar
# date_string = input("Enter a date (dd/mm/yyyy): ")
# day, month, year = map(int, date_string.split('/'))
# day_of_week = calendar.weekday(year, month, day)
# day_string = calendar.day_name[day_of_week]
# print(day_string)
