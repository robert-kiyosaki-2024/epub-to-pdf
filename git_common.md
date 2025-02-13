
## Git 常用命令

### 基础配置
```bash
# 配置用户信息
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱"

# 生成 SSH 密钥
ssh-keygen -t rsa -C "你的邮箱"
```

### 仓库操作
```bash
# 初始化仓库
git init

# 克隆仓库
git clone <仓库地址>

# 添加远程仓库
git remote add origin <仓库地址>

git remote add origin git@github-personal-robert:robert-kiyosaki-2024/epub-to-pdf.git
```

### 日常操作
```bash
# 查看状态
git status

# 添加文件到暂存区
git add .                    # 添加所有文件
git add <文件名>             # 添加指定文件

# 提交更改
git commit -m "提交说明"

# 拉取更新
git pull origin <分支名>

# 推送更改
git push origin <分支名>
```

### 分支操作
```bash
# 查看分支
git branch

# 创建分支
git branch <分支名>

# 切换分支
git checkout <分支名>

# 创建并切换分支
git checkout -b <分支名>

# 合并分支
git merge <分支名>

# 删除分支
git branch -d <分支名>
```

### 其他常用命令
```bash
# 查看提交历史
git log

# 撤销修改
git checkout -- <文件名>     # 撤销工作区的修改
git reset HEAD <文件名>      # 撤销暂存区的修改

# 查看远程仓库信息
git remote -v

# 标签管理
git tag <标签名>             # 创建标签
git tag -d <标签名>          # 删除标签
```

### 分支管理
```bash
# 查看分支
git branch

# 创建分支
git branch <分支名>

# 切换分支
git checkout <分支名>   

# 合并分支
git merge <分支名>

# 删除分支
git branch -d <分支名>  

# 查看分支合并状态
git branch --merged

# 查看未合并的分支
git branch --no-merged  

# 查看分支合并图
git log --graph --oneline --all

# 查看分支合并历史
git log --oneline --decorate --graph    

# 查看分支合并历史
git log --oneline --decorate --graph    

# 查看分支合并历史
git log --oneline --decorate --graph    



