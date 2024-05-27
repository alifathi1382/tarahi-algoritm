a = {'sam', 'sung', 'samsung', 'like', 'i', 'ice', 'mobile', 'cream', 'ice cream', 'man', 'mango'}
b=input('pleas enter any word :')
# b = 'ilikesamsung'
result = []
i = 0
while i < len(b):
    found=False
    for j in range(i + 1, len(b) + 1):
        word = b[i:j]
        print(word)
        if word in a:
            result.append(word)
            i = j-1
            found=True

            break

    i += 1
output = ' '.join(result)
print(result)
print(f'yes,the string can be segemnted as  (({output}))')
