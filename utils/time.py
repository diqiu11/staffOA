from datetime import date, datetime
from flask.json import JSONEncoder as f_JSONEncoder


# 处理返回时间，直接使用 jsonify 会把时间处理成 GMT 时间
class JSONEncoder(f_JSONEncoder):
    def default(self, o):  # pylint: disable=E0202
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        return super(JSONEncoder, self).default(o)