# Input  - List of n integers
# Output - For every element lst[i] we want the produc of all elements of the list
#          excluding element lst[i]
# E.g.   - Input  : lst = [1,2,3,4]
#          Output = res = [24,12,8,6]
# Explanation :-
# res[0] = lst[1]*lst[2]*lst[3] = 2*3*4 = 24
# res[1] = lst[0]*lst[2]*lst[3] = 1*3*4 = 12
# res[2] = lst[0]*lst[1]*lst[3] = 1*3*4 = 8
# res[3] = lst[0]*lst[1]*lst[2] = 1*2*3 = 6

# Below solution uses O(n) complexity

l = [1,2,3,4,5,6,7,8,9,10]
l = [1,2,3,4]

l_len = len(l)

l_prd = [1]*l_len
r_prd = [1]*l_len

for i in range(1,l_len):
    l_prd[i] = l_prd[i-1]*l[i-1]

for i in range(l_len-2,-1,-1):
    r_prd[i] = r_prd[i+1]*l[i+1]

print("Left Product    : " + str(l_prd))
print("Right Product   : " + str(r_prd))

product = [l_prd[i]*r_prd[i] for i in range(l_len)]

print("\nExpected Output : " + str(product))
