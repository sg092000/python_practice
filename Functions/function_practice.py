def isPal(str):
    i = 0
    j = len(str)-1
    while(i <= j):
        if(str[i] != str[j]):
            return False
        i+=1
    return True

str = input("enter string : ")
print(str)
print("\nChecking whether it is palindrome or not")
ans = isPal(str)
if(ans):
    print("palindrome")
else:
    print("not a palindrome")