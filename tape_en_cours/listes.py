l = [10, 5, 65, 49, 3.2, 4, 56, 4, 45]

print(l)

# for index in range(len(l)):
#     print(l[index])

min_actuel = l[0]
max_actuel = l[0]

for item in l:
    print("item :", item, "----- min actuel :", min_actuel)
    if min_actuel > item:
        min_actuel = item
    if max_actuel < item:
        max_actuel = item
        
print(min_actuel, max_actuel)
    
# salut
 

