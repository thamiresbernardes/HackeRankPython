#runner-up score

import random

second = []
for i in range(2, 10):
    s = random.randint(-100, 100)
    second.append(s)
second.sort(reverse=True)
print(second)
print(second[1])