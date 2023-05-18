import os

# =============================================== 数据库配置 =================================================

# 数据库驱动
DB_DRIVER = os.getenv('DB_DRIVER', 'mysql')
# 数据库地址
DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
# 数据库端口
DB_PORT = os.getenv('DB_PORT', 3306)
# 数据库名称
DB_DATABASE = os.getenv('DB_DATABASE', 'staffOA')
# 数据库账号
DB_USERNAME = os.getenv('DB_USERNAME', 'root')
# 数据库密码
DB_PASSWORD = os.getenv('DB_PASSWORD', 'qhl123123')
# 数据表前缀
DB_PREFIX = os.getenv('DB_PREFIX', 't_oa_')
# 是否开启调试模式：是-True,否-False
DB_DEBUG = (os.getenv('DB_DEBUG', 'True') == 'True')


# 应用环境变量
FLASK_ENV = os.getenv('FLASK_ENV', 'development')
# 应用根目录
FLASK_ROOT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# 应用文件存储路径
FLASK_UPLOAD_DIR = os.getenv('FLASK_UPLOAD_DIR', os.path.join(FLASK_ROOT_PATH, '/uploads'))

# 应用运行地址
FLASK_HOST = os.getenv('FLASK_HOST', '127.0.0.1')
# 应用运行端口
FLASK_PORT = os.getenv('FLASK_PORT', 8022)
# 是否调试模式：是-True,否-False
FLASK_DEBUG = (os.getenv('FLASK_DEBUG', 'True') == 'True')