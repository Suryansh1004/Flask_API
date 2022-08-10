# API 
# HTTP -> URL -> JSON -> REST!
# Representational State Transfer
# REST is basically a set of rules followed to make an API 
# Stateless -> Client Server -> Cacheable -> Layered System(provide Load balancing) ->  Code on Demand
# FLASK
# from crypt import methods
# Curl is a cmd-line software for transferring datat to or from the server using URL syntax
# curl -X POST [URL]
    #  -H "Content-Type: application/json" 
    #  -d "[JSON data]" 
# Where:
# -X, --request: HTTP method to use when communicating with the server.
# -H, --header: HTTP headers to send to the server with a POST request.
# -d, --data: Data to be sent to the server using a POST request.
# to make a post request we need this command
# curl.exe -i -H "Content-Type: Application/json" -X POST http://localhost:5000/courses 
# curl.exe -i -H "Content-Type: Application/json" -X PUT http://localhost:5000/courses/3
# curl.exe -i -H "Content-Type: Application/json" -X DELETE http://localhost:5000/courses/3


import json
from multiprocessing import connection
# from click import command
from flask import Flask, jsonify, request
import requests
app = Flask(__name__) 
courses = [
         {'name':'Python',
          'course_id':0,
          'description': 'interpret'
          },
           {'name':'java',
            'course_id': 1,
            'description': 'Bytecode'},
           {'name':'Cython',
            'course_id': 2,
            'description': 'Syn'},
           {'name':'C++',
            'course_id': 3,
            'description': 'Compiler'},
           ]

@app.route('/')
def index():
    return "<h1>Welcome to Course API!</h1>"

# GET METHOD
@app.route('/courses', methods=['GET'])
def get():
    return jsonify({'Courses':courses})

@app.route("/courses/<int:course_id>",methods=['GET'])
def get_course(course_id):
    return jsonify({'course':courses[course_id]})

# POST METHOD
@app.route("/courses",methods=['POST'])
def create():
    cour = {'name': request.json['name'],
              'course_id': request.json['course_id'],
              'description': request.json['description']
              } 
    courses.append(cour)
    return jsonify({'Course addded':courses})


# now put method 
@app.route("/courses/<int:course_id>", methods = ['PUT'])
def course_update(course_id):
    # course = [course for course in courses if course['id'] == course_id]
    # courses[course_id]['name'] = request.json['name']
    courses[course_id]['description'] = request.json.get('description',courses[course_id]['description'])
    return jsonify({'course_updated': courses[course_id]})

@app.route("/courses/<int:course_id>",methods = ['DELETE'])
def delete(course_id):
    courses.remove(courses[course_id])
    return jsonify({'Deleted': courses})

if __name__ == "__main__":
    app.run()