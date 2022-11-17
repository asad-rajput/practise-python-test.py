'''
a=int(input("enter the value"))
print("the num is : ", a)
for i in range(1,11): 
    print(a,"*",i,"=",a*i)
    '''
distance=[1,2,5,6,3,7,4,9]
print(len(distance))

if len(distance) > 2:
    distance.pop(0)
    distance.append(5)
    print("the new list is:",distance)
else:
     distance.append(5)


for i in range(len(distance)):
    print(distance[i])
    if distance[i] == 5:
        break
    else:    
        print(distance[i])
         

