s = input()

# ord('a') == 97
# ord('z') == 122

for i in range(97, 123):
    print(s.find(chr(i)), end = ' ')