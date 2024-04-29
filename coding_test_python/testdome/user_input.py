class TestInput:
    def __init__(self):
        self.value = ""

    def add(self, character):
        self.value += character

    def get_value(self):
        return self.value


# class
class NumberInput(TestInput):
    def add(self, character):
        if character.isdigit():
            self.value += character

    def get_value(self):
        return self.value


test_input = TestInput()
test_input.add("1")
test_input.add("1")
test_input.add("1")
print(test_input.get_value())


test_number = NumberInput()
test_number.add("1")
test_number.add("a")
test_number.add("0")
print(test_number.get_value())

