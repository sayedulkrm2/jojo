def example_function():
    print("This line ends with a space character!")  # This line has an extra space at the end.
# Example of refactoring a function with too many parameters
class Configuration:
    def __init__(self, param1, param2, param3):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3


def example_function(config):
    print(config.param1)
    print(config.param2)
    print(config.param3)

# Usage:
config = Configuration(param1='value1', param2='value2', param3='value3')
example_function(config)