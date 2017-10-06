一、项目简介

本项目是一个小型的论坛系统，采用Python + Flask + MySQL进行开发, 前端用的是bootstrap框架，界面比较的简单。 用户可以进行问答的发布、问答。主要的功能包括：注册、登录、首页界面、发布问答、查询问答、评论。 头像显示。是我学习Flask时候的一个练手小项目。
二、如何运行本项目？

    1.先创建好一个本地的虚拟环境，并启动了虚拟环境，在虚拟环境下面打来本项目。推荐使用pycharm来 进行项目的开发。
    2.pip install -r requirements.txt 安装项目所需要的包。
    3.安装好MySQL，设置好账号和密码，并且创建好一个数据库。
        create database database_name charset utf8;
    4.修改config中的数据库配置文件：
        SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/database_name'
        填写好你的数据库的账号和密码，以及你创建好的database_name。
    5.使用Flask-Migrate实现数据库的迁移
        python manage.py db init : 创建迁移的脚本
        python manage.py db migrate:创建迁移的脚本
        python manage.py db upgrade:更新数据库
    6.在pycharm中启动platform程序，打开http://127.0.0.1:5000 查看项目内容.
