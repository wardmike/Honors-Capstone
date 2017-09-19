f = open('prices/bit.txt', 'r')
lines = f.read().splitlines()

prcs=[]
for line in lines: prcs.append(float(line))
    
i=0
buy,profit=0.0,0.0
for prc in prcs:
    if(i>9):
        avg=(prcs[i-1]+prcs[i-2]+prcs[i-3]+prcs[i-4]+prcs[i-5])/5.0
        #if(prc<avg*.97 and buy==0.0):#mean reversion
        if(prc>avg and buy==0.0):
            print "day",i,"we bought at stock at price: ",prcs[i]
            buy=prc
        #elif(prc>avg*1.03 and buy!=0.0):
        elif(prc<avg and buy!=0.0):
            print "day",i,"we sold at stock at price: ",prcs[i]
            print "profit for this trade: ",prcs[i]-buy
            profit+=prcs[i]-buy-(prcs[i]*.03)
            buy=0.0
    i+=1
print "total profit: ",profit
print "returns: ",profit/prcs[0]
print "overall return: ",prcs[-1]/prcs[0]


