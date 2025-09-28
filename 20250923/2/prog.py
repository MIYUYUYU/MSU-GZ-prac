ipt = [int(x.strip()) for x in input().split(',')]
indexed_number = [(num, idx)for idx, num in enumerate(ipt)]
proc = [(num**2 % 100,idx) for num,idx in indexed_number]
for i in range(len(proc)):
    for j in range(i+1,len(proc)):
        if proc[i][0] > proc[j][0]:
            proc[i], proc[j] = proc[j], proc[i]
opt = [ipt[proc[i][1]] for i in range(len(ipt))]
print(opt)
#print(proc)
#print(proc)