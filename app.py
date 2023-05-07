from app import app
import importlib
from flask import request, abort

@app.route('/<path:path>')
def api(path):
    module = f"api.{path.replace('/', '.')}.{request.method.lower()}"
    try:
        module = importlib.import_module(module)
        return module.run()
    except Exception as e:
        return str(e)
    
@app.route('/')
def home():
    module = f"api.{request.method.lower()}"
    try:
        module = importlib.import_module(module)
        return module.run()
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)