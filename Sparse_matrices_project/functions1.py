
def ask_travel():
     
    c=0
    flag=True
    while (flag):
        if (c!=0):
            print("You entered invalid input.\n\n")
        print("Enter an integer from 1 to 10000 to choose a travel.")
        travel=input("Choose travel:")
        travel=int(travel)
        if (travel<1 or travel>10000):
            flag=True
        else:
            flag=False
        c=c+1

    return travel

def ask_option():

    option='a'
    flag=0
    while (option!='s' and option!='l'):
        if (flag!=0):
            print("You entered invalid input.\n\n")
        print("Enter 's' to add a destination at the beginning of the travel.")
        print("Enter 'l' to add a destination at the end of the travel. ")
        option=input("Enter 's' or 'l':")
        flag=flag+1

    return option

def update_weight(V,a1_jval,weights,nodes,option,travel):

    if (option=='s'):
        line=nodes[0]-1
        column=nodes[1]-1
        index=V*line+column
        a1_jval[travel-1]+=weights[index]
    else:
        total_cost=a1_jval[travel-1]
        line=nodes[-2]-1
        column=nodes[-1]-1
        index=V*line+column
        a1_jval[travel-1]+=weights[index]

