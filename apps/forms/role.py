from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import NumberRange, DataRequired, Length, ValidationError

from apps.models.role import Role


# 角色表单验证
class RoleForm(FlaskForm):
    # 角色ID
    id = IntegerField(
        # 文本描述
        label='角色ID',
        # 验证规则
        validators=[
            NumberRange(min=0, message='角色ID必须大于0')
        ]
    )
    # 角色名称
    name = StringField(
        label='角色名称',
        validators=[
            DataRequired(message='角色名称不能为空'),
            Length(max=150, message='角色名称长度不得超过150个字符')
        ]
    )
    # 角色编码
    code = StringField(
        label='角色编码',
        validators=[
            DataRequired(message='角色编码不能为空'),
            Length(max=30, message='角色编码长度不得超过30个字符')
        ]
    )
    # 角色状态
    status = IntegerField(
        label='角色状态',
        validators=[
            DataRequired(message='角色状态不能为空'),
            NumberRange(min=1, max=2, message='角色状态值在1~2之间')
        ]
    )
    # 角色排序
    sort = IntegerField(
        label='角色排序',
        validators=[
            DataRequired(message='角色排序不能为空'),
            NumberRange(min=0, max=99999, message='角色排序值在0~99999之间')
        ]
    )
    # 角色备注
    note = StringField(
        label='角色备注',
        validators=[
            Length(max=255, message='角色备注长度不得超过255个字符')
        ]
    )

    # 自定义验证名称不能重复
    def validate_name(self, field):
        # 查询单条数据
        if not field.data and Role.query.filter(Role.name == field.data).first():
            raise ValidationError("角色名称不能重复")


# 状态设置表单
class RoleStatusForm(FlaskForm):
    # 角色ID
    id = IntegerField(
        # 文本描述
        label='角色ID',
        # 验证规则
        validators=[
            NumberRange(min=0, message='角色ID必须大于0')
        ]
    )
    # 角色状态
    status = IntegerField(
        label='角色状态',
        validators=[
            DataRequired(message='角色状态不能为空'),
            NumberRange(min=1, max=2, message='角色状态值在1~2之间')
        ]
    )
