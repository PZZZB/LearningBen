import os
import sd
from sd.tools import io
from sd.ui.graphgrid import *
from sd.api.sbs.sdsbscompgraph import *
from sd.api.sdvalueint import *
from sd.api.sdvaluestring import *
from sd.api.sdvaluefloat import *
from sd.api.sdvaluebool import *
from sd.api.sdtypefloat2 import *
import sd.api.sdgraph

# 批量读取贴图base color/normal/roughness/ao/height, 设置到Graph的输入上，然后执行输出结果CR/NOH保存到磁盘

# Get the application and UI manager object.
context = sd.getContext()
app = context.getSDApplication()
uiMgr = app.getQtForPythonUIMgr()
packMgr = app.getPackageMgr()

# Get the current graph
g = uiMgr.getCurrentGraph()
print("The current graph is %s" % g.getIdentifier())

outputNodes = g.getOutputNodes()
for outputNode in outputNodes:
    print(outputNode.getIdentifier())
    props = outputNode.getProperties(SDPropertyCategory.Output)
    for prop in props:
        print(prop.getId())

##nodeMakeCRNOH = g.getNodeFromId("MakeCR_NOH")
nodes = g.getNodes()


# for node in nodes:
#     print("Input")
#     properties = node.getProperties(SDPropertyCategory.Input)
#     for prop in properties:
#         print(prop.getId())
#     print("Output")
#     propertiesO = node.getProperties(SDPropertyCategory.Output)
#     for prop in propertiesO:
#         print(prop.getId())
#     print("Annotation")
#     propertiesA = node.getProperties(SDPropertyCategory.Annotation)
#     for prop in propertiesA:
#         print(prop.getId())
##print("The MakeCRNOH Node %s", nodeMakeCRNOH.getIdentifier())

# Get the currently selected nodes
#selection = uiMgr.getCurrentGraphSelection()
# for node in selection:
#    print("Node %s" % node)
