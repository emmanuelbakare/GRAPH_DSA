from django.contrib import admin
from graphs.models import Graph, Node, GraphGroup
# Register your models here.


class GraphInline(admin.TabularInline):
    model= Graph 


class GraphGroupAdmin(admin.ModelAdmin):
    inlines=[GraphInline]

admin.site.register(GraphGroup, GraphGroupAdmin)
admin.site.register(Node)


# class NodeInline(admin.TabularInline):
#     model = Node 
    
# class GraphAdmin(admin.ModelAdmin):
#     inlines=[NodeInline]


# admin.site.register(Graph, GraphAdmin)
# admin.site.register(Node)
# admin.site.register(Graph)
# admin.site.register(GraphGroup)