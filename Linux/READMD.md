# Linux 基本操作

## `cd` 指令

- 返回上一级目录 `cd ..`
- 返回刚刚所在的目录 `cd -`
- 去往 Home `cd ~`

## `ls` 指令

- 输出详细信息 `ls -l` (long)
- 显示所有文件 `ls -a` (all) 这里还会显示隐藏的文件(以 `.` 开头的)
- 方便给人观看的详细信息 `ls -lh` (human)
- 查看其他功能 `ls --help`

## `touch` 指令

- 建立(多个)空文件 `touch file3 file4 file5`

## `cp` 指令

- 复制老文件到新文件 `cp file1 file1copy`
- 上述命令将会直接覆盖已存在的 file1copy，要避免直接覆盖，在后面加一个选项 `cp -i file1 file1copy` (interactive) 将输出 `cp: overwrite 'file1copy'?`
- 复制文件到文件夹 `cp file1 folder1/`
- 复制文件夹 `cp -R folder1/ folder2/` (recursive)
- 复制名字部分相同的多个文件( `*` 意思是找名字前面是 file 的所有文件) `cp file* folder2/`
- 复制多个文件，可以单独选定几个文件，默认最后一个选项是要复制去的文件夹 `cp file1copy file2 folder1/`

## `mv` 指令

- 移动去另一个文件夹 `mv file1 folder1/`
- 重命名文件 `mv file1 file1rename`

## `mkdir` 指令

- 创建文件夹 `mkdir folder2`

## `rmdir` 指令

- 移除文件夹，不过要移除的文件夹必须是空的 `rmdir folder3`

## `rm` 指令

- 适用于文件夹里有文件或者移除单个文件的情况，注意，执行 `rm`后是不能进行返回操作的，请确保别执行像这样的操作 `rm /`，这会清空你的电脑.
- 移除单个文件 `rm file1`

-`-i` 或 `-I` 有提示地移除文件(为了避免误删): `-i` 每个要移除的文件都进行提示；`-I` 超过3个文件才进行提示 `rm -i f1 f2 f3 f4` ; `rm -I f1 f2 f3 f4`

-`-r` 或 `-R` (recursively) 删文件夹 `rm -r folder1` 可以在文件夹中有文件的情况下删除这个文件夹

## `nano` 指令

- 做基本的终端的文本编辑 `nano t.py`

## `cat` 指令

- 查看文件内容 `cat t.py`

-`>` 将文件的内容放到另一个文件里 `cat t.py > t1.py`

-`>` 将多个文件的内容打包一起放入另一个文件 `cat t.py t1.py > t2.py`

-`>>` 将内容添加在一个文件末尾 `cat t3.py >> t2.py`远程操控

-`sudo apt-get install openssh-server`

-`sudo apt install net-tools`

-`ifconfig`

- ssh报错可以尝试 `ssh-keygen -R [ip]`
- 创建公钥和私钥 `ssh-keygen` 可以一路 Enter
- 将公钥复制到被控制的 Linux `ssh-copy-id [username]@[ip]`

## 文件权限

-`drwxrw-rw-` 第一个 `d`代表Type，`-`为文件，`d`为文件夹，后面分别代表User，Group，Others，其中r，w，x分别代表read，write，execute

-`chmod [谁][怎么修改] [哪个文件]`

-`[谁]` u：对于 User 修改；g：对于 Group 修改；o：对于 Others 修改；a：对于所有人修改

-`[怎么修改]` +，-，=：作用的形式，加上，减掉，等于某些权限；r，w，x 或者多个权限一起，比如 rx

- 现在的文件权限是 `----rw-r--`，如果想让 User 有读的能力：`chmod u+r t1.py` 这里 `u+r`代表 User + read
- 如果没有 x 权限，在终端中需要这样执行 `python3 t.py`，如果有 x 可执行权限，可以直接 `./t.py`，在这个 Python 脚本的开头还需要加上 `#!/usr/bin/python3`
