from  collections import defaultdict

#my_dict = defaultdict(lambda : 1)
#my_dict[1] = 'a'
#my_dict = {1: 'a'}

#print((my_dict[2]))

s = 'Hello'
d = defaultdict(int)
for k in s:
    d[k] += 1
print(sorted(d.items()))

