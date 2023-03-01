tup1 = ('sam', 'sammy', 19, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print(tup1[0])
print(tup2[2:5])

tup3 = tup1 + tup2
print(tup3)

print("\nthe Original tuple : ")
print(tup3)

print("\ntuple using for loop")

for i in range(len(tup3)-1):
    print (tup3[i],end=", ")
print(tup3[len(tup3)-1])

print("\ntuple using while loop")

    
cnt = 0
while(cnt < len(tup3)):
    print(tup3[cnt],end=" ")
    cnt+=1

print("\ntuple using forEach loop")

for i in tup3:
    print(i,end=" ")
    
