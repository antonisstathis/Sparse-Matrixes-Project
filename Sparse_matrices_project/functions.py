import random
from functions1 import ask_travel,ask_option,update_weight

random.seed(228524)

def create_weights(V):
    weights=list()
    for node1 in range(1,V+1):
        for node2 in range(1,V+1):
            if node1==node2:
                weights.append(0)
            else:
                weight=random.randint(50,100)
                weights.append(weight)

    
    return weights


def create_travels(V,n,a1_jloc,a1_irow,a1_jval,weights):
    
    a1_jloc.append(0)
    index=0
    for travel in range(1,n+1):
        nodes=list()
        total_cost=0
        total_nodes=0
        
        while (total_cost<200 or total_cost==200):

            check=0
            while (check==0):
                node=random.randint(1,V)
                check=check_node(node,nodes)
                if (check==1):
                    nodes.append(node)
                    total_nodes=total_nodes+1

            total_cost=calculate_cost(V,nodes,total_cost,weights)
        
        for node in nodes:
            a1_irow.append(node)

        index=index+total_nodes

        if (travel!=n):
            a1_jloc.append(index)
            
        a1_jval.append(total_cost)



def check_node(node,nodes):

    n=len(nodes)

    if (n==0):
        return 1
    else:
        for i in range(n):
            if (nodes[i]==node):
                return 0
        
        return 1



def calculate_cost(V,nodes,total_cost,weights):
    

    # indexes of list weights
    # line 0: from 0 to 799
    # line 1: from 800 to 1599
    # line 2: from 1600 to 2399
    # ...
    # ...
    # line 100: from 80000 to 80799
    # ...
    # ...
    # line 798: from 480000 to 559999
    # line 799: from 560000 to 639999


    if (len(nodes)!=1):
        line=nodes[-2]-1
        column=nodes[-1]-1
        index=V*line+column
        total_cost=total_cost+weights[index]
        return total_cost
    else:
        total_cost=0
        return total_cost

def add_node(V,n,a1_jloc,a1_irow,a1_jval,weights):
   
    travel=ask_travel()
    
    option=ask_option()
    
    nodes=print_results(a1_jloc,a1_irow,a1_jval,travel)
     
    check=0
    while (check==0):
        node=random.randint(1,V)
        check=check_node(node,nodes)
    
    if (option=='s'):
        index=a1_jloc[travel-1]
        update_nodes(V,index,a1_irow,a1_jloc,a1_jval,weights,node,nodes,option,travel)
    else:
        index=a1_jloc[travel]
        update_nodes(V,index,a1_irow,a1_jloc,a1_jval,weights,node,nodes,option,travel)
    
    print("\n\nNodes updated in travel "+str(travel)+".")
    nodes=print_results(a1_jloc,a1_irow,a1_jval,travel)
    

def print_results(a1_jloc,a1_irow,a1_jval,travel):
    
    nodes=list()
    print("travel="+str(travel))
    start=a1_jloc[travel-1]
    end=a1_jloc[travel]-1
    print("start="+str(start))
    print("end="+str(end))
    for i in range(start,end+1):
        node=a1_irow[i]
        nodes.append(node)
    print(nodes)
    print("weight="+str(a1_jval[travel-1]))

    return nodes

def update_nodes(V,index,a1_irow,a1_jloc,a1_jval,weights,node,nodes,option,travel):

    a1_irow.insert(index,node)
    update_weight(V,a1_jval,weights,nodes,option,travel)
    a1_jloc[travel]+=1

def calculate_product(V,n,a1_irow,a1_jloc):

    l1=list()
    l2=list()
    b_iloc=list()
    b_jval=list()
    b_val=list()
    travel1=0
    travel2=0
    value=0
    counter=0

    b_iloc.append(0)
    for i in range(1,n+1):
        l1=get_travel(n,a1_irow,a1_jloc,i)
        for j in range(1,n+1):
            l2=get_travel(n,a1_irow,a1_jloc,j)
            reps=min(len(l1),len(l2))
            for k in range(reps):
                if (l1[k]==l2[k]):
                    value=value+1
            if (value!=0):
                b_jval.append(j)
                b_val.append(value)
                counter=counter+1
        b_iloc.append(counter)
        counter=0

    print("\n\n")
    print(len(b_iloc))
    print(len(b_jval))
    print(len(b_val))

def get_travel(n,a1_irow,a1_jloc,num):

    travel=list()

    if (num<n):
        start=a1_jloc[num-1]
        end=a1_jloc[num]
        for i in range(start,end):
            travel.append(a1_irow[i])
    if (num==n):
        start=a1_jloc[num-1]
        for i in range(start,n):
            travel.append(a1_irow[i])


    return travel
            
def print_data(a1_jloc,a1_irow,a1_jval):

    print("Travels created.")
    print("The length of a1_jloc array is:"+str(len(a1_jloc)))
    print("The length of a1_irow array is:"+str(len(a1_irow)))
    print("The length of a1_jval array is:"+str(len(a1_jval)))
    print("\n\n")
    
        
def calculate_min(V,n,a1_jloc,a1_irow,a1_jval):

    visit=list()
    for i in range(V):
        visit.append(0)

    for node in a1_irow:
        visit[node-1]=visit[node-1]+1
    
    visits=min(visit)
    position=visit.index(visits)
    node=position+1

    print("The destination with less visits is:"+str(node)+".")  
