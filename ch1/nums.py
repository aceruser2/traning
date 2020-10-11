def gen(n):
    
    for i in range(1,n+1):
        if 5>=i>0:
                yield i+i
        if 50>=i>5: 
                yield i*i
        if i>50:            
                yield (2*i+3*i)

for i in gen(60):
    print(i)

# for i in gen(7):
#     print(i)

# for i in gen(69):
#     print(i)
