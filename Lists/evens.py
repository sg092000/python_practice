from functools import reduce

nums = [3,4,5,6,7,6,8,9,0]

result = list(filter(lambda n : n%2==0 , nums))

doubles = list(map(lambda n : n*2 , result))

sum = reduce(lambda a,b : a+b,doubles)

print(sum)

employee = {}
employee['Name'] = "Mehul"
employee['Mobile'] = [982789876,98768987]
print(employee)

emp = []
emp.append({'Name':"Mehul",'Mobile':[987658765]})
emp.append({'Name':"samarth",'Mobile':[78787878]})

print(emp)

listMobile = []
for x in emp:
    try:
        mob = x['Mobile'][1]
        listMobile.append(mob)
    except Exception as e:
        print("no data found:  " , e)
    
print(listMobile)