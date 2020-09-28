import xml.etree.ElementTree as ET

tree = ET.parse("StateChart.xml")
root = tree.getroot()
print(root.tag, ":", root.attrib)  # 打印根元素的tag和属性

# 遍历xml文档的第二层
for child in root:
    # 第二层节点的标签名称和属性
    print(child.tag,":", child.attrib) 
    # 遍历xml文档的第三层
    for children in child:
        # 第三层节点的标签名称和属性
        print(children.tag, ":", children.attrib)