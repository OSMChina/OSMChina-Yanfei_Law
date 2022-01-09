from keqing_sword.kqs_class import PyOsm

# 从.osm文件加载PyOsm对象
pyosm = PyOsm()
pyosm.from_file('./demo.osm')

# 遍历所有点
for node in pyosm.node_dict.values():
    # 跳过无name或有name:zh标签的点
    if 'name' not in node.tags or 'name:zh' in node.tags:
        continue

    # 获取name，并设置name:zh
    name = node.tags['name']
    node.tags['name:zh'] = name

    # 如果修改前后的标签有差异，则打印差异，并标记为已修改
    if node.has_diff():
        node.print_diff()
        node.action = 'modify'

# 写到.osm文件
pyosm.write('../demo_changed.osm')