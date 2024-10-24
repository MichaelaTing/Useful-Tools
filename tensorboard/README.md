# Tensorboard 教程

```shell
pip install tensorboard
```

## 启动 TensorBoard

### 本地启动

```shell
tensorboard --logdir='./logs' --bind_all # 打开 http://localhost:6006/ 查看
```

### 在 Jupyter Notebooks 中使用 TensorBoard

```jupyter-notebook
%load_ext tensorboard
%tensorboard --logdir logs
```

### 远程运行 TensorBoard

```shell
ssh -L 6006:127.0.0.1:6006 username@server_ip # 使用SSH将远程服务器的端口映射到本地的计算机
tensorboard --logdir='./logs' --port=6006 # 远程服务器上运行
```

## TensorBoard 仪表板

- Scalars: 跟踪与模型性能相关的指标，确定模型是否过度拟合
- Images: 处理图像数据时
- Graphs: 模型结构
- Distributions and Histograms: 分布和直方图
- TEXT: 可视化文本数据
- Projector: 可视化高维数据
