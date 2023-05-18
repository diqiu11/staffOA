from datetime import datetime

from extends import db


# 基类模型
class base_model(db.Model):
    # 定义为抽象类
    __abstract__ = True
    # 默认字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="主键ID")
    create_user = db.Column(db.Integer, default=0, comment="创建人")
    create_time = db.Column(db.DATETIME, default=datetime.now, comment="创建时间")
    update_user = db.Column(db.Integer, default=0, comment="更新人")
    update_time = db.Column(db.DATETIME, default=datetime.now, comment="更新时间")
    is_delete = db.Column(db.Integer, default=0, comment="删除标识：0-正常 1-已删除")

    # 自定义将返回实例对象转化为json
    def to_json(self):
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item