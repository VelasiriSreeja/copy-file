with open('f1.txt','r') as firstfile:
    with open('f2.txt','a') as secondfile:
        for line in firstfile:
            secondfile.write(line)