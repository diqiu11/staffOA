from apps import create_app
from config.evn import FLASK_HOST, FLASK_PORT, FLASK_DEBUG

# 创建应用实例
app = create_app()

# # 创建Redis的客户端连接
# redis_client = FlaskRedis(app)
# redis_client.init_app(app)

if __name__ == '__main__':
    # app.run()
    # 启动应用
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)