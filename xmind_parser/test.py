import xmind
import os
current_directory = os.getcwd()
xmind_file_path = current_directory + "\examples\example.xmind"
workbook = xmind.load(xmind_file_path)

print(workbook.getData()[0]["topics"])