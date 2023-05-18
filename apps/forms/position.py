from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

from apps.models.position import Position


# 岗位表单验证
class PositionForm(FlaskForm):
    # 岗位ID
    id = IntegerField(
        # 文本描述
        label='岗位ID',
        # 验证规则
        validators=[
            NumberRange(min=0, message='岗位ID必须大于0')
        ]
    )
    # 岗位名称
    name = StringField(
        label='岗位名称',
        validators=[
            DataRequired(message='岗位名称不能为空'),
            Length(max=150, message='岗位名称长度不得超过150个字符')
        ]
    )
    # 岗位状态
    status = IntegerField(
        label='岗位状态',
        validators=[
            DataRequired(message='岗位状态不能为空'),
            NumberRange(min=1, max=2, message='岗位状态值在1~2之间')
        ]
    )
    # 岗位排序
    sort = IntegerField(
        label='岗位排序',
        validators=[
            DataRequired(message='岗位排序不能为空'),
            NumberRange(min=0, max=99999, message='岗位排序值在0~99999之间')
        ]
    )

    # 自定义验证名称不能重复
    def validate_name(self, field):
        # 查询单条数据
        if not field.data and Position.query.filter(Position.name == field.data).first():
            raise ValidationError("岗位名称不能重复")


# 状态设置表单
class PositionStatusForm(FlaskForm):
    # 岗位ID
    id = IntegerField(
        # 文本描述
        label='岗位ID',
        # 验证规则
        validators=[
            NumberRange(min=0, message='岗位ID必须大于0')
        ]
    )
    # 岗位状态
    status = IntegerField(
        label='岗位状态',
        validators=[
            DataRequired(message='岗位状态不能为空'),
            NumberRange(min=1, max=2, message='岗位状态值在1~2之间')
        ]
    )
