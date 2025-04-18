import re

s = open('24-298.txt').readline()
s = re.sub('[-*]0+', ' ', s)  # не натуральные
s = re.sub('[^0-9]{2,}', ' ', s)  # //>=2 не цифр
s = re.sub(' 0', ' ', s).split()  # лидирующие 0
print(s)
print(max([len(x) for x in s]))