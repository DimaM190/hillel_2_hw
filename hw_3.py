# 1. Рядки
# Напишіть функцію, яка приймає рядок і повертає його довжину.
def get_string_length(some_string: str) -> int:
    """Displays the length of a string"""
    str_len = len(some_string)
    return str_len


# Створіть функцію, яка приймає два рядки і повертає об'єднаний рядок.
def get_concatenate_string(first_string: str, second_string: str) -> str:
    """Combines two strings into one"""
    comb_str = f"{first_string} {second_string}"
    return comb_str


# 2. Числа (Int/float):
# Реалізуйте функцію, яка приймає число і повертає його квадрат.
def get_square_number(number: int | float) -> float:
    """Squares a number"""
    squ_num = number**2
    return squ_num


# Створіть функцію, яка приймає два числа і повертає їхню суму.
def get_sum_numbers(number_1: int | float, number_2: int | float) -> int | float:
    """Adds 2 numbers"""
    sum_num = number_1 + number_2
    return sum_num


# Створіть функцію яка приймає 2 числа типу int, виконує операцію ділення та повертає чілу частину і залишок.
def get_whole_remainder(dividend: int, divisor: int) -> tuple[int, int]:
    """Returns the integer part and the remainder of a division"""
    if divisor == 0:
        raise ValueError("The divisor is 0")
    if not type(dividend) == int or not type(divisor) == int:
        raise ValueError("The numbers entered are not integers")
    whole = dividend // divisor
    remainder = dividend % divisor
    return whole, remainder


# 3. Списки (Lists):
# Напишіть функцію для обчислення середнього значення списку чисел.
def get_average_value(number_list: list) -> float:
    """Calculates the average of numbers in a list"""
    len_list = len(number_list)
    sum_list = sum(number_list)
    result = sum_list / len_list
    return result


# Реалізуйте функцію, яка приймає два списки і повертає список, який містить спільні елементи обох списків.
def get_common_elements(list_1: list, list_2: list) -> list:
    """Returns the common elements of two lists."""
    result = list(set(list_1) & set(list_2))
    return result


# 4. Словники (Dictionaries):
# Створіть функцію, яка приймає словник і виводить всі ключі цього словника.
def get_keys_dict(dictionary: dict) -> list:
    """Returns a list of keys"""
    keys_list = list(dictionary.keys())
    return keys_list


# Реалізуйте функцію, яка приймає два словники і повертає новий словник, який є об'єднанням обох словників.
def get_common_dict(dict_1: dict, dict_2: dict) -> dict:
    """Combines two dictionaries"""
    dict_3 = dict_1 | dict_2
    return dict_3


# 5. Множини (Sets):
# Напишіть функцію, яка приймає дві множини і повертає їхнє об'єднання.
def get_common_set(set_1: set, set_2: set) -> set:
    """Combines two sets"""
    result = set_1 | set_2
    return result


# Створіть функцію, яка перевіряє, чи є одна множина підмножиною іншої.
def is_subset(set_1: set, set_2: set) -> bool:
    """Checks whether set 2 is included in set 1"""
    result = set_1.issubset(set_2)
    return result


# 6. Умовні вирази та цикли:
# Реалізуйте функцію, яка приймає число і виводить "Парне", якщо число парне, і "Непарне", якщо непарне.
def is_even_not_even(number: int) -> None:
    if not type(number) == int:
        raise ValueError("The numbers entered are not integers")
    if number % 2 == 0:
        print("Парне")
    else:
        print("Непарне")


# Створіть функцію, яка приймає список чисел і повертає новий список, що містить тільки парні числа.
def get_even_list(list_1: list) -> list:
    even_list = []
    for elm in list_1:
        if type(elm) == int and elm % 2 == 0:
            even_list.append(elm)
    return even_list


# 7. Написати лямбда-функцію визначальну парне/непарне.
is_event = lambda x: "Парне" if x % 2 == 0 else "Не парне"
