def calculate_average(numbers):
    total = 0

    for i in range(len(numbers)):
        total += numbers[i]

    try:
        return total / len(numbers)
    except ZeroDivisionError:
        return None
data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = []

print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")

def get_list_element(my_list, index):
    try:
        if not isinstance(my_list, list):
            raise TypeError("my_list must be a list")

        return my_list[index]

    except IndexError:
        print("Error: The index is out of bounds.")
        return None

    except TypeError:
        print("Error: The input must be a list.")
        return None
print(get_list_element([10, 20, 30], 1))
print(get_list_element([10, 20, 30], 10))
print(get_list_element("hello", 1))
