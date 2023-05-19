
import datetime

import jwt

from jwt import exceptions



# JWT加密盐
JWT_SALT = "ds()udsjo@jlsdosjf)wjd_#(#)$"


# JWT解密
def parse_payload(token):
    # 自定义对象
    message = {"code": 0, "data": None, "msg": "操作成功"}
    try:
        # 进行解密
        verified_payload = jwt.decode(token, JWT_SALT, algorithms=['HS256'])
        # 返回结果
        message['data'] = verified_payload
    except exceptions.ExpiredSignatureError:
        message['code'] = -1
        message['msg'] = "token已失效"
    except jwt.DecodeError:
        message['code'] = -1
        message['msg'] = "token认证失败"
    except jwt.InvalidTokenError:
        message['code'] = -1
        message['msg'] = "非法的token"
    return message