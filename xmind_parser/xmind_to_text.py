import xmind

def parse_xmind_to_text(input_file: str) -> list:
    # 加载XMind文件
    xmind_file = xmind.load(input_file)
    
    # 获取根节点（通常是第一个 sheet 的根节点）
    root_topic = xmind_file.getPrimarySheet().getRootTopic()
    
    # 递归解析并输出文本
    result = []
    parse_topic(root_topic, result, level=0)
    
    return result


def parse_topic(topic, result: list, level: int):
    # 将主题文本添加到结果列表
    result.append(f"{topic.getTitle()}")
    
    # 递归处理子主题
    for sub_topic in topic.getSubTopics():
        parse_topic(sub_topic, result, level + 1)