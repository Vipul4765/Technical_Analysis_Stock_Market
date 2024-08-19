class SumDigitsClass1:
    def __init__(self, data):
        self.n = data

    def process(self):
        result = sum(int(digit) for digit in str(self.n))
        return result


class SumDigitsClass2:
    def __init__(self, data):
        self.n = data

    def process(self):
        result = sum(int(digit) for digit in str(self.n))
        return result


class SumDigitsClass3:
    def __init__(self, data):
        self.n = data

    def process(self):
        result = sum(int(digit) for digit in str(self.n))
        return result


def execute_classes(class_sequence, initial_input):
    data = initial_input
    for class_name in class_sequence:
        class_instance = class_name(data)
        data = class_instance.process()
        print(f"Output after processing with {class_name.__name__}: {data}")
    return data


# Take initial number from the user
initial_number = int(input("Enter the initial number: "))

# Take the sequence of class execution from the user
print("Choose the order of classes to execute:")
print("1. SumDigitsClass1")
print("2. SumDigitsClass2")
print("3. SumDigitsClass3")

user_sequence = input("Enter the sequence of class numbers separated by commas (e.g., 1,3,2): ")
class_sequence = []

# Map user input to actual class names
class_mapping = {
    '1': SumDigitsClass1,
    '2': SumDigitsClass2,
    '3': SumDigitsClass3
}

for class_number in user_sequence.split(','):
    class_sequence.append(class_mapping[class_number.strip()])

# Execute the classes in the chosen order
final_output = execute_classes(class_sequence, initial_number)
print("Final output:", final_output)
