#program to create a list by concatenating a given list with a range from 1 to n.
#Sample list : ['p', 'q']
#n =5
#Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
def concating(l):
    n=5
    l2=[]
    for i in range(n):
        for y in l:
            l2.append(f'{y}{i}')
    print(l2)
Sample_list= ['p', 'q']
concating(Sample_list)