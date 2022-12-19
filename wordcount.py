"""Count words in file."""

file = open("twain.txt")

dict = {}

words = []

for line in file:
    for word in line.split():
        words.append(word)


# for word in words:
#     if word in dict:
#         dict[word] += 1
#     else:
#         dict[word] = 1

for word in words:
    dict[word] = dict.get(word, 0) + 1

print(dict)



# dict = {}
# for line in file:
#      for word in line.split():
#         dict[word] = dict.get(word,0) + 1