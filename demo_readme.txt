demo_.... 的用法

1 处理的是 www.biquge.tw 的小说
2 demo_charpter.py 处理某一个章节页面，取出其中的正文。
    demo_charpter.html 是一个测试页面
3 demo_index.py 处理目录页
    demo_index.html 是一个测试页面
4 demo_textfilter.py 是整理章节的文本
    这里需要3个配置文件：
    demo_remove_ad_at_firstline.txt : 删除文件中出现一次的字符串和随后的空行。
    demo_remove_ad_at_tail.txt : 同上，删除文件末尾的。
    demo_remove_words.txt : 删除词汇，不含换行符。
5 用法
    1) demo_index.py 获取一个目录页
    2) demo_charpter.py 处理其中的一个页面，取得其中的文本。
    3) demo_textfilter.py 根据配置删掉多余的广告文字。