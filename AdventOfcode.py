



    
name = open("FirstLab_1.txt",'r')
list = []
counter = 0
j = 1
for line in name:
        list.append(int(line))


for x in range(len(list)):
    if j >= len(list):
        break
    if list[x] < list[j]:
        counter += 1
    j += 1
print(counter)
    

        
        
    
 
        
    
    
    
    