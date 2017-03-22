# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
A=  [0, 1, 3, -2,  0, 1, 0, -3, 2, 3]
def solution(A):
    triplets=[]
    pits=[]
    # write your code in Python 2.7
    pit=-1
    last_direction='up'
    print A
    for x in range(0, len(A)):
       # find all the pits
       if x:
          # if this is less than before is neg start the pit if pit started close the pit start a new pit
          if A[x] < A[x-1]:
               if last_direction=='up':
                  last_direction='down' 
                  pit+=1 
                  pits.append([]) 
                  pits[pit].append(x-1)
               pits[pit].append(x)
          # if this grt  before is pos if pit started put in pit
          if A[x] > A[x-1] and pit!=-1:
               last_direction='up'
               pits[pit].append(x)
       #print A[x]
    # print the pits
    print "pits"
    for x in pits:
        print x
        for y in x:
            print " " , A[y]
    # find the triplets
    print 'find the triplets'
    for p in pits:
        triplets.append([])
        cnt=0
        for x in range(2, len(p)):
           if A[p[x]]>A[p[1]]:
              triplets.append([])
              triplets[cnt].append(p[0])
              triplets[cnt].append(p[1])
              triplets[cnt].append(p[x])
              cnt+=1
        break
              
    for x in triplets:
        print x
    print "triplet ", triplets[0]
    return min(A[triplets[0][0]]-A[triplets[0][1]], A[triplets[0][2]]-A[triplets[0][1]])

print solution(A)
