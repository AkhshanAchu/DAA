import random
g=["A","C","G","T"]


def randomizer(g,size):
    j=""
    for _ in range(size):
        z = random.randint(0,3)
        j+=g[z]
        
    return str(j)
        
    
    
    
match = 5
penality = -4
table=[]
s1=randomizer(g,16)
s2=randomizer(g,16)
row = len(s1)
column = len(s2)



def creater(row,column):
    for _ in range(row+1):
        s=[]
        for _ in range (column+1):
            s.append(0)
            
        table.append(s)
   
def filler(arr, current_row, current_col,M,N) :
    
    
    
    if (current_col >= M) :
        return False;
    
    if (current_row >= N) :
        return True;
    
    if(current_row!=0 and current_col!=0):
        table[current_row][current_col] = checker(current_row,current_col)
    
    if (filler(arr, current_row, current_col + 1 ,M,N)):
        return True;
    
    return filler(arr, current_row + 1, 0 ,M , N);


def checker(current_row,current_col):
    
    if(s1[current_row-1]==s2[current_col-1]):
        return table[current_row-1][current_col-1]+match;
    else:
        ret = max([table[current_row-1][current_col-1],table[current_row][current_col-1],table[current_row-1][current_col]])
        fin = ret+penality
        
        if fin>=0:
            return fin
        else:
            return 0



creater(row,column)
filler(table, 0, 0, column+1,row+1)
