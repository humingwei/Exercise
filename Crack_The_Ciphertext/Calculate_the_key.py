data = [int(i) for i in open('cipher1.txt').read().strip().split(",")]
#print  data

d = {}
for i in data:
    d[i] = data.count(i)

keys = sorted(d.iteritems(), key=lambda x:x[1])[-3:]
print keys

for k,v in keys:
    print k ^ 32, chr(k ^ 32)
