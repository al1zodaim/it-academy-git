text = "1 1 1 1"
text_list = text.split(' ')

count_pair = 0

for i in range(len(text_list)):
    for j in range(i + 1, len(text_list)):
        if text_list[i] == text_list[j]:
            count_pair = count_pair + 1

print(count_pair)