# DRIVE数据集

# 安装依赖库

```
pip install -r requirements.txt
```



# 训练

LiteSeg文件夹下命令行执行
```
python train.py --backbone_network mobilenet
```



# 测试

LiteSeg文件夹下命令行执行
```
python test.py --backbone_network mobilenet
```


**backbone_network可选择mobilenet/darknet/shufflenet