# OSMChina-Validator

规则中如果有node，way，relation共存同样内容的，可以用nwr表示

rule的mode如果是rule，就按照rule执行，否则作为单独的validator程序

执行完每个rule以后做diff是必须操作，不需要写在rule里面作为一个action

### 禁令

若发现存在标签为```process_with_robot```之类的东西，任何一个rule都不能在该元素上执行，但可以在其他元素执行

### 依赖

[Keqing_Sword](https://github.com/OSMChina/OSMChina-Keqing_Sword)

### 使用

需要安装前置依赖库，需要在本项目的根目录下运行：

```shell
pip install -r requirements.txt
```

默认源文件为`src.osm`，目标文件为`dst.osm`。将待处理的文件命名为`src.osm`放置到本工具相同目录，双击运行`branch_name_splitter`即可，处理结果为`dst.osm`。

本程序支持命令行代参启动，可选参数如下表

```
--src 源文件名，不加默认为src.osm 该功能尚未开发
--dst 输出文件名，不加默认为dst.osm 该功能尚未开发
--mode safe为仅检查不修正
--help 帮助
```

### 注意

仅适用于中国内地的简体中文地区。未特殊指明的均仅处理简体中文，指明了的没开发的也默认语言代码为zh

修改后请逐个人工检查修改结果！
