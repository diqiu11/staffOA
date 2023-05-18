from extends.getevn import init_dotenv
from extends.extends_sqlalchemy import db


# 注册扩展(扩展初始化)
def register_extends(app):
    # 初始化全局配置文件
    init_dotenv()
    # 绑定数据库到app中
    db.init_app(app)