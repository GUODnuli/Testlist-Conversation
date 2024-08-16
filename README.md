# Xmind to excel tool

一个将Xmind文件转换至Excel文件的小工具

## 快速开始

1. `git clone`到本地目录,`cd Xmind_parser_project`。
2. 将要转换的Xmind文件放入input文件夹。
3. 使用任意文本编辑器打开`Testcase_config.json`并配置。
4. 使用Excel或WPS打开`tapd用例模板.xlsx`文件，另存一份并重命名为Xmind的文件名。
5. 命令行`cd`至该项目文件夹，执行`python main.py`。
6. 从output文件夹获取转换后的excel文件

ps：xmind的python包只能解析

### 输入文件夹

`/input`

### 输出文件夹

`/output`

### 配置文件

`/config/Testcase_config.json`
配置字段：

- 用例文件名，用于识别你需要转换的文件，当前仅限配置单个文件。
- 输出文件名，还未应用的配置，留空即可，现在的输出文件名就是用例文件名.xlsx。
- 模板文件名，填写你的excel模板文件名，不用带文件后缀。
- 根目录，当前tapd用例顶级目录为“所有的”，不用填写这一段，写你想保存的目录，每个子级使用“-”连接。示例：“通用平台-通用930”。
- 用例类型，无需修改。
- 用例状态，无需修改。
- 创建人，填写自己的名字。
- 需求ID，无需填写。
- 表头，无需填写。
- 用例目录识别符，需要在每个用例目录前加一个符号用作识别
