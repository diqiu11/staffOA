from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from apps import create_app
from extends import db

# 创建应用
app = create_app()

manager = Manager(app)

# 第一个参数是Flask的实例，第二个参数是Sqlalchemy数据库实例
# # 用来绑定app和db到flask-migrate的
migrate = Migrate(app, db)

# manager是Flask-Script的实例，这条语句在flask-Script中添加一个db命令
# # 添加Migrate的所有子命令到db下
manager.add_command('db', MigrateCommand)

# 导入需要生成的模块类
from apps.models import *

if __name__ == '__main__':
    manager.run()