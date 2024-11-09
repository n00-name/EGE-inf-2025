x = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in x:
    s1 = 'GCJLP2' + i
    s2 = 'I16TN' + i + '6EM'
    s3 = '9TM' + i + 'N'

    f = int(s1, 31) + int(s2, 31) + int(s3, 31)
    if f % 30 == 0:
        print(i, f / 30)