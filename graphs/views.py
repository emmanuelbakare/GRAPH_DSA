from django.shortcuts import render
from graphs.models import Graph, Node, GraphGroup

from utils.graph_algol import iGraph, make_dfs_diag, make_diag # import graph modules



# list all graph groups 
def dashboard(request):
    context={
        'groups': GraphGroup.objects.all()
        } 
    return render(request,'graph/dashboard.html', context)


#get a specific graph from the group pk
def graph_nodes(request,pk):
    group=GraphGroup.objects.get(pk=pk)
    graphs=group.graphs.all()
    
    
    #generate the graph as your generate the web outputs
    graph_to_print=get_group_node_dict(pk)
    
    make_diag(graph_to_print)
    
    
    #generate graph, make dfs and draw dfs network
    root_node=graphs.first().fromNode.name  # get root node
    igraph=iGraph()
    igraph.dfs(graph_to_print, root_node)
    make_dfs_diag(igraph.dfs_path)  
   
    context={ 
        'graphs':graphs  
    }
    
    return render( request, 'graph/node_list.html', context)



def get_graph(request, name):
    context={'name':name,'neighbours': graph_dict(name)}
    return render(request, 'graph/get_graph.html', context)

def get_graph2(request, name):
    
    context={
        'graphs': graph_dict(name, False),
        'nodes': Node.objects.all(),
       
        }
    # return render(request, 'graph/get_graph.html', context)
    return render(request, 'graph/dashboard.html', context)

 

# the diagram view - after module draw graph. this view displays it
def graph_diagram(request):
    return render(request, 'diagrams/nodeshow.html')

# the DFS diagram view - after module draw graph. this view displays it
def graph_diagram_dfs(request):
    return render(request, 'diagrams/dfs_show.html') 







def graph_dict(name,query=True):
        node_dict=set() 

        graphs=Graph.objects.filter(fromNode__name__iexact=name)
        
        if query:
            return { graph.toNode.name for graph in graphs}
        else:
            return graphs

def get_all_node_dict():

    nodes=Node.objects.all()
    return {node.name:[graph.toNode.name for graph in Graph.objects.filter(fromNode__name__iexact=node.name)] for node in nodes}
    
#get the graph dict according to the group picked as pk
def get_group_node_dict(pk):
    group_=GraphGroup.objects.get(pk=pk)
    all_nodes=set()
    
    for node in group_.graphs.all():
        # all_nodes+={node.fromNode} | {node.toNode }
        all_nodes.add(node.fromNode)
        all_nodes.add(node.toNode)
        
    # from_nodes={node.fromNode for node in group_.graphs.all()}
    # to_nodes={node.toNode for node in group_.graphs.all()}
    # all_nodes= from_nodes | to_nodes 
    
    return {node.name:[graph.toNode.name for graph in Graph.objects.filter(fromNode__name__iexact=node.name, groups__name__icontains=group_.name)] for node in all_nodes}
    
    
    
    
    

  
# print('All NODES',get_all_node_dict()) 

# print()
# print()   
# print('FIRST NODES',get_group_node_dict(1))    
# print('SECOND NODES',get_group_node_dict(2))    
# print('THIRD NODES',get_group_node_dict(3))    
  
# graph_to_print=get_all_node_dict()
# graph_to_print=get_group_node_dict(2)

# dfs2(visited, graph_to_print, 'A') 
# print()
# print('DFS PATH',dfs_path)      
   
# make_diag(graph_to_print)  
# make_dfs_diag(dfs_path)  
# print(graph.graphdict())            