import os

from config.evn import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE, \
      FLASK_UPLOAD_DIR, DB_DEBUG


# 应用全局配置
class Config(object):
    DEBUG = False
    TESTING = False
    WTF_CSRF_CHECK_DEFAULT = False
    # 全局禁用CSRF
    WTF_CSRF_ENABLED = False
    DATABASE_URL = 'sqlite://:memory:'
    # 项目路径
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # 静态文件夹路径
    STATIC_DIR = os.path.join(BASE_DIR, '../static')
    TEMPLATE_DIR = os.path.join(BASE_DIR, '../templates')
    # 文件上传目录
    FLASK_UPLOAD_DIR = FLASK_UPLOAD_DIR
    pass


# 生产环境配置
class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'
    ENV = "production"
    pass


# 开发环境配置
class DevelopmentConfig(Config):
    # 打开调试模式
    DEBUG = DB_DEBUG
    ENV = "development"
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/flask_demo'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT,
                                                                      DB_DATABASE)
    # 是否追踪数据库修改，一般不开启, 会影响性能
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 是否显示底层执行的SQL语句,打开调试模式
    SQLALCHEMY_ECHO = True
    pass


# 测试环境配置
class TestingConfig(Config):
    TESTING = True
    pass


if __name__ == '__main__':
    print(Config.FLASK_UPLOAD_DIR)