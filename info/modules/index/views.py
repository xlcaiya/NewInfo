from flask import current_app

from . import index_blu


@index_blu.route('/index')
def index():
    current_app.logger.debug('debug')  # 输出时，会打印分割线
    current_app.logger.error('error')  # 不会覆盖原先的日志输出，它是增加了一些日志信息
    return 'index'
