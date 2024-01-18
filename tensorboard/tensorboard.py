from torch.utils.tensorboard import SummaryWriter
import numpy as np
import torch, torchvision

def add_graph(writer):
    img = torch.rand([1, 3, 64, 64], dtype=torch.float32)
    model = torchvision.models.AlexNet(num_classes=10)
    # 可视化模型的网络结构图
    writer.add_graph(model, input_to_model=img) 
 
   
def add_scalars(writer):
    r = 5
    for i in range(100):
        # 在一张图中可以绘制多个曲线，只需要以字典的形式传入参数
        writer.add_scalars(main_tag='scalars1/P1', tag_scalar_dict={'xsinx': i * np.sin(i/r), 'xcosx': i * np.cos(i/r), 'tanx': np.tan(i/r)}, global_step=i)
        writer.add_scalars('scalars1/P2', {'xsinx': i * np.sin(i/(2*r)), 'xcosx': i * np.cos(i/(2*r)), 'tanx': np.tan(i/(2*r))}, global_step=i)
        writer.add_scalars(main_tag='scalars2/Q1', tag_scalar_dict={'xsinx': i * np.sin((2*i)/r), 'xcosx': i * np.cos((2*i)/r), 'tanx': np.tan((2*i)/r)}, global_step=i)
        writer.add_scalars('scalars2/Q2', {'xsinx': i * np.sin(i / (0.5*r)), 'xcosx': i * np.cos(i / (0.5*r)), 'tanx': np.tan(i / (0.5*r))}, global_step=i)


def add_histogram(writer):
    for i in range(10):
        x = np.random.random(1000)
        writer.add_histogram('distribution centers/p1', x + i, i)
        writer.add_histogram('distribution centers/p2', x + i * 2, i)
        
        
def add_pr_curve(writer):
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import label_binarize
    def get_dataset():
        from sklearn.datasets import load_iris
        from sklearn.model_selection import train_test_split
        x, y = load_iris(return_X_y=True)
        random_state = np.random.RandomState(2023)
        n_samples, n_features = x.shape
        # 为数据增加噪音维度以便更好观察pr曲线
        x = np.concatenate([x, random_state.randn(n_samples, 100 * n_features)], axis=1)
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=random_state)
        return x_train, x_test, y_train, y_test

    x_train, x_test, y_train, y_test = get_dataset()
    model = LogisticRegression(multi_class="ovr")
    model.fit(x_train, y_train)
    y_scores = model.predict_proba(x_test)  # shape: (n,3)
    b_y = label_binarize(y_test, classes=[0, 1, 2])  # shape: (n,3)
    for i in range(3): 
        # 在训练过程中可视化Precision-Recall曲线
        writer.add_pr_curve(f"pr_curve/label_{i}", b_y[:, i], y_scores[:, i], global_step=1)
        
        
if __name__ == '__main__':     
    writer = SummaryWriter(log_dir="logs/result_1", flush_secs=120)
    for n_iter in range(100):
        # 用来可视化网络训练时的各类标量参数，例如损失、学习率和准确率等
        writer.add_scalar(tag='Loss/train', scalar_value=np.random.random(), global_step=n_iter)
        writer.add_scalar('Loss/test', np.random.random(), n_iter)
    writer.close()
    
    writer = SummaryWriter(log_dir="logs/result_2")
    add_graph(writer)
    writer.close()
    
    writer = SummaryWriter(log_dir="logs/result_3")
    add_scalars(writer)
    writer.close()
    
    writer = SummaryWriter(log_dir="logs/result_4")
    add_histogram(writer)
    writer.close()
    
    writer = SummaryWriter(log_dir="logs/result_5")
    add_pr_curve(writer)
    writer.close()