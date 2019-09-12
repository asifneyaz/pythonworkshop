import xml.etree.cElementTree as ET 
tree = ET.ElementTree(file='test.xml')
root = tree.getroot()
for child in root:
    if(child.tag =='magazine'):
        print(child.get('id'))
