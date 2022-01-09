单行道上的红绿灯不用标traffic_singal:direction=*，如果标了是不对的，此外它不可在交叉点有但本处不管只管单行。

思路一是overpass到所有红绿灯点，然后检查它所在的线是不是单行。但是问题是点不包含父层次路径的数据，因此就需要对全图中所有way都检查一下是否node在它上边。

写出伪代码是（不一定最后这么定义，然后fatherWay可以是一个列表因为可能位于一条路一条其他东西的交点上）

```python
if node[traffic_singal:direction].fatherWay[all].[oneway=yes]:
    node[traffic_singal:direction].(del)[traffic_singal:direction]
```

但是查询量很大，如果全都走API化的话

因此提出第二种思路，对全图中每一条线段遍历看是不是highway，是再看是不是oneway，如果是再看包含不包含红绿灯，如果包含那么上面的红绿灯全都去方向标签。缺点是必须提前下载好全量数据。

```python
for way[i] in map:
    if way[i].[highway=*]:
        if way[i].[oneway=yes]:
            for node[j] in way[i]:
                if node[j].[traffic_singal:direction=*]:
                    node[j].(del)[traffic_singal:direction]
```