# We have 2 input lists lst1 and lst2
# lst1 is of size n and lst 2 is of size m
# lst1 populated with x values and rest y are place holders such that y = m
# both the list are sorted
# out is required to have all the values of lst2 also in lst1 (as we have the placeholders)
# and still the lst1 should be sorted

# Below solution has complexity of Orcder O(n) + O(m)

lst1 = [12,14,16,18,0,0,0,0]
lst2 = [2,5,7,123]


j = len(lst2) - 1
i = j
k = len(lst1) - 1

while k >= 0:
    if lst2[j] > lst1[i]:
        lst1[k] = lst2[j]
        j -= 1
        print("1 : " + str(lst1))
    else:
        lst1[k] = lst1[i]
        i -= 1
        print("2 : " + str(lst1))
    k -= 1
    if i < 0 or j < 0: break

if i < 0:
    for x in range(j,-1,-1):
        lst1[k] = lst2[x]
        k -= 1
elif j < 0:
    for x in range(i,-1,-1):
        lst1[k] = lst2[x]
        k -= 1

print("\nF : " + str(lst1))
