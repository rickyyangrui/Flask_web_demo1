# 小型问答平台

## 简介

本项目是一个小型的论坛系统，采用Python + Flask + MySQL进行开发, 前端用的是bootstrap框架，界面比较的简单。 用户可以进行问答的发布、问答。主要的功能包括：注册、登录、首页界面、发布问答、查询问答、评论， 
头像显示。是我学习Flask时候的一个练手小项目。

## 使用方法
* 克隆项目到本地
```
git clone https://github.com/rickyyangrui/Flask_web_demo1
```

* 先创建一个虚拟环境，避免污染整个Python的环境。
```
pip install virtualenv
```
* 创建一个文件夹，名字：Virtualenv
```
mkdir Virtualenv
cd Virtualenv
```
* 创建一个虚拟环境 venv
```
virtualenv venv
```
* 激活虚拟环境（因为我在win上面搞的，这里启动环境的命令很蛋疼，我不喜欢用，我是直接进入到venv -> Scripts目录下，输入activate直接打开虚拟环境）
```
cd venv
cd Scripts
activate
```
* 不需要时候可以关闭
```
deactivate
```
不过假如我们有pycharm的话，那都不是事，创建环境小意思，Python程序员的利器，直接全部搞定。
* 安装我们所需要的各种包
```
pip install -r requirements.txt
```
* 假定大家都安装好了MySQL，我们去创建一个databases,在mysql命令行中输入：
```
create database you_database_name charset urf-8;
```
* 修改下我们的配置文件，config中的数据库配置。
```
SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/you_database_name'
```
* 使用Flask中强大的sqlalchemy -> Flask-Migrate；来实现数据库的迁移
```
python manage.py db init     # 创建迁移的仓库
Python manage.py db migrate  # 创建迁移的脚本
python manage.py db upgrade  # 更新数据库
```
* 在pycharm中直接启动platform程序，或者：
```
python manage.py runserver
```
* 最后，打开http://127.0.0.1:5000, 成功啦。

## 网站的截图
***登录的界面***
![Login](https://github.com/rickyyangrui/Flask_web_demo1/blob/master/screenshoots/Login.png)
***注册的界面***
![注册](https://github.com/rickyyangrui/Flask_web_demo1/blob/master/screenshoots/%E6%B3%A8%E5%86%8C.png)
***首页***
![首页](https://github.com/rickyyangrui/Flask_web_demo1/blob/master/screenshoots/%E9%A6%96%E9%A1%B5.png)
***发布问答***
![发布问答](https://github.com/rickyyangrui/Flask_web_demo1/blob/master/screenshoots/%E5%8F%91%E5%B8%83%E9%97%AE%E7%AD%94.png)
***评论***
![首页](https://github.com/rickyyangrui/Flask_web_demo1/blob/master/screenshoots/%E8%AF%84%E8%AE%BA.png)

