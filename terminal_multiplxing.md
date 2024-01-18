# 终端复用

## tmux

```shell
tmux new -s <session_name> # 新建窗体
tmux ls # 显示窗体
tmux attach -t <session_name> # 由终端进入之前创建的窗体
tmux kill-session -t <session_name> # 删除窗体
```

## screen

```shell
screen -S <session_name> # 创建会话
screen -ls # 显示会话
screen -r <session_name> # 指定会话
screen -d <session_name> # 脱离会话
```