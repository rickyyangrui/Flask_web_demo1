一.项目简介
1.本项目是一个小型的论坛系统，采用的是python + flask 项目框架进行开发,用户可以进行问答的发布。

2.安装简介：
（1）先创建好本地的虚拟环境，并且启动了虚拟环境，在虚拟环境中打开本项目。

（2）pip install -r requirements.txt , 安装所需要的包。

（3）在config中修改数据库的配置
SQLALCHEMY_DATABASE_URI = 'mysql://user:password@localhost/database_name'
填写你的数据库账号，密码，还有一点，我们需要先在数据库中创建好一个数据库，名称替换配置中的database_name.

(4) 在启动的虚拟环境中，进入到项目文件夹中。
python manage.py db init      :创建迁移的仓库
python manage.py db migrate   :创建迁移的脚本
python manage.py db upgrade   :更新数据库

（5）在pycharm中启动platform程序。
