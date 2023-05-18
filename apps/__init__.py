import os

from flask import Flask
from flask_cors import CORS
from flask_wtf import CSRFProtect

# from apps.middleware import register_middleware
from config import config
from apps.views import register_blueprint
# from apps.views.position import position_blue
# from config.env import REDIS_PASSWORD, REDIS_HOST, REDIS_PORT, REDIS_INDEX
from extends import register_extends
from utils.time import JSONEncoder
# csrf = CSRFProtect()


# 创建应用APP
def create_app():
    config_name = os.getenv('FLASK_ENV', 'development')
    # 创建Flask对象
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    # flask-redis 的配置和初始化
    # app.config['REDIS_URL'] = 'redis://:{}@{}:{}/{}'.format(REDIS_PASSWORD, REDIS_HOST, REDIS_PORT, REDIS_INDEX)
    # # 开启CSRF保护
    # csrf.init_app(app)
    # 设置应用配置
    app.config.from_object(config[config_name])
    # # json 序列化处理
    app.json_encoder = JSONEncoder
    # 跨域处理
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

    # 注册蓝图到
    register_blueprint(app)
    # 初始化扩展
    register_extends(app)
    # 注册中间件
    # register_middleware(app)

    # 返回APP
    return app