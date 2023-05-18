from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

from apps.models.project import Project


# 项目表单验证
class ProjectForm(FlaskForm):
    # 项目ID
    id = IntegerField(
        # 文本描述
        label='项目ID',
        # 验证规则
        validators=[
            NumberRange(min=0, message='项目ID必须大于0')
        ]
    )
    # 项目名称
    name = StringField(
        label='项目名称',
        validators=[
            DataRequired(message='项目名称不能为空'),
            Length(max=150, message='项目名称长度不得超过150个字符')
        ]
    )
    # 项目状态
    status = IntegerField(
        label='项目状态',
        validators=[
            DataRequired(message='项目状态不能为空'),
            NumberRange(min=1, max=2, message='项目状态值在1~2之间')
        ]
    )
    # 项目排序
    sort = IntegerField(
        label='项目排序',
        validators=[
            DataRequired(message='项目排序不能为空'),
            NumberRange(min=0, max=99999, message='项目排序值在0~99999之间')
        ]
    )

    # 自定义验证名称不能重复
    def validate_name(self, field):
        # 查询单条数据
        if not field.data and Project.query.filter(Project.name == field.data).first():
            raise ValidationError("项目名称不能重复")

# 状态设置表单
class ProjectStatusForm(FlaskForm):
    # 项目ID
    id = IntegerField(
        # 文本描述
        label='项目ID',
        # 验证规则
        validators=[
            NumberRange(min=0, message='项目ID必须大于0')
        ]
    )
    # 项目状态
    status = IntegerField(
        label='项目状态',
        validators=[
            DataRequired(message='项目状态不能为空'),
            NumberRange(min=1, max=2, message='项目状态值在1~2之间')
        ]
    )
