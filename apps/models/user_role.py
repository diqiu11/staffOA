from apps.models.base_db import base_db
from apps.models.base_model import base_model
from config.evn import DB_PREFIX
from extends import db


# 用户角色模型
class UserRole(base_model, base_db):
    # 设置表名
    __tablename__ = DB_PREFIX + "user_role"
    # 用户ID
    user_id = db.Column(db.Integer, default=0, comment="用户ID")
    # 角色ID
    role_id = db.Column(db.Integer, default=0, comment="角色ID")

    def __str__(self):
        return "用户角色表{}".format(self.user_id)