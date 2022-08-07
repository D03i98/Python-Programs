def almost_there(n):
    if abs(100-n) <= 10 or abs(200-n) <= 10:
        return True
    else:
        return False
print(almost_there(300))