# -worknote
note that work for huanongtianshi
take a note



# Git常用命令
常用 Git 命令总结



下面是常用 Git 命令清单。几个专用名词的译名如下。
Workspace：工作区
Index / Stage：暂存区
Repository：仓库区（或本地仓库）
Remote：远程仓库
## 一、新建代码库

### 在当前目录新建一个Git代码库
```
1 $ git init
```
### 新建一个目录，将其初始化为Git代码库
```
1 $ git init [project-name]
```
### 下载一个项目和它的整个代码历史
```
 1 $ git clone [project-path]
```
## 二、配置

　　Git的设置文件为.gitconfig，它可以在用户主目录下（全局配置），也可以在项目目录下（项目配置）。
### 显示当前的Git配置
```
1 $ git config --list
```
### 编辑Git配置文件
```
1 $ git config -e [--global]
```
### 设置提交代码时的用户信息
```
1 $ git config [--global] user.name "[name]"
2 $ git config [--global] user.email "[email address]"
```
## 三、增加/删除文件

### 添加指定文件到暂存区
```
1 $ git add [file1] [file2] ...
```
### 添加指定目录到暂存区，包括子目录
```
1 $ git add [dir]
```
### 添加当前目录的所有文件到暂存区
```
1 $ git add .
```
### 删除工作区文件，并且将这次删除放入暂存区
```
1 $ git rm [file1] [file2] ...
```
### 停止追踪指定文件，但该文件会保留在工作区
```
1 $ git rm --cached [file]
```
### 改名文件，并且将这个改名放入暂存区
```
1 $ git mv [file-original] [file-renamed]
```
## 四、代码提交

### 提交暂存区到仓库区
```
1 $ git commit -m [message]
```
### 提交暂存区的指定文件到仓库区
```
1$ git commit [file1] [file2] ... -m [message]
```
### 提交工作区自上次commit之后的变化，直接到仓库区
```
1 $ git commit -a
```
### 提交时显示所有diff信息
```
1 $ git commit -v
```
### 使用一次新的commit，替代上一次提交
### 如果代码没有任何新变化，则用来改写上一次commit的提交信息
```
1 $ git commit --amend -m [message]
```
### 重做上一次commit，并包括指定文件的新变化
```
1 $ git commit --amend   ...
```
## 五、分支

### 列出所有本地分支
```
1 $ git branch
```
### 列出所有远程分支
```
1 $ git branch -r
```
### 列出所有本地分支和远程分支
```
1 $ git branch -a
```
### 新建一个分支，但依然停留在当前分支
```
1 $ git branch [branch-name]
```
### 新建一个分支，并切换到该分支
```
1 $ git checkout -b [branch]
```
### 新建一个分支，指向指定commit
```
1 $ git branch [branch] [commit]
```
### 新建一个分支，与指定的远程分支建立追踪关系
```
1 $ git branch --track [branch] [remote-branch]
```
### 切换到指定分支，并更新工作区
```
1 $ git checkout [branch-name]
```
### 建立追踪关系，在现有分支与指定的远程分支之间
```
1 $ git branch --set-upstream [branch] [remote-branch]
```
### 合并指定分支到当前分支
```
1 $ git merge [branch]
```
### 选择一个commit，合并进当前分支
```
1 $ git cherry-pick [commit]
```
### 删除分支
```
1 $ git branch -d [branch-name]
```
### 删除远程分支
```
1 $ git push origin --delete 
2 $ git branch -dr
```
## 六、标签

### 列出所有tag
```
1 $ git tag
```
###### 新建一个tag在当前commit
```
1 $ git tag [tag]
```
### 新建一个tag在指定commit
```
1 $ git tag [tag] [commit]
```
### 查看tag信息
```
1 $ git show [tag]
```
### 提交指定tag
```
1 $ git push [remote] [tag]
```
### 提交所有tag
```
1 $ git push [remote] --tags
```
### 新建一个分支，指向某个tag
```
1 $ git checkout -b [branch] [tag]
```
## 七、查看信息

### 显示有变更的文件
```
1 $ git status
```
### 显示当前分支的版本历史
```
1 $ git log
```
### 显示commit历史，以及每次commit发生变更的文件
```
1 $ git log --stat
```
### 显示某个文件的版本历史，包括文件改名
```
1 $ git log --follow [file]
2 $ git whatchanged [file]
```
### 显示指定文件相关的每一次diff
```
1 $ git log -p [file]
```
### 显示指定文件是什么人在什么时间修改过
```
1 $ git blame [file]
```
### 显示暂存区和工作区的差异
```
1 $ git diff
```
### 显示暂存区和上一个commit的差异
```
1 $ git diff --cached []
```
### 显示工作区与当前分支最新commit之间的差异
```
1 $ git diff HEAD
```
### 显示两次提交之间的差异
```
1 $ git diff [first-branch]...[second-branch]
```
### 显示某次提交的元数据和内容变化
```
1 $ git show [commit]
```
### 显示某次提交发生变化的文件
```
1 $ git show --name-only [commit]
```
### 显示某次提交时，某个文件的内容
```
1 $ git show [commit]:[filename]
```
### 显示当前分支的最近几次提交
```
1 $ git reflog
```
## 八、远程同步

