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

## 思路分析
要做一个复杂的站点的时候，往往我们不知道如何入手，通常我们可以分解下，先做一个大概的模型，结构，分析一下我们要做的网页的结构都有什么？比如简书，知乎，微博等等，先做大体的结构，至于具体的功能可以慢慢的添加。

* 搭建好我们的项目骨架，项目启动的环境等等。

* 想好我们的界面是什么样子的，不知道的话，找个简单的站点看看，看看别人的整体样式，然后，去[bootstrap中文网](http://www.bootcss.com/),搜搜我们需要的样式，哈哈，可以直接复制，粘贴过来，当然有能力的可以直接自己写。

就比如知乎的样式：
![知乎](https://github.com/rickyyangrui/Flask_web_demo1/blob/master/screenshoots/%E7%9F%A5%E4%B9%8E.png)

我们可以看出，知乎的首页界面还是比较的简洁的，我们也可以做出来，只不过他有很多复杂的功能，我们可以先不做。首页由导航栏（知乎图标、首页、发现、话题、搜索、提问、通知、私信、用户信息），以及下面的内容组成。功能比我们自己做的多。

我们需要的就是去修改一下你Bootstrap中复制过来的内容，改成我们自己需要的，简化一下功能，通知，私信等等就不要了。

* 知乎上面点击首页，发现，话题等，导航栏会变，我们自己做的可以，简化一下，点击导航栏上面的东西，都是用同一个导航栏，这里就可以做父模板抽离，先做一个base模板，点击不用的button，显示不同的界面，我们只需要继承base模板，修改一下，做成不同的子模板。

* 然后做登录，注册，注销的样式。要实现登录和注册，先做好登录，注册的界面，然后我们还需要做一个User模型，也就是models.py模块，做好模型之后，把他映射到数据库的表之中，也就是我们的manage.py中，这里就涉及到数据库的SQLalchemy,做完之后，就可以完成登录，注册，注销的功能了。

* 接下来，我们就去做发布问答的界面，登录限制，发布问答的功能-> 首页布局 -> 首页功能 -> 问答详情界面 -> 评论 -> 查找。

* 总体的思路就是先做好界面，需要什么，我们就慢慢的添加，太难的做不出来，简单的还会没问题的。

这里推荐一本书《Flask Web开发：基于Python的Web应用开发实战》

