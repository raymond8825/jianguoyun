# 0 git 工作区(work)-暂存区（stage）-仓库(responsity)三个区的总结
Git管理的文件分为：工作区，版本库，版本库又分为暂存区stage和暂存区分支master(仓库)

工作区>>>>暂存区>>>>仓库

git add把文件从工作区>>>>暂存区，git commit把文件从暂存区>>>>仓库，

git diff查看工作区和暂存区差异，

git diff --cached查看暂存区和仓库差异，

git diff HEAD 查看工作区和仓库的差异，

git add的反向命令git checkout，撤销工作区修改，即把暂存区最新版本转移到工作区，

git commit的反向命令git reset HEAD，就是把仓库最新版本转移到暂存区。

# 1. 版本回退(在本地仓库中的版本中切换)
无论是前进还是回退版本，都只是用`git reset --hard`+`commit版本号`来到达想要的版本，因为git内部有个HEAD的指针指向当前工作区的版本号，我们只需要告诉git我们想去的版本号，HEAD就会指向该版本，并将我们的工作区改为该版本。如果我们找不到commit的版本号，我们可以使用`git reflog`来看之前执行的所有git命令。
# 2. 撤销工作区修改
如果我们在工作区域做了一些修改，比如说是`readme.txt`，但是现在不想要了，此时分为两种情况
- 一种是readme.txt自修改后还没有被放到暂存区，现在，撤销修改就回到和版本库一模一样的状态；
- 一种是readme.txt已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态。

第一种情况是我们修改文件`readme.txt`后，并没有将文件add进入暂存区，但是现在我们想丢弃工作区的修改，我们使用`git checkout -- readme.txt`即可丢弃工作区修改，回到和版本库一样（和暂存区也是一样，因为我们从来没有add文件）

第二种情况是我们修改文件`readme.txt`后，有过一次将文件add进入暂存区，在这之后我们又再次修改文件，但是这次没有add进入暂存区，我们使用`git checkout -- readme.txt`即可丢弃工作区修改回到跟暂存区一样。

