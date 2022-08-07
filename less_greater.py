def lesser_greater(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)
print(lesser_greater(2,4))        
