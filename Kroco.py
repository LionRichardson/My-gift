'''
n=int(input())
s=[]
p=''
games=0
win=0
draw=0
defeat=0
points=0
for i in range(n):
    d=str(input())
    d=d.split(';')
    s+=d
for i in range(0,n*4,2):
    result = ''
    if s[i] not in p:
        p+=s[i]
        name=str(s[i])
        for j in range(0, n * 4, 2):
            if (s[j]==s[i])and((j%4==0)or(j==0)):
                games+=1
                if int(s[j+1])>int(s[j+3]):
                    win+=1
                if int(s[j + 1])==int(s[j + 3]):
                    draw+=1
                if int(s[j + 1])<int(s[j + 3]):
                    defeat+=1
            elif (s[j]==s[i])and(j%4==2):
                games += 1
                if int(s[j + 1]) > int(s[j - 1]):
                    win += 1
                if int(s[j + 1]) == int(s[j - 1]):
                    draw += 1
                if int(s[j + 1]) < int(s[j - 1]):
                    defeat += 1
        points=win*3+draw
        result+=str(name)+':'+str(games)+' '+str(win)+' '+str(draw)+' '+str(defeat)+' '+str(points)
        print(result)
        games = 0
        win = 0
        draw = 0
        defeat = 0
        points = 0
'''
'''
s1=str(input())
s2=str(input())
voc=dict(zip(s1,s2))
s_p=list(input())
s_o=list(input())
ss_p=[]
for i in range(len(s_p)):
    ss_p+=voc[s_p[i]]
ss_p=''.join(ss_p)
print(ss_p)
voc=dict(zip(s2,s1))
ss_o=[]
for i in range(len(s_o)):
    ss_o+=voc[s_o[i]]
ss_o=''.join(ss_o)
print(ss_o)
'''
'''
d=int(input())
k=[]
for i in range(d):
    k+=input().lower().split()
l=int(input())
s=[]
for i in range(l):
    s+=input().lower().split(' ')
w=[]
for i in range(len(s)):
    if (s[i] not in k)and(s[i] not in w):
        w+=s[i].split()
for i in range(len(w)):
    print(w[i])
'''
'''
n=int(input())
x=0
y=0
s=[]
for i in range(n):
    s+=input().split()
for i in range(0,len(s)-1,2):
    if s[i]=='север':
        y+=int(s[i+1])
    elif s[i]=='юг':
        y-=int(s[i+1])
    elif s[i]=='восток':
        x+=int(s[i+1])
    elif s[i]=='запад':
        x-=int(s[i+1])
print(x,y)
'''
'''
# Второе решение данной задачи
coor={'север':0,'юг':0,'восток':0,'запад':0}
for i in range(int(input())):
    s=input().split()
    coor[s[0]]+=int(s[1])
print(coor['восток']-coor['запад'],coor['север']-coor['юг'])
'''
s=[]
n=1
with open('dataset_3380_5.txt','r') as inf, open('result.txt','w') as ouf:
    for line in inf:
        s+=line.split()
    while n!=12:
        k=0
        sr=0
        for i in range(0,len(s)-2,3):
            if int(s[i])==n:
                sr+=int(s[i+2])
                k+=1
        if k!=0:
            ouf.write(str(n)+' '+str(sr/k)+'\n')
        else:
            ouf.write(str(n)+' '+'-'+'\n')
        n+=1




