def Numbers_Equality(a,b,c):
    if a == b and a == c:
        return True
    elif b == a and b == c:
        return True
    elif c == a and c == b:
        return True
    else:
        return False


Equality = Numbers_Equality(1,1,1)
# print("no {} is equal to no {} and also equal to no {}".format(1,2,3))
print(Numbers_Equality(2,2,2))

