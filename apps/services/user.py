from flask import request
from sqlalchemy import and_

import utils.dict
from apps.forms.user import UserForm, UserStatusForm, UpdatePwdForm, UserInfoForm, ResetPwdForm
from apps.models.department import Dept
#from apps.models.level import Level
from apps.models.project import Project
from apps.models.position import Position
from apps.models.user import User
from apps.models.user_role import UserRole
from apps.services import user_role
from extends import db
from utils import R, regular
from utils.utils import uid


# 查询用户分页数据
def UserList():
    # 页码
    page = int(request.args.get("page", 1))
    # 每页数
    limit = int(request.args.get("limit", 10))
    # 实例化查询对象
    query = User.query.filter(User.is_delete == 0)

    # 用户姓名
    realname = request.args.get('realname')
    if realname:
        query = query.filter(User.realname.like('%' + realname + '%'))
    # # 性别
    # gender = request.args.get('gender')
    # if gender:
    #     query = query.filter(User.gender == gender)
    # # 用户状态
    # status = request.args.get('status')
    # if status:
    #     query = query.filter(User.status == status)
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

        # 查看项目列表
        project_list = Project.query.filter(Project.is_delete == 0).all()
        projectList = {}
        if project_list:
            for project in project_list:
                projectList[project.id] = project.name

        # 查看职位列表
        position_list = Position.query.filter(Position.is_delete == 0).all()
        positionList = {}
        if position_list:
            for position in position_list:
                positionList[position.id] = position.name

        for item in user_list:
            # 获取用户角色列表
            roleList = user_role.getUserRoleList(item.id)
            # # 城市
            # city_list = []
            # # 省份编码
            # city_list.append(item.province_code)
            # # 城市编码
            # city_list.append(item.city_code)
            # # 县区编码
            # city_list.append(item.district_code)

            # 对象转字典
            data = utils.load2dict(item)
            # # 性别
            # data['gender_name'] = GENDER_LIST.get(item.gender)
            # # 头像
            # data['avatar'] = getImageURL(item.avatar) if item.avatar else ""
            # # 出生日期
            # data['birthday'] = str(item.birthday.strftime('%Y-%m-%d')) if item.birthday else None
            # 部门名称
            data['dept_name'] = deptList.get(item.dept_id) if deptList else None
            # 职级名称
            #data['level_name'] = levelList.get(item.level_id) if levelList else None
            # 项目名称
            data['project_name'] = projectList.get(item.project_id) if projectList else None
            # 岗位名称
            data['position_name'] = positionList.get(item.position_id) if positionList else None
            # 角色列表
            data['roleList'] = roleList
            # 行政区划
            #data['city'] = city_list
            # 创建时间
            data['create_time'] = str(item.create_time.strftime('%Y-%m-%d %H:%M:%S')) if item.create_time else None
            # 更新时间
            data['update_time'] = str(item.update_time.strftime('%Y-%m-%d %H:%M:%S')) if item.update_time else None
            # 加入列表
            result.append(data)
    # 返回结果
    return R.ok(data=result, count=count)



# 根据ID查询用户详情
def UserDetail(user_id):
    # 根据ID查询用户
    user = User.query.filter(and_(User.id == user_id, User.is_delete == 0)).first()
    # 查询结果判空
    if not user:
        return None

    # 获取用户角色数据
    roleList = UserRole.query.filter(UserRole.user_id == user.id).all()
    roles = []
    for role in roleList:
        roles.append(int(role.role_id))

    # # 城市编码
    # cityList = []
    # # 省份编号
    # cityList.append(user.province_code)
    # # 城市编码
    # cityList.append(user.city_code)
    # # 县区编码
    # cityList.append(user.district_code)

    # 对象转字典
    data = utils.load2dict(user)
    # # 头像
    # data['avatar'] = getImageURL(user.avatar) if user.avatar else ""
    # # 出生日期
    # data['birthday'] = str(user.birthday.strftime('%Y-%m-%d')) if user.birthday else None
    # 角色
    data['roles'] = roles
    # 行政区划
    # data['city'] = cityList
    # 返回结果
    return data

# 添加用户
def UserAdd():
    # 表单验证
    form = UserForm(request.form)
    if not form.validate():
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)

    # # 图片处理
    # avatar = form.avatar.data
    # if avatar:
    #     form.avatar.data = saveImage(avatar, "user")
    #
    # # 密码存在是MD5加密
    # password = form.password.data
    # if password:
    #     form.password.data = md5.getPassword(password)
    # else:
    #     # 密码不填时保持原密码值不做更新梳理
    #     del form.password

    # 用户角色
    roles = form.roles.data
    # 从表单中移除角色信息
    del form.roles

    # 表单数据赋值给对象
    user = User(**form.data)
    user.create_user = uid()

    # 插入数据
    user.save()

    # 创建用户角色数据
    addUserRole(user.id, roles)

    # 返回结果
    return R.ok(msg="添加成功")

# 创建用户角色信息
def addUserRole(user_id, roles):
    # 删除用户角色关系数据
    UserRole.query.filter(UserRole.user_id == user_id).delete()
    # 创建新的用户角色关系
    if roles:
        roleIdList = roles.split(',')
        for roleId in roleIdList:
            # 为空直接跳过
            if not roleId:
                continue
            user_role = UserRole(
                user_id=user_id,
                role_id=roleId
            )
            user_role.save()

# 删除用户
def UserDelete(user_id):
    # 记录ID为空判断
    if not user_id:
        return R.failed("记录ID不存在")
    # 分裂字符串
    list = user_id.split(',')
    # 计数器
    count = 0
    # 遍历数据源
    if len(list) > 0:
        for vId in list:
            # 根据ID查询记录
            user = User.query.filter(and_(User.id == int(vId), User.is_delete == 0)).first()
            # 查询结果判空
            if not user:
                return R.failed("记录不存在")
            # 设置删除标识
            user.is_delete = 1
            # 提交数据
            db.session.commit()
            # 计数器+1
            count += 1
    # 返回结果
    return R.ok(msg="本次共删除{0}条数据".format(count))


