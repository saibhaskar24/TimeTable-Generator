import gtable
import matplotlib.pylab as pl

names = ["Python","WT","DBMS","Flat","CO", "OS"]
Labs = ["L1", "L2","L3"]
subphrs = 5 #25
labhrs = 9
extrahrs = 8
examhrs = 6


def conv(table):
    for i in table:
        for j in range(len(i)):
            if int(i[j]) < 7:
                if int(i[j]) == 0:
                    i[j] = 'Unallocated'
                else:
                    i[j] = names[int(i[j])-1]
            else:
                i[j] = Labs[int(i[j]) - 25 ]
    return table



table = gtable.gentable().tolist()
table = conv(table)
print(table)

ny = len(table)
nx = len(table[0])

pl.figure()
tb = pl.table(cellText=table, loc=(0,0), cellLoc='center')

tc = tb.properties()['child_artists']
for cell in tc: 
    cell.set_height(1/ny)
    cell.set_width(1/nx)

ax = pl.gca()
ax.set_xticks([])
ax.set_yticks([])

pl.show()