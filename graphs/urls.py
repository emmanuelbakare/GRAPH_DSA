from django.urls import path, include 
from graphs import views

app_name="graphs"

urlpatterns =[ 
    path('', views.dashboard),
    path('<int:pk>/', views.graph_nodes, name='graph_nodes'),
   
   #Graph Diagram Paths
    path('nodeshow/', views.graph_diagram, name="nodeshow"),
    path('dfsshow/', views.graph_diagram_dfs, name="dfsshow"),
    
    
    
   #htmx endpoints
    path('node2/<str:name>/', views.get_graph2, name='node_details2'),

]