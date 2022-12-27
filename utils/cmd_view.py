from  graph_algol import iGraph, make_diag
import os


            
            
            


 
# this get input from users and manage validation
def get_input(msg='Enter Value: ', itype=str):
        
    value=input(msg)
    
    # Exit on no Entry: 
    if len(value.strip())==0: 
        print('No value entered. exiting...')
        exit()
    # if the value entered is not a string, then try to convert it before returning it
    #iType attribute tell what type to convert it to
    if itype is not str:
        try:
            value=itype(value)
        except Exception as e:
            print(f'expecting type {itype}\n{e}')
            return False
    # print(f"Value {converted_value} is {itype}")
    return value
        

def connect_graph():
    while True:
        print()
        nFrom=input("Enter Start Node Value: ")  
        if len(nFrom.strip())==0:
            print('should exit')
            return False
        nTo=input("Enter End Node Value: ")  
        nWeight=input("Enter The Weight In between ")  
        # print()
        # nFrom=get_input(msg="Enter Start Node Value")
        # nFrom=get_input("Enter Start Node Value: ")
        # nTo=get_input("Enter End Node Value: ")
        # nWeight=get_input("Enter The Weight In between ", int)
        
        
        if type(nFrom) != type(nTo):
            print('Start and End Node must be same type')
            continue
        
         
            
        graph.connect(nFrom,nTo,nWeight)
    
# command line interface menu for adding new nodes
def cmd_add_node():
        while True:
            node_name=input("Enter a Node Name: ")
            
            if len(node_name.strip())==0 or node_name=="exit()":
                return False
            node=graph.add_node(node_name)
            

def heading(title):
    print()
    print()
    print(f'====== {title.upper()} ======')
    
    
def menu_interface():
        # os.system('cls')
        actions=['Add Nodes','Print all nodes','Connect_nodes','Show Connections','Show Diagram','Exit']
        
        while True:
            heading("Main Menu")
            for num, action in enumerate(actions,1):
                print(num, action)
           
            # action = int(input("What do you want to do (Enter Number): "))
            action = int(input("What do you want to do (Enter Number): "))
           
            match action:
                case 1:
                    heading("Generate Node")
                    cmd_add_node()
                case 2:
                    heading("Pring All Nodes")
                    print(graph.all_nodes())
                case 3:
                    heading("CONNECT NODES TOGETHER")
                    connect_graph()
                case 4:
                    heading("Show Connected Nodes")
                    graph.graphdict(stringify=True)
                case 5:
                    heading("Show Graph Diagram")
                    make_diag(graph.graphdict())
                case 6:
                    heading("Exiting program")
                    return False
                case _:
                    
                    print("Your Input is Invalid")
                    
                    
           
        
         

graph=iGraph()
menu_interface()
# connect_graph()
# get_input("What are you selling? ", int)