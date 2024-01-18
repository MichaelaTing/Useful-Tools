# Git 教程

## 配置

```shell
git config --global user.name xxx
git config --global user.email xxx
git config --global user.password xxx # 这里可以通过 "Github/Settings/Developer Settings" 设置token
git config --global http.proxy xxx.xxx.xxx.xxx:zz # 代理服务器地址: 代理服务器端口号
git config --list # 查看上述信息
git config --global --edit # 编辑
git config --global credential.helper store # 避免每次git clone重复输入用户名和密码
```

## 利用 SSH 完成 Git 与 GitHub 的绑定

```shell
ssh-keygen -t rsa # 生成公钥和私钥
cd ~/.ssh
cat id_rsa.pub # 将 ~/.ssh 文件夹中的公钥 id_rsa.pub 的内容添加到 “GitHub/Settings/SSH”
ssh -T git@github.com # 测试是否绑定成功，若端口22失败，则使用端口443，在 ~/.ssh/config 中添加 
" 
Host github.com 
    Hostname ssh.github.com 
    Port 443 
"
```

## 创建仓库

### 初始化仓库

```shell
mkdir foldname # 创建文件夹
cd foldname/
git init # 当执行 git init 的时候，默认情况下 Git 就会创建 master/main 分支。
ls -a
```

### 拷贝远程仓库

```shell
git clone [url]
```

## 提交与修改

### 添加文件到暂存区

文件修改后，一般都需要进行 `git add` 操作，从而保存历史版本。

```shell
touch filename # 创建文件
git add <file1> <file2>
git add . # 一次性添加文件夹中所有未被添加的文件
```

### 查看仓库当前的状态，显示有变更的文件

```shell
git status # 查看版本库的状态
git status -s # 缩写模式
```

### 提交暂存区到本地仓库

```shell
git commit -m [message]
git commit <file1> <file2> ... -m [message]
git commit -a # 修改文件后不需要执行 git add，直接提交
```

### 比较暂存区和工作区的差异

```shell
git diff # 尚未缓存的改动
git diff --cached # 查看已缓存的改动
git diff HEAD # 查看已缓存的与未缓存的所有改动
git diff --stat # 显示摘要而非整个 diff
```

### 回退版本

```shell
git reset [--soft | --mixed | --hard] [HEAD] # --soft 用于回退到某个版本，--hard 撤销工作区中所有未提交的修改内容，将暂存区与工作区都回到上一次版本，删除之前的所有信息，谨慎使用，--mixed 为默认，可以不用带该参数，HEAD^[n] 表示往前 n 个版本
```

### 将文件从暂存区和工作区中删除

```shell
git rm <file> # 将文件从暂存区和工作区中删除
git rm -r <fold> # 删除本地文件夹
git rm --cached <file> # 仅从暂存区中移除
git rm –r * # 递归删除整个目录中的所有子目录和文件
```
 
### 移动或重命名工作区文件

```shell
git mv <file> <newfile> # 移动或重命名一个文件、目录
git mv -f <file> <newfile> # 新文件名已经存在，但还是要重命名它
```

### 标签

```shell
git tag -a v1.0 
git tag # 查看所有标签
```

### 查看历史提交记录

```shell
git log # 查看历史提交记录
git log --oneline # 查看历史记录的简洁版本
git log --oneline --graph # 开启拓扑图选项
git log --reverse --oneline # 逆向显示日志
git log --decorate ## 查看标签
git log --help # 查看帮助命令
git blame <file> # 以列表形式查看指定文件的历史修改记录。
```

## 分支管理
几乎每一种版本控制系统都以某种形式支持分支，一个分支代表一条独立的开发线。

使用分支意味着你可以从开发主线上分离开来，然后在不影响主线的同时继续工作。

有人把 Git 的分支模型称为必杀技特性，而正是因为它，将 Git 从版本控制系统家族里区分出来。

在分支中增加、删除文件不影响主分支。使用分支将工作切分开来，从而让我们能够在不同开发环境中做事，并来回切换。

### 分支

```shell
git branch # 查看 Git 仓库的分支情况
git branch -a # 查看远程仓库的分支情况
git log --oneline --graph # 观看分支
git branch <newbranch> # 建立分支
git branch -d <newbranch> # 删除本地分支
git push origin --delete <newbranch> # 删除远程分支
```

### 分支切换

```shell
git checkout <branch>
git checkout -b <newbranch> # 直接创建和切换到新建的分支
git checkout - # 快速切换回前一个分支
git checkout -- <file> # 将指定文件恢复到最新的提交状态，丢弃所有未提交的更改，对于撤销不需要的更改非常有用
git checkout tags/<tagname> # 切换到标签指向的提交状态
```

### 分支合并
如果有冲突，则不能直接合并，需要先手动解决冲突

```shell
git merge <branch>
git merge --no-ff -m "keep merge info" <branch> # --no-ff 禁止快进式合并，通常主分支存放的都是稳定的代码，提交频率很低，而分支是用来开发特性的，上面会存在许多零碎的提交，快进式合并会把分支的提交历史混入到主分支中，搅乱主分支的提交历史。
```

## 远程操作

### 远程仓库操作

```shell
git remote # 列出当前仓库中已配置的远程仓库
git remote -v # 列出当前仓库中已配置的远程仓库，并显示它们的 URL
git remote show <remote_name> # 显示指定远程仓库的详细信息
git remote add <remote_name> <remote_url> # 指定一个远程仓库的名称和 URL，将其添加到当前仓库中
git remote rename <old_name> <new_name> # 将已配置的远程仓库重命名
git remote set-url <remote_name> <new_url> # 修改指定远程仓库的 URL
git remote remove <remote_name> # 从当前仓库中删除指定的远程仓库
git remote rm <remote_name>  # 删除远程仓库

```

### 从远程获取代码库

```shell
git fetch origin # 提取更新的数据
git merge origin/master # 将更新同步到本地
```

### 下载远程代码并合并

```shell
git pull <远程主机名> <远程分支名>:<本地分支名>
git pull origin master # 取回 origin 的 master 分支，与本地的 master 分支合并
git pull origin master:brantest # 取回 origin 的 master 分支，与本地的 brantest 分支合并。
```

### 上传远程代码并合并

```shell
git push <远程主机名> <本地分支名>:<远程分支名>
git push origin master # 将本地的 master 分支推送到 origin 主机的 master 分支
git push --force origin master # 本地版本与远程版本有差异，但又要强制推送
git push origin --delete master # 删除 origin 主机的 master 分支
```
