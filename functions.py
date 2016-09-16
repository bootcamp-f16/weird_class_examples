def add_five(num):
    return num + 5

def is_ten():
    return 10

add_five(is_ten()) # => 15

val = is_ten()
add_five(val) # => 15

def add_seven_from_is_fifteen():
    return is_fifteen() + 7

def is_fifteen():
    return 15

add_seven_from_is_fifteen() # => 22

class AddTen():
    def do_the_adding(self, num):
        return num + 10

instantiated_from_add_10 = AddTen()
instantiated_from_add_10.do_the_adding(is_fifteen()) # => 25

class PrintValues():
    def __init__(self, value):
        self.value = value

    def do_printing(self):
        print("The value is {}".format(self.value))

    def print_from_add_10(self):
        print(AddTen().do_the_adding(4))

value = instantiated_from_add_10.do_the_adding(is_ten()) # => 20
p_val = PrintValues(value)
p_val.do_printing() # => 'The value is 20'
p_val.print_from_add_10() # => 14
