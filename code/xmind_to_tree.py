import zipfile
import json
from .ListNode import TreeNode

def parse_xmind_to_tree(input_file: str) -> list:
    # 以zip包的方式打开xmind文件，从中读取content.json
    with zipfile.ZipFile(input_file, 'r') as z:
        # 打开content.json文件
        with z.open('content.json') as f:
            # 读取文件内容
            content = f.read()
            #加载JAON对象
            data = json.loads(content)

    # 获取根节点（通常是第一个 sheet 的根节点）
    dictData = data[0]["rootTopic"]

    print(dictData)
    
    # 建立多叉树根节点，并递归调用子主题
    root_id = dictData["id"]
    root_title = dictData["title"]
    root_node = TreeNode(root_id, root_title, None, None, None)
    for i in dictData["children"]["attached"]:
        root_node.add_child(create_tree_node(i))
    
    return root_node

def create_tree_node(dictData: dict) -> TreeNode:
    # 识别用例目录并准备创建目录节点或用例节点的数据
    id, title = dictData["id"], dictData["title"]
    step, result, level = None, None, None

    # FIXME: 用例目录识别符号替换成可配置形式
    if title[0] == "-":
        node = TreeNode(id, title, step, result, level)
        for i in dictData["children"]["attached"]:
            node.add_child(create_tree_node(i))
        return node
    else:
        # 设置用例数据
        level = dictData["markers"][0]["markerId"]
        match level:
            case "priority-1":
                level = "高"
            case "priority-2":
                level = "中"
            case "priority-3":
                level = "低"
            case _:
                level = "低"
        steptopic = dictData["children"]["attached"][0]
        resulttopic = steptopic["children"]["attached"][0]
        step = steptopic["title"]
        result = resulttopic["title"]
        return TreeNode(id, title, step, result, level)