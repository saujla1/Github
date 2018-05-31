class my_class(object):
    def func():
        fopen=open("D:\Resume\python.txt")
        counts=dict()
        readFile=fopen.read()
        
        for r in readFile:
            if r not in counts:
                counts[r]=1
            else:
                counts[r]=counts[r]+1
            
        #print(counts)
        #print([v for k,v in counts.items()])
        ke=list(counts.keys())
        #print(ke)
        ve=list(counts.values())
        #print(ve)
        #print(ke[ve.index(max(ve))])
        
                
        #print([k for k,v in counts.items() if v==(max(counts.values()))])
        for k,v in counts.items():
            if v==max(counts.values()):
                print("the highest value is:", [k])
       
            
    