### 下载远程仓库的所有变动
```
1 $ git fetch [remote]
```
### 显示所有远程仓库
```
1 $ git remote -v
```
### 显示某个远程仓库的信息
```
1 $ git remote show [remote]
```
### 增加一个新的远程仓库，并命名
```
1 $ git remote add [shortname] [url]
```
### 取回远程仓库的变化，并与本地分支合并
```
1 $ git pull [remote] [branch]
```
### 上传本地指定分支到远程仓库
```
1 $ git push [remote] [branch]
```
### 强行推送当前分支到远程仓库，即使有冲突
```
1 $ git push [remote] --force
```
### 推送所有分支到远程仓库
```
1 $ git push [remote] --all
```
## 九、撤销

### 恢复暂存区的指定文件到工作区
```
1 $ git checkout [file]
```
### 恢复某个commit的指定文件到工作区
```
1 $ git checkout [commit] [file]
```
### 恢复上一个commit的所有文件到工作区
```
1 $ git checkout .
```
### 重置暂存区的指定文件，与上一次commit保持一致，但工作区不变
```
1 $ git reset [file]
```
### 重置暂存区与工作区，与上一次commit保持一致
```
1 $ git reset --hard
```
### 重置当前分支的指针为指定commit，同时重置暂存区，但工作区不变
```
1 $ git reset [commit]
```
### 重置当前分支的HEAD为指定commit，同时重置暂存区和工作区，与指定commit一致
```
1 $ git reset --hard [commit]
```
### 重置当前HEAD为指定commit，但保持暂存区和工作区不变
```
1 $ git reset --keep [commit]
```
### 新建一个commit，用来撤销指定commit
### 后者的所有变化都将被前者抵消，并且应用到当前分支
```
1 $ git revert [commit]
```
## 十、其他

### 生成一个可供发布的压缩包
```
1 $ git archive
```

# time, datetime处理时间转换
## 字符串格式转时间格式----string > datetime/time
```
1 from datetime import datetime
2 end_time = datetime.strptime('2017-03-03 20:30:57','%Y-%m-%d %H:%M:%S') 
  #参数一为字符串格式时间，参数二为字符串时间格式
3 import time
4 end_time = time.strptime('20170101','%Y%m%d')
 # 参数一为字符串格式时间，参数二为字符串时间格式
```
## 时间格式转字符串格式----datetime/time > string
```
1 from datetime import datetime
2 end_time = datetime.now().strftime('%Y%m%d%H%M%S')
  # datetime.now()获取当前时间，strftime()是转换成字符串操作，参数为转换后的格式
3 import time
4 end_time = time.strftime('%Y-%m-%d %w %H:%M:%S')
  #time.strftime()获取当前时间并按strftime的参数转换成字符串格式
5 time = time.time()
6 end_time = time strftime('%Y%m%d',time)
  #把给定的时间转换成固定格式的字符串
  
```
## 时间的天数操作
```获取昨天的时间
1 myTime = time.strftime('%Y%m%d',time.localtime(time.time() - 24*60*60) )
2 d1 = datetime.datetime(2017,04,07)
3 d2 = datetime.datetime(2017,05,01)
4 day = (d1-d2).days # d1与d2的天数差
```
```
其本上常用的类有：datetime和timedelta两个。它们之间可以相互加减。
每个类都有一些方法和属性可以查看具体的值，如datetime可以查看：天数(day)，小时数(hour)，星期几(weekday())等;
timedelta可以查看：天数(days)，秒数(seconds)  
start_date = datetime.datetime()
mid_date = start_date + timedelta(days=7)
#mid_date 等于在start_date基础上加7天，要取过去的几天，可以用days=-7
```

# 列表中的字典排序
```
import operator
# django查询数据库
content = []
ret = MedOrgPrincipal.objects.filter(user_id=user_id, org_uuid=org_uuid).values()
for item in ret:
    cintent.append(item)
    
content.sort(key=operator.itemgetter('updated_at'), reverse=True)
print (content)
# content 按照每个字典中的updated_at键排序
```
# 求n的阶乘
```
from operator import mul
# mul(a,b) 表示a*b
total = reduce(mul,[x for x in range(1,n)],1)
# mul 表示方法,第二个参数为列表,最后以为默认到1结束
```
