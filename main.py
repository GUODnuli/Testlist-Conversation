import os
import xmind_parser.xmind_to_tree as xmind_to_tree
import xmind_parser.excel_output as excel_output
from xmind_parser.Data_struct import TreeNode
from xmind_parser.config_loader import config_dict

def traverse_tree(node: TreeNode, depth=0):
    if node.title[0] != '-':
        print(f"{'  ' * depth}{node.title} {node.step} {node.result}")
    else:
        print(f"{'  ' * depth}{node.title}")
    for child in node.children:
        traverse_tree(child, depth + 1)

if __name__ == "__main__":
    # 输入XMind文件路径
    current_directory = os.getcwd()
    xmind_file_path = current_directory + "\\examples\\example.xmind"
    config_path = current_directory + "\\config\\xmind_config.json"
    print(f"开始解析xmind文件，文件路径：{xmind_file_path}")
    print(f"配置文件路径：{config_path}")
    
    # 调用解析函数
    config_data = config_dict(config_path)
    parsed_tree = xmind_to_tree.parse_xmind_to_tree(xmind_file_path)

    # 输出解析结果
    excel_output.process_to_excel(parsed_tree, "output\output.xlsx")