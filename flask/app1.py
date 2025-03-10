#  #hello world in Flask pycharm
# from flask import Flask
# app=Flask(__name__)
#
# @app.route('/')
# def hello():
#     return 'Hello world!'
#
# if __name__=='__main__':
#     app.run(debug=True)

#============================================
#hello+name
# from flask import Flask
# app=Flask(__name__)
#
# @app.route('/')
# def hello():
#     return 'Hello world!'
#
# @app.route('/<name>')
# def hello_world(name):
#     return 'Hello '+ name
#
# if __name__=='__main__':
#     app.run(debug=True)

#=========================================
#hello+name
# from flask import Flask
# app=Flask(__name__)
#
# @app.route('/')
# def hello():
#     return 'Hello world!'
#
# @app.route('/<name>')
# def hello_world(name):
#     return 'Hello '+ name
# #hello+name
# @app.route('/hello/<name>')
# def hello1(name):
#     b=int(name)
#     if b%2==0:
#         return f'given {b} is even'
#     else:
#         return f'given {b} is odd'
# if __name__=='__main__':
#     app.run(debug=True)
#===============================================
# from flask import Flask
# app=Flask(__name__)
#
# @app.route('/')
# def hello():
#     return 'Hello world!'
#
# @app.route('/<name>')
# def hello_world(name):
#     return 'Hello '+ name
# #hello+name
# @app.route('/hello/<int:name>')
# def hello1(name):
#     if name%2==0:
#         return f'given {name} is even'
#     else:
#         return f'given {name} is odd'
# if __name__=='__main__':
#     app.run(debug=True)

#=============================================

#Str-Dynamic URL
#By default in Flask route accepts string only. So, <str:> won't work
#But it acceptsdee123-@ etc so go with this
#+reverse string

# from flask import Flask, abort
# import re
#
# app = Flask(__name__)
#
# @app.route('/rev/<revstr>')
# def reverse_string(revstr):
#     if not re.match(r'^[a-zA-Z]+$', revstr):
#         abort(400, "Invalid format. Only letters are allowed.")
#     return f"Reversed string: {revstr[::-1]}"
#
# if __name__ == '__main__':
#     app.run(debug=True)

#========================================================================
#admin and guest
from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/admin')
def hello():
    return 'Hello admin!'

@app.route('/guest/<guest>')
def hello_world(guest):
    return 'Hello %s as a guest' %guest

@app.route('/user/<name>')
def hello1(name):
    if name=='admin':
        return redirect(url_for('hello'))
    else: return redirect(url_for('hello_world',guest=name))


if __name__=='__main__':
    app.run(debug=True)