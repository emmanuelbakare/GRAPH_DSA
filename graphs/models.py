from django.db import models

class Node(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class GraphGroup(models.Model):
    name=models.CharField(max_length=50)
    # graph=models.ForeignKey(Graph, on_delete=models.CASCADE, related_name='nodes')
    def __str__(self):
        return self.name


class Graph(models.Model):
    fromNode=models.ForeignKey(Node, on_delete=models.DO_NOTHING,related_name="nodes")
    toNode=models.ForeignKey(Node, on_delete=models.DO_NOTHING, related_name="toNode")
    groups=models.ForeignKey(GraphGroup, on_delete=models.CASCADE, related_name="graphs")
    weight=models.IntegerField(default=0)

    class Meta:
        unique_together =('groups','fromNode', 'toNode')

    def __str__(self):
        return f"{self.fromNode}---{self.weight}--->{self.toNode}"
    





 