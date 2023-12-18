l = [10, 5, 99, 49, 3.2, 4, 99, 1, 45]

print(l)

# for index in range(len(l)):
#     print(l[index])

min_actuel = l[0]

for item in l:
    print("item :", item, "----- min actuel :", min_actuel)
    if min_actuel > item:
        min_actuel = item
    
# salut


