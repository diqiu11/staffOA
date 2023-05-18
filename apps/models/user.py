from apps.models.base_db import base_db
from apps.models.base_model import base_model
from config.evn import DB_PREFIX
from extends import db

# 用户模型
class User(base_model, base_db):
    # 设置表名
    __tablename__ = DB_PREFIX + "user"
    # 用户姓名
    realname = db.Column(db.String(150), nullable=False, comment="用户姓名")
    # 公司id
    # companyID = db.Column(db.Integer, default=0, comment="公司ID")
    # 部门id
    departmentID = db.Column(db.Integer, default=0, comment="部门ID")
    # 项目id
    projectID = db.Column(db.Integer, default=0, comment="项目ID")
    # 岗位ID
    positionID = db.Column(db.Integer, default=0, comment="岗位ID")
    # 角色id
    # roleID = db.Column(db.Integer, default=0, comment="角色ID")
    # 飞书id
    feishuID = db.Column(db.String(250), default=0, comment="飞书ID")
    # 用户昵称
    # nickname = db.Column(db.String(150), nullable=False, comment="用户昵称")
    # # 性别：1-男 2-女 3-保密
    # gender = db.Column(db.Integer, default=1, comment="性别：1-男 2-女 3-保密")
    # # 用户头像
    # avatar = db.Column(db.String(255), nullable=False, comment="用户头像")
    # # 手机号
    # mobile = db.Column(db.String(30), nullable=False, comment="手机号")
    # # 邮箱
    # email = db.Column(db.String(30), nullable=False, comment="邮箱")
    # # 出生日期
    # birthday = db.Column(db.Date, nullable=True, comment="出生日期")
    # # 部门ID
    # dept_id = db.Column(db.Integer, default=0, comment="部门ID")
    # # 职级ID
    # level_id = db.Column(db.Integer, default=0, comment="职级ID")
    # # 岗位ID
    # position_id = db.Column(db.Integer, default=0, comment="岗位ID")
    # # 省份编码
    # province_code = db.Column(db.String(30), nullable=False, comment="省份编码")
    # # 城市编码
    # city_code = db.Column(db.String(30), nullable=False, comment="城市编码")
    # # 县区编码
    # district_code = db.Column(db.String(30), nullable=False, comment="县区编码")
    # # 省市区信息
    # address_info = db.Column(db.String(255), nullable=True, comment="省市区信息")
    # # 详细地址
    # address = db.Column(db.String(255), nullable=False, comment="详细地址")
    # 用户名
    # username = db.Column(db.String(30), nullable=True, comment="用户名")
    # # 密码
    # password = db.Column(db.String(255), nullable=True, comment="密码")
    # # 加密盐
    # salt = db.Column(db.String(30), nullable=True, comment="加密盐")
    # 个人简介
    # intro = db.Column(db.String(255), nullable=True, comment="个人简介")
    # # 状态：1-正常 2-禁用
    # status = db.Column(db.Integer, default=1, comment="状态：1-正常 2-禁用")
    # # 排序
    # sort = db.Column(db.Integer, default=0, comment="排序")
    # # 个人备注
    # note = db.Column(db.String(255), nullable=True, comment="个人备注")

    # 初始化
    def __init__(self, id, realname, departmentID, projectID, positionID, feishuID):
        self.id = id
        self.realname = realname
        self.departmentID = departmentID
        self.projectID = projectID
        self.positionID = positionID
        self.feishuID = feishuID
        # self.nickname = nickname
        # self.gender = gender
        # self.avatar = avatar
        # self.mobile = mobile
        # self.email = email
        # self.birthday = birthday
        # self.dept_id = dept_id
        # self.level_id = level_id
        # self.position_id = position_id
        # self.province_code = province_code
        # self.city_code = city_code
        # self.district_code = district_code
        # self.address = address
        # self.username = username
        # self.password = password
        # self.intro = intro
        # self.status = status
        # self.sort = sort
        # self.note = note

    def __str__(self):
        return "用户{}".format(self.id)
