key = 'keyence'
word = ''
s = input()
s_list = list(s)
flag = True

for i in key:
    if not i in s_list:
        print('NO')
        flag = False
        break
    s_list.remove(i)

for j in s_list:
    word += j

print(word)

if flag:
    if s.count(word) == 1 or len(word) == 0:
        print('YES')
    else:
        print('NO')