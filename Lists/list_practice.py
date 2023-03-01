lst = [20,30,50,10,9,8,7]

print("the Original list : " ,lst)

print("\nlist using for loop")

for i in range(len(lst)-1):
    print (lst[i],end=", ")
print(lst[len(lst)-1])

print("\nlist using while loop")

    
cnt = 0
while(cnt < len(lst)):
    print(lst[cnt],end=" ")
    cnt+=1

print("\nlist using forEach loop")

for i in lst:
    print(i,end=" ")
    
lst[2] = 1000
lst[3] = 2000

#deleting an element
del lst[2]

print("\nthe list after modification and deletion: " ,lst)

print("\nmax of list is : ",max(lst))

print("\nmin of list is : ",min(lst))

lst[4] = 20

print("\ncount of list is : ",lst.count(20))

lst.reverse()
print("\nreversed list is : ",lst)


lst.sort()
print("\nsorted list is : ",lst)

lst.append(5000)

print("\nmodified list is : ",lst)

lst.insert(3,3000)


print("\nafter inserting list is : ",lst)

print("popped element : ",lst.pop())

lst.remove(7)
print("list after deleting 7  : ",lst)



