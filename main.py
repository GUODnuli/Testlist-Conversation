import os
import xmind_parser.xmind_to_text as xmind_to_text


if __name__ == "__main__":
    # 输入XMind文件路径
    current_directory = os.getcwd()
    xmind_file_path = current_directory + "\examples\example.xmind"
    print(xmind_file_path)
    
    # 调用解析函数
    parsed_list = xmind_to_text.parse_xmind_to_text(xmind_file_path)
    
    # 输出解析结果
    print(len(parsed_list))