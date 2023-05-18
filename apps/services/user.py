from flask import request
from sqlalchemy import and_

import utils.dict
from apps.constants.constants import GENDER_LIST
from apps.constants.message import PAGE_LIMIT
from apps.forms.user import UserForm, UserStatusForm, UpdatePwdForm, UserInfoForm, ResetPwdForm
from apps.models.department import Dept
#from apps.models.level import Level
from apps.models.position import Position
from apps.models.user import User
from apps.models.user_role import UserRole
from apps.services import user_role
from extends import db
from utils import R, regular, md5
from utils.utils import getImageURL, uid, saveImage


# 查询用户分页数据
def UserList():
    # 页码
    page = int(request.args.get("page", 1))
    # 每页数
    limit = int(request.args.get("limit", PAGE_LIMIT))
    # 实例化查询对象
    query = User.query.filter(User.is_delete == 0)

    # 用户姓名
    realname = request.args.get('realname')
    if realname:
        query = query.filter(User.realname.like('%' + realname + '%'))
    # 性别
    gender = request.args.get('gender')
    if gender:
        query = query.filter(User.gender == gender)
    # 用户状态
    status = request.args.get('status')
    if status:
        query = query.filter(User.status == status)
    # 排序
    query = query.order_by(User.id.asc())
    # 记录总数
    count = query.count()
    # 分页查询
    user_list = query.limit(limit).offset((page - 1) * limit).all()
    # 实例化结果
    result = []
    # 遍历数据源
    if len(user_list) > 0:
        # 查看部门列表
        dept_list = Dept.query.filter(Dept.is_delete == 0).all()
        deptList = {}
        if dept_list:
            for dept in dept_list:
                deptList[dept.id] = dept.name

        # 查看职级列表
        # level_list = Level.query.filter(Level.is_delete == 0).all()
        # levelList = {}
        # if level_list:
        #     for level in level_list:
        #         levelList[level.id] = level.name

        # 查看职位列表
        position_list = Position.query.filter(Position.is_delete == 0).all()
        positionList = {}
        if position_list:
            for position in position_list:
                positionList[position.id] = position.name

        for item in user_list:
            # 获取用户角色列表
            roleList = user_role.getUserRoleList(item.id)
            # 城市
            city_list = []
            # 省份编码
            city_list.append(item.province_code)
            # 城市编码
            city_list.append(item.city_code)
            # 县区编码
            city_list.append(item.district_code)

            # 对象转字典
            data = utils.load2dict(item)
            # 性别
            data['gender_name'] = GENDER_LIST.get(item.gender)
            # 头像
            data['avatar'] = getImageURL(item.avatar) if item.avatar else ""
            # 出生日期
            data['birthday'] = str(item.birthday.strftime('%Y-%m-%d')) if item.birthday else None
            # 部门名称
            data['dept_name'] = deptList.get(item.dept_id) if deptList else None
            # 职级名称
            data['level_name'] = levelList.get(item.level_id) if levelList else None
            # 岗位名称
            data['position_name'] = positionList.get(item.position_id) if positionList else None
            # 角色列表
            data['roleList'] = roleList
            # 行政区划
            data['city'] = city_list
            # 创建时间
            data['create_time'] = str(item.create_time.strftime('%Y-%m-%d %H:%M:%S')) if item.create_time else None
            # 更新时间
            data['update_time'] = str(item.update_time.strftime('%Y-%m-%d %H:%M:%S')) if item.update_time else None
            # 加入列表
            result.append(data)
    # 返回结果
    return R.ok(data=result, count=count)

