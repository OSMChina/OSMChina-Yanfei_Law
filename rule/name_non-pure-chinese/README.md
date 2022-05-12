本检查器作用

如果name中包含26个英文字母或者是拼音符号的话，就抛出异常（但是怎么断句需要人工处理，因此初期只能作为检查）

外置数据：

+ english.datalist
+ pinyin.datalist （数据来源：https://zh.wikipedia.org/wiki/%E6%B1%89%E8%AF%AD%E6%8B%BC%E9%9F%B3#Unicode%E8%BE%93%E5%85%A5%E7%A0%81%E4%BD%8D）（还可用作`name:en`中出现拼音字符的一对一替换）

以下也可考虑加入Non Pure Chinese检查

+ 未来引入：特殊符号
+ 未来引入：日文平假名片假名
+ 未来引入：法语、德语、西班牙语、葡萄牙语
+ 未来引入：韩语
+ 未来引入：西里尔字母、阿拉伯字母、希腊字母
