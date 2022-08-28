from flask import Flask,request,jsonify, make_response
import datetime
import logging
import os


#set up flask parameters
app = Flask(__name__)

current_working_dir = os.getcwd()
# Set up Logging

log_name=os.path.join(current_working_dir,'api_log.log')
logging.basicConfig(filename=log_name, level=logging.DEBUG,
                   format='%(asctime)s %(message)s',
                   datefmt='%d%m%Y %H:%M:%S')

@app.route('/', method=['GET'])
def demo():
    print(request)
    print(request.headers)
    if request.headers['Content-Type'] != 'application/json':
        resp = jsonify('Hello, World')
       #resp = jsonify({'message': 'Hello, World'})
        return resp
    if request.headers['Content-Type'] == 'application/json':
        return jsonify({'message': 'Hello, World'})

if __name__== '  main  ':
    logging.info('==========Script started======')
   #app.run(host='localhost', port=80, debug=True)
    app.run()