总结：感觉两种情况都可以归为checkout是将工作区文件恢复到和当前暂存区域一样。
# 3. 把暂存区的修改撤销掉，重新放回工作区
> 这里`git reset HEAD`和`git reset --hard HEAD`的不同是：如果`git reset HEAD`是将暂存区更新为最新的版本库中的版本，但是工作区中做的修改会保留，而`git reset --hard
`git reset HEAD readme.txt`这里的reset就是commit的反向命令，就是将HEAD指向的版本库直接赋值给暂存区，但是工作区之前所做的修改依然保留在工作区，处于等待add的状态。
# 4. 删除分支
`git branch -d dev`
# 5. merge时候是否提交commit
当我们提交是git采用`fast-forward`即为ff的时候，git不会为我们自动commit，我们也无法commit，此后不利于我们代码回滚。所以在git自动为我们ff的时候我们应该禁止使用自动merge。使用`git merge --no-ff -m "merge with no-ff" dev`,这个命令后面必须使用`-m`参数，否则git会自动让你在一个文本中输入commit。合并分支时，加上--no-ff参数就可以用普通模式合并，合并后的历史有分支，能看出来曾经做过合并，而fast forward合并就看不出来曾经做过合并。
# 5.1 使用merge的注意事项
-  如果在dev分支上使用`git merge master`命令，那么合并结果则会在dev分支上，而master分支上的结果保持不变。
# 6. 使用git stash 命令
当我们需要临时存储自己的工作区区别的分支上干活的时候（比如去bug分支上修改bug），此时我们可以使用`git stash`命令将我们的工作区暂存起来，此时工作区就是干净的，我们就可以切换分支。我们可以stash多个暂存空间存储我们的工作区，git会为多个stash创建不同的编号（index:0,1,2,3...）,`git stash list`来看一下我们所有的工作区。使用`git stash apply stash@{index}`来恢复我们想要的工作区。apply命令虽然恢复了工作区，但是stash起来的内容并没有删除，我们可以使用`git stash drop stash@{index}`来删除我们不想保留的stash。当然我们也可以一步到位，使用`git stash pop stash@{index}`,既恢复了我们的工作区，同时还删除了不必要的stash。
# 7. feature特性分支
当我们开发新的特性的时候，不想因为一些实验性代码搞乱我们原来的代码，我们可以建立一个feature分支，类似与改bug分支。如果我们在开发分支时被叫停，我们应该使用`git branch -d feature1`发现git提醒说`由于分支没有合并，无法删除`,此时我们可以使用`git branch -D feature1`
# 8. 下拉代码冲突问题
1.在本地修改与远程代码无冲突的情况下，优先使用：pull->commit->push
2.在本地修改与远程代码有冲突的情况下，优先使用：commit->pull->push
# 9. 查看当前工作区的远程仓库的地址
- `git remote -v`
- `git remote show origin`:给出的信息比上面的git remote -v还详细
- `git branch -avv`:显示每个分支的对应的远端仓库的地址信息
# 10. 查看当前git的用户和邮箱，并更改用户及邮箱
> 查看当前用户
- `git config user.name`:显示当前git的用户名
- `git config user.email`:显示当前git的用户的邮箱
> 更改用户
`git config --global user.name "Your_username"`:更改用户名
`git config --global user.email "Your_email"`：更改用户邮箱

# 11. 如果commit在push后才发现新版本（版本四）出错，如何更改
1. 首先使用`git reset --hard 版本三的版本号`或者`git reset --soft 版本三的版本号`回退到上一个版本；
2. 在本地做好修改之后，在使用`git add .`或者`git commit -m " "`正常commit，此时使用`git status`或者`git push`都会提示你本地仓库和远程仓库变成了两个分支，无视之
3. 使用`git push --force`强制push，就可以删除错误版本四的commit，变成修改后正确的版本四commit

# 12. 当完成自己的任务需要提交的时候
1. 首先进行`git add . & git commit -m "commitments"`
2. 然后进行`git pull --rebase`
3. 进行去冲突操作
4. `git add .`
5. `git rebase --continue`
6. `git push`

# 删除命令
## 1.对于从本地直接将某个文件或者某个目录删除后，想要远程库中也要对应删除文件或者目录
1. 第一步：`rm [-r] 目录/文件名`
2. 第二步：`git rm [-r] 目录/文件名`或者`git add .`
3. 第三步：`git commit -m "说明"`
4. 第四步：`git push`

删除文件不同于普通的修改，不用add--->commit--->push。(使用这个顺序也没有错误，甚至减少记忆压力)
# 8. git clone
`git clone`会从云端仓库克隆所有文件到本地，但是使用`git branch`查看分支时发现，只有`master`分支，并没有其他分支（如dev），这是因为我们虽然从云端clone了一份完成的仓库，但是我们在本地并没有对应云端的分支dev，我们使用`git branch dev`创建dev分支，然后使用`git checkout dev`切换到dev分支，然后就可以使用了（不用pull吗？）
# 9. git clone 和 git pull
简单理解，`git clone`是从远程库中复制整个版本库到本地，是一个本地从无到有的过程，包含了所有的分支和版本。使用`git branch`命令只能看到`master`一个分支，要手动使用`git checkout 分支名`切换到对应分支。`git pull`则是从远程库中更新本地的仓库，详细使用尚未接触到。
# 10. git pull --rebase的使用
csdn收藏
最总要的是：
- 永远不要使用`git rebase --skip`
- 在`git pull --rebase`出现冲突后，先去解决冲突，然后使用`git add .`,最后在使用`git rebase --continue`,最后再`git push`
# 11. git merge的注意事项
自己开发的内容在commit之后，需要使用`git pull --rebase`下拉最新的代码，但是千万不要直接把原来的旧HEAD的文件全部删除，因为这个是刚刚`git pull`下来的，可能有别人最新的代码，所以应该根据`git log`中小心删除。
# 12. git如何在本地创建分支并同步到远端
> 使用场景：本地新建了一个分支wechat，但是远端仓库没有该分支，而且需要同步到远端仓库
- 首先使用`git checkout -b wechat`,创建并切换到wechat，以防止忘记切换分支，而在原来的分支上瞎操作
- 我们可以使用`git branch -vv`查看所有分支与远程仓库的绑定情况，我们会发现我们新建的分支没有绑定任何远程分支
- 如果我们新建的分支不是最新的代码，需要更新远程dev分支的最新代码,但是我们的wechat分支有没有绑定远程分支，我们可以在wechat分支上使用`git pull --rebase origin dev`来将最新的代码下拉到自己的wechat本地分支上。（如何处理冲突，上面有介绍）
- 然后直接使用`git push origin wechat`来把本地分支推送到远程仓库的wechat分支，如果远程仓库没有wechat分支，则会自动创建wechat分支
- 推送完还需要为本地的wechat分支和远程仓库的wecaht分支<font color="red">建立绑定关系</font>，使用`git branch --set-upstream-to=origin/wechat`，之后就可以直接使用`git pull`和`git push`来直接拉推代码。
- 此时我们使用`git branch -vv`来查看所有分支与远程分支的绑定关系，发现新建的分支已经绑定。
- 如第三步所示，<font color="red">在没有wechat没有绑定远程仓库之前</font>我们可以通过`git pull/push origin dev`来推拉别的分支的代码