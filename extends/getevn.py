import os

from dotenv import load_dotenv

# 项目根目录决定路径
root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# 配置文件路径
flask_env_path = os.path.join(root_path, '.env')


# 初始化全局配置文件
def init_dotenv():
    # 判断文件是否存在
    if os.path.exists(flask_env_path):
        # 加载配置文件
        load_dotenv(flask_env_path)