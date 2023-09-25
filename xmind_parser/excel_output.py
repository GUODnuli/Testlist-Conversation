import openpyxl
from .Data_struct import TreeNode

def process_to_excel(root: TreeNode, output_file: str):
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # 设置列标题
    headers = ["完整用例文件夹路径", "用例标题", "用例步骤", "用例结果"]
    for col_num, header in enumerate(headers, 1):
        sheet.cell(row=1, column=col_num).value = header

    # 用于存储当前路径的列表
    current_path = []
    
    def traverse_and_write(node: TreeNode, depth=0):
        nonlocal current_path  # 使用外部函数的变量
        
        # 构建路径
        if node.title.startswith('-'):
            current_path.append(node.title[1:])
        else:
            row_num = sheet.max_row + 1  # 获取当前应写入的行号
            sheet.cell(row=row_num, column=1).value = "-".join(current_path)
            sheet.cell(row=row_num, column=2).value = node.title
            sheet.cell(row=row_num, column=3).value = node.step
            sheet.cell(row=row_num, column=4).value = node.result
        
        # 遍历子节点
        for child in node.children:
            traverse_and_write(child, depth + 1)
        
        # 当完成当前节点及其子节点的处理后，从路径中删除该节点（如果它是一个文件夹）
        if node.title.startswith('-'):
            current_path.pop()

    traverse_and_write(root)
    workbook.save(output_file)