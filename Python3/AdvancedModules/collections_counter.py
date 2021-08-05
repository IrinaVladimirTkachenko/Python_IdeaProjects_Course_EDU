from collections import Counter

number_list = [1, 1, 1, 4, 4, 5, 77, 77, 3, 3, 3, 3, 3]

string = 'dddddkkkkeeeooooooooiiiiiiiiiii'

sentence = "Hello how are you doing? Hello I'm fine. How do you do ? Hey Hey Hey !"

c = Counter(sentence.split(' '))
# c.clear()

# print(list(c))
# print(set(c))
# print(dict(c))
#c = c.items()
#c = Counter(dict(c))
print(c.most_common() [:-2-1:-1])