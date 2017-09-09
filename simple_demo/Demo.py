import sys
import module

age = 20
name = 'mazouri'

# format
print('My name is {0}, and I\' {1} years old.'.format(name, age))
print('My name is {}, and I\' {} years old.'.format(name, age))

dir(sys)

module.say_hi()
module.__version__

dir(module)

print('hello haha')


def testTag():
    print("print from method.")


testTag()
