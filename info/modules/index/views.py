from flask import current_app, url_for

from . import index_blu
from flask import render_template


@index_blu.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('news/favicon.ico')


@index_blu.route('/')
def index():
    return render_template('news/index.html')


@index_blu.route('/index')
def index_redirect():
    # current_app.logger.debug('debug')  # 输出时，会打印分割线
    # current_app.logger.error('error')  # 不会覆盖原先的日志输出，它是增加了一些日志信息
    return render_template('news/index.html')
