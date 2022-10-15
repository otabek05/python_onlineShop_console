emails=[]


with open(file='mbox-short.txt', mode='r', encoding='utf-8') as file:
    i=0
    for line in file:
        line=line.split(' ')
        
        emails=[]

        for word in line:
            if 'from' in word.lower():
                index=line[index]+1
                email=line[index].replace("\ ",' ')
                if "@" in email and '.' in email:
                    if    email not in emails:
                        emails.append(email)

print(emails)

