from typing import Counter


with open(file='pushkin.txt', mode='r',encoding='utf-8' ) as my_file:
   for line in my_file:
    line=line.split()
    line_counter=0
    for x in line:
        counter=0
        
        if x=='и'.lower():
            counter+=1 
    line_counter+=0
print()

with open(file='file2.json',mode='a',encoding='utf-8') as doc:
    doc.write('\n안녕 친구') 
    doc.write('\nwrite in new line')
    doc.write('\n I dont know why you want to build this time')        
    