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



import json
from click import command
from flask import Flask, jsonify
app = Flask(__name__) 
courses = [
         {'name':"Python",
            'course_id': "0",
            'Description': "Python",
            'price': "$130"
            },
           
           {'name':"Java",
            'course_id': "1",
            'Description': "JDK JRE",
            'price': "$150"
            },
           
           {'name':"Cython",
            'course_id': "2",
            'Description': "Python + C",
            'price': "$80"
            },
           
           {'name':"C++",
            'course_id': "3",
            'Description': "STL, Libraries, Competitive Coding",
            'price': "$120"
            },
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
    course = {'name':"C++",
            'course_id': "3",
            'Description': "STL, Libraries, Competitive Coding",
            'price': "$120"
            } 
    courses.append(course)
    return jsonify({'created': course})

# to make a post request we need this command
# curl.exe -i -H "Content-Type: Application/json" -X POST http://localhost:5000/courses


# now put method 
@app.route("/courses/<int:course_id>", methods = ['PUT'])
def course_update(course_id):
    courses[course_id]['Description']  ="XYZ"
    return jsonify({'course':courses[course_id]})
    
# curl.exe -i -H "Content-Type: Application/json" -X PUT http://localhost:5000/courses/3


@app.route("/courses/<int:course_id>",methods = ['DELETE'])
def delete(course_id):
    courses.remove(courses[course_id])
    return jsonify({'result': True})
# curl.exe -i -H "Content-Type: Application/json" -X DELETE http://localhost:5000/courses/3


if __name__ == "__main__":
    #    app.run(debug = True)
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)