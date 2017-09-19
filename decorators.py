#encoding: utf-8

from functools import wraps
from flask import session, redirect, url_for

# 登录限制的装饰器
def login_required(func):

    @wraps(func)
    def qingwa(*args, **kwargs):
        if session.get('user_id'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return qingwa
