import math
import os
import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = 'hello, {}'.format(who_to_greet)
    return greeting

    print(greet('World'))
    print(greet('Cody'))
