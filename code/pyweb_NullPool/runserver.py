# -*- coding: utf-8 -*-
from web import app


@app.route('/hello')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
