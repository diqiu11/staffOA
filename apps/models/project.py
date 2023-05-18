from apps.models.base_db import base_db
from apps.models.base_model import base_model
from config.evn import DB_PREFIX
from extends import db


# 岗位模型
class Project(base_model, base_db):
    # 设置表名
    __tablename__ = DB_PREFIX + "project"
    # 项目名称
    name = db.Column(db.String(150), nullable=False, comment="项目名称")
    # 项目状态：1-在用 2-停用
    status = db.Column(db.Integer, default=0, comment="项目状态：1-在用 2-停用")
    # 项目排序
    sort = db.Column(db.Integer, default=0, comment="项目排序")

    # 初始化
    def __init__(self, id, name, status, sort):
        self.id = id
        self.name = name
        self.status = status
        self.sort = sort

    def __repr__(self):
        return '项目：{}'.format(self.name)
