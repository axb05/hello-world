# hello-world
project for test
Add form the brower。

修改分支2中的文件。

20190305 22:16
add for test

20190311
上传ballgame的python程序，学习git的功能。
开始没有配置igore文件，uenv和__pycache__两个目录也上传了，如何删除托管代码中的目录？

在github上只能删除仓库,却无法删除文件夹或文件, 所以只能通过命令来解决
首先进入你的master文件夹下, Git Bash Here ,打开命令窗口

$ git pull origin master                    # 将远程仓库里面的项目拉下来
$ dir                                                # 查看有哪些文件夹
$ git rm -r --cached target              # 删除target文件夹
$ git commit -m '删除了target'        # 提交,添加操作说明
$ git push -u origin master               # 将本次更改更新到github项目上去

操作完成.

注:本地项目中的target文件夹不收操作影响,删除的只是远程仓库中的target, 可放心删除

每次增加文件或删除文件，都要commit 然后直接 git push -u origin master，就可以同步到github上了
--------------------- 
