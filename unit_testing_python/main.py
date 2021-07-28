import Test_Arithematics
import UnitTest_Arithmetics
import inheritance_example


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def sum(a,b):
    return a + b

def test_example():
    # assert (2 + 2) == 4
    assert sum(2 , 2) == 4

def test_hello_world(name):
    assert name == 'Hello World'


if __name__ == '__main__':
    print_hi('PyCharm')
    test_example()
    # test_hello_world('Pritesh')
    test_hello_world('Hello World')
    # test_hello_world('Hello World')
    Test_Arithematics.Test_Arithmetics().run_test()
    UnitTest_Arithmetics.UnitTest_Arithmetics().run_test()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
    p = inheritance_example.person(1,"param","gill")
    s = inheritance_example.Student(100 , "Pass")

