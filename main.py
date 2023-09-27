import os
import xmind_parser.xmind_to_tree as xmind_to_tree
import xmind_parser.excel_output as excel_output
from xmind_parser.config_loader import get_config

def format_print(text: str, max_len: int, char="*") -> str:
    length = len(text)
    if length > max_len:
        return text
    char_len = max_len - length
    return text.center(char_len, char)

if __name__ == "__main__":
    # 输入XMind文件路径
    current_directory = os.getcwd()

    # 加载配置
    config_path = current_directory + f"\\config\\Testcase_config.json"
    config_data = get_config(config_path)
    file_name = config_data["必填项"]["用例文件名"]
    if file_name == "":
        print("请在配置中填写文件名")

    xmind_file_path = current_directory + f"\\input\\{file_name}.xmind"
    excel_file_path = current_directory + f"\\output\\{file_name}.xlsx"
    print(f"\n开始解析xmind文件，文件路径：{xmind_file_path}\n\n")
    
    print(f"配置文件路径：{config_path}\n\n")
    
    # 调用解析函数
    parsed_tree = xmind_to_tree.parse_xmind_to_tree(xmind_file_path)

    # 输出解析结果
    excel_output.process_to_excel(parsed_tree, excel_file_path, config_data)
    print(f"转换已结束\n\n")
    print(f"excel文件已输出到：{current_directory}\output\{file_name}.xlsx\n")