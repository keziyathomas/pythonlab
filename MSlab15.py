two = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

both=[]

if len(one) < len(two):
    for i in one:
        if i in two and i not in both:
            both.append(i)
         
if len(one) > len(two):
    for i in two:
        if i in one and i not in both:
            both.append(i)
                     
print(both)