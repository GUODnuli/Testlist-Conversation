import xmind
import os
current_directory = os.getcwd()
xmind_file_path = current_directory + "\examples\example1.xmind"
workbook = xmind.load(xmind_file_path)
print(workbook.getData())
print(workbook.to_prettify_json())