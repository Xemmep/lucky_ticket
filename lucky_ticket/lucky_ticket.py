# -*- coding: cp1251 -*-
t = input('�������  �����: ')
l = int(t[0]) + int(t[1]) + int(t[2])
r = int(t[3]) + int(t[4]) + int(t[5])
if l == r:
    print('Yes')
else:
    print('NO')
# ���
s = input('������� 6-�������  �����: ')
if len(s) != 6:
    print(f'����� {s} �� 6-���������')
else:
    res1 = 0
    res2 = 0
    for i in range(len(s)//2):
        res1 += int(s[i])
        res2 += int(s[len(s)//2 + i])
    if res1 == res2:
        print(f'{s} ���������� �����')
    else:
        print(f'{s} �� ���������� �����')
