from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import NumberRange, DataRequired, Length


# 部门表单验证
class DeptForm(FlaskForm):
    # 部门ID
    id = IntegerField(
        # 文本描述
        label='部门ID',
        # 验证规则
        validators=[
            NumberRange(min=0, message='部门ID必须大于0')
        ]
    )
    # 部门名称
    name = StringField(
        label='部门名称',
        validators=[
            DataRequired(message='部门名称不能为空'),
            Length(max=150, message='部门名称长度不得超过150个字符')
        ]
    )
    # 部门编码
    code = StringField(
        label='部门编码',
        validators=[
            DataRequired(message='部门编码不能为空'),
            Length(max=150, message='部门编码长度不得超过150个字符')
        ]
    )
    # 部门类型：1-公司 2-子公司 3-部门 4-小组
    type = IntegerField(
        label='部门类型',
        validators=[
            DataRequired(message='部门类型不能为空'),
            NumberRange(min=1, max=4, message='部门类型值在1~4之间')
        ]
    )
    # 上级ID
    pid = IntegerField(
        # 文本描述
        label='上级ID',
        # 验证规则
        validators=[
            NumberRange(min=0, message='上级ID不得小于0')
        ]
    )
    # 部门排序
    sort = IntegerField(
        label='部门排序',
        validators=[
            DataRequired(message='部门排序不能为空'),
            NumberRange(min=0, max=99999, message='部门排序值在0~99999之间')
        ]
    )
    # 部门备注
    note = StringField(
        label='部门备注',
        validators=[
            Length(max=255, message='部门备注长度不得超过255个字符')
        ]
    )
