W = int(input())
dict_word = {}
while True:
    try:
        line = input()
    except EOFError:
        break
    proced_line = []
    for i in range(len(line)):
        if line[i].isalpha():
            proced_line.append(line[i])
        else:
            proced_line.append(' ')

    proced_line = ''.join(proced_line)
    #print(proced_line)

    line = [x.strip().lower() for x in proced_line.split(' ')]
    #print(line)
    for word in line:
        if len(word) == W:
            if word not in dict_word:
                dict_word.update({word: 1})
            else:
                dict_word[word] += 1
#print(len(dict_word))
if len(dict_word) == 0:
    exit(0)
max_pop = max(dict_word.values())
#print(max_pop)
output = []

for word, count in dict_word.items():
    if count == max_pop:
        output.append(str(word))

print(' '.join(sorted(output)))
