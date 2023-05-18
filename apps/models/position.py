from apps.models.base_db import base_db
from apps.models.base_model import base_model
from config.evn import DB_PREFIX
from extends import db


# 岗位模型
class Position(base_model, base_db):
    # 设置表名
    __tablename__ = DB_PREFIX + "position"
    # 岗位名称
    name = db.Column(db.String(255), nullable=False, comment="岗位名称")
    # 岗位状态：1-在用 2-停用
    status = db.Column(db.Integer, default=0, comment="岗位状态：1-在用 2-停用")
    # 岗位排序
    sort = db.Column(db.Integer, default=0, comment="岗位排序")

    # 初始化
    def __init__(self, id, name, status, sort):
        self.id = id
        self.name = name
        self.status = status
        self.sort = sort

    def __repr__(self):
        return '岗位：{}'.format(self.name)
