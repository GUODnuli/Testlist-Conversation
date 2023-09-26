import os
import sys
import xmind_parser.xmind_to_tree as xmind_to_tree
import xmind_parser.excel_output as excel_output
from xmind_parser.config_loader import config_dict

def format_print(text: str, max_len: int, char="*") -> str:
    length = len(text)
    if length > max_len:
        return text
    char_len = max_len - length
    return text.center(char_len, char)

if __name__ == "__main__":
    # 输入XMind文件路径
    current_directory = os.getcwd()

    argv = sys.argv[1:]
    file_name = argv[0]

    xmind_file_path = current_directory + f"\\examples\\{file_name}.xmind"
    config_path = current_directory + f"\\config\\xmind_config.json"
    print(f"\n开始解析xmind文件，文件路径：{xmind_file_path}\n\n")
    
    print(f"配置文件路径：{config_path}\n\n")
    
    # 调用解析函数
    config_data = config_dict(config_path)
    parsed_tree = xmind_to_tree.parse_xmind_to_tree(xmind_file_path)

    # 输出解析结果
    excel_output.process_to_excel(parsed_tree, f"output\{file_name}.xlsx", config_data)
    print(f"转换已结束\n\n")
    print(f"excel文件已输出到：{current_directory}\output\{file_name}.xlsx\n")