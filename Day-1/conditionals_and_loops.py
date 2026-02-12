language = 'java'

if language == 'python':
    print('language is python')
elif language == 'java':
    print('language is java')
else:
    print('no match')

nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print('found')
        break
    print(num)

x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
