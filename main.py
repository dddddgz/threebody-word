import jieba
import wordcloud as cloud
import os
from rich.console import Console
from collections import Counter
jieba.setLogLevel(jieba.logging.INFO)

console = Console()
console.log("正在读取三体文件……")
with open("Threebody.txt", encoding="utf-8") as f:
    content = f.read()
console.log("三体文件读取完毕，正在分词……")
words = jieba.lcut(content)
console.log("分词完毕，正在过滤无效词语……")
words = [word for word in words if len(word) > 1]
console.log("无效词语过滤完毕，正在绘制词云图……")
wc = cloud.WordCloud(font_path="C:/Windows/Fonts/msyh.ttc",
              background_color="white")
wc.fit_words(dict(Counter(words)))
wc.to_file("result.png")
console.log("词云图绘制完成，正在打开图片……")
os.system(os.path.join(os.getcwd(), "result.png"))
console.log("图片打开完毕。祝您有愉快的一天！")
