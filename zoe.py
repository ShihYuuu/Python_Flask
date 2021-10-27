from flask import Flask, request, jsonify
from flask_restplus import Resource, Api
from flask_restplus import Namespace
from flask import render_template
from flask_restful import reqparse

app = Flask(__name__)
# api = Api(app)

@app.route('/page')
def index():
    return render_template('page.html')

app.run(debug=True, host='0.0.0.0', port=5000)

# 1 Send a json packet
"""
@api.route('/hello')
class Hello(Resource):
    def get(self):
        return jsonify(message = 'Yo~Yo~Yo~')
"""

# 2 Test all the method
"""
@api.route('/chapter2')
class context(Resource):
    def get(self):
        return jsonify(message = 'Yo~Yo~Yo~')
    
    def post(self):
        return 
    
    def delete(seld):
        return
"""

# 3 Create a namespace
"""
zoe_api = Namespace('Zoe', description='API operations')
api.add_namespace(zoe_api)

@zoe_api.route('/')
class myapi(Resource):
    def get(self):
        return jsonify(message = 'Hi I am Zoe.')

@zoe_api.route('/cute')
class myapi(Resource):
    def get(self):
        return jsonify(message = 'You are cute!')
"""

# 4 interact with different user
"""
student = {'std1': 'Happy', 'std2': 'Halloween'}

@api.route('/<string:id>')
class Aclass(Resource):
    def get(self, id):
        return {id: student[id]}

    def put(self, id):
        student[id] = request.form['data']
        return {id: student[id]} #, 201 自訂義狀態碼

# curl http://localhost:5000/std2 -d "data=cindy" -X PUT
"""

# 5 get Parameters
"""
student_api = Namespace('student', description='API operations')
api.add_namespace(student_api)

register_data = student_api.parser()
register_data.add_argument('name', required=True, help='Name is required')
register_data.add_argument('email', required=False, help='Email is required')
register_data.add_argument('password', required=True, help='Password is required', type=int)

student_data = student_api.parser()
student_data.add_argument('name', required=True, help='Entry your name')

student = []

@student_api.route('/')
class Aclass(Resource):

    @student_api.expect(register_data)
    def get(self):
        args = register_data.parse_args()
        user = {
            'name': args['name'],
            'email': args['email'],
            'password': args['password']
        }
        
        student.append(user)
        return jsonify(message = 'Register success')
    
    @student_api.route('/<string:name>')
    class Aclass(Resource):
        def put(self, name):
            for i in student:
                if name == i['name']:
                    return {name: i['email']}
            
            return {'message': 'No data'}
"""

# 6 Create a page
"""
@app.route('/page')
def index():
    return render_template('page.html')
"""
