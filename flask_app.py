
#from flask import Flask
# app = Flask(__name__)


from app import  app, db
# from app.models import User, Product

@app.shell_context_processor
def make_shell_context():
  return {'db': db, 'User': User, 'Product': Product}

if __name__ == '__main__':
    app.run()




