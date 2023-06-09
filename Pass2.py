from tabulate import tabulate

ipCode=['START 100', 'READ N1', 'READ N2', 'READ N3', 'DECR N1,N2,N3', 'STOP', 'N1 DS 1', 'N2 DS 2', 'N3 DS 3', 'END']
MNT=[[1, 'INCR', 0], [2, 'DECR', 5]]
MDT=[[0, 'INCR &X,&Y,&REG1'], [1, 'MOVER #3,#1 '], [2, 'ADD #3,#2'], [3, 'MOVEM #3,#1'], [4, 'MEND'], [5, 'DECR &A,&B,&REG2'], [6, 'MOVER #6,#4'], [7, 'SUB #6,#5'], [8, 'MOVEM #6,#4'], [9, 'INCR #4,#5,#6'], [10, 'MEND']]
ALA=[['#1', '&X'], ['#2', '&Y'], ['#3', '&REG1'], ['#4', '&A'], ['#5', '&B'], ['#6','&REG2']]

i = 0
ala_ip = []
ala_code = []
ala_index = []
while i < len(ipCode):
    j = 0
    while j < len(MNT):
        if ipCode[i].split()[0] == MNT[j][1]:
            startIndex = MNT[j][2]
            try:
                endIndex = MNT[j + 1][2] - 1
            except IndexError:
                endIndex = len(MDT) - 1
            ipIndex = i
            ala_ip += ipCode[i].split()[1].split(',')
            ala_code += MDT[startIndex][1].split()[1].split(',')
            for k in MDT[startIndex][1].split()[1].split(','):
                for x in ALA:
                    if x[1] == k:
                        temp = x[0]
                ala_index.append(temp)
            del ipCode[i]
            for k in range(startIndex, endIndex):
                temp = MDT[k][1]
                for x in range(0, len(ala_ip)):
                    temp = temp.replace(ala_index[x], ala_ip[x])
                    temp = temp.replace(ala_code[x], ala_ip[x])
                ipCode.insert(ipIndex, temp)
                ipIndex += 1
            break
        j += 1
    i += 1

pass2 = []
for i, index in enumerate(ipCode):
    pass2.append([i, index])

print('\n===========PASS 2===========')
print(tabulate(pass2, tablefmt="simple_grid", headers=['Index', 'Code']))
