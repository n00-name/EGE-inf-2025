import string
x = string.digits + string.ascii_uppercase
for i in x:
    s1 = i + '1418'
    s2 = '1' + i + '037'
    s3 = '2' + i + '209'

    if int(s1, 13) + int(s2, 14) == int(s3, 19):
        print(int(s3, 19))
        break
