t=int(input())
while t:
	t-=1
	ar=[]
	a,b=list(map(int,input().split()))
	for i in range(a,b+1):
		if(i>1):
		    for j in range(2,i):
			    if(i%j==0):
				    break
		    else:
			    ar.append(i)
	for i in ar:
		print(i)
	print()
				
			