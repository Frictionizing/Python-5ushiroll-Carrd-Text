def mult_list(lis):
    if len(lis) == 0:
        return 1
    else:
        return lis.pop() * mult_list(lis)


def reverse(x):
    st = ""
    for i in range(len(x)-1, -1, -1):
        st += x[i]
    return st 

print(mult_list([2,2,3,4]))
print(reverse("sammich"))