## 互联网新闻情感分析 Emotional Analysis of Internet News

### tra__emoAna
该文件夹保存的是传统算法实现的情感分析算法

### dl__emoAna
这里使用的是百度paddlepaddle开发的[ERNIE](https://github.com/PaddlePaddle/ERNIE)模型，
将情感分析模块单独拿出来使用。

0. 首先下载预训练[模型](https://baidu-nlp.bj.bcebos.com/ERNIE_stable-1.0.1.tar.gz) 
模型的路径为~model/~文件夹下，然后对模型进行解压~tar -zxvf ERNIE_stable-1.0.1.tar.gz~

0. 下载训练[数据](https://ernie.bj.bcebos.com/task_data_zh.tgz)
将数据直接解压到~dl__emoAna~目录下

0. 运行~bash run.sh~
