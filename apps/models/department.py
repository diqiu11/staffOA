from apps.models.base_db import base_db
from apps.models.base_model import base_model
from config.evn import DB_PREFIX
from extends import db


# 部门模型
class Dept(base_model, base_db):
    # 设置表名
    __tablename__ = DB_PREFIX + "dept"
    # 部门名称
    name = db.Column(db.String(150), nullable=False, comment="部门名称")
    # 部门编码
    code = db.Column(db.String(150), nullable=False, comment="部门编码")
    # 部门类型：1-公司 2-子公司 3-部门 4-小组
    type = db.Column(db.Integer, default=0, comment="部门类型：1-公司 2-子公司 3-部门 4-小组")
    # 上级部门ID
    pid = db.Column(db.Integer, default=0, comment="上级部门ID")
    # 部门排序
    sort = db.Column(db.Integer, default=0, comment="部门排序")
    # 备注
    note = db.Column(db.String(255), nullable=True, comment="备注")

    # 初始化
    def __init__(self, id, name, code, type, pid, sort, note):
        self.id = id
        self.name = name
        self.code = code
        self.type = type
        self.pid = pid
        self.sort = sort
        self.note = note

    def __str__(self):
        return '部门{}'.format(self.name)