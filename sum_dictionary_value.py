dict={"neha":5,"prgati":10,"priya":6,"sonam":7}
value= dict.values()#dictionary me jitni bhi key ki values hai print ho jayegi 
print"multiplication of dictionary value"
i=0
sum=0
while i<len(value):#dictionary ki value ki length jitni hai wahi tak chalega
    sum=value[i]+sum
    i=i+1
print sum # dictionary ki values ka sum print hoga

