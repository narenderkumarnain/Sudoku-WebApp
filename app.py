from flask import Flask , render_template, request ,  make_response , redirect , url_for
#from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
#import cv2
#from PIL import Image
import numpy
import backend_wrapper
from utils import list_to_table
app = Flask(__name__)

@app.route('/')
def upload_file():
	return render_template('home.html')

@app.route('/waiting')
def waiting():
	return render_template('wait.html')

@app.route('/uploader' , methods = ['GET' , 'POST'])
def upload_file_1():
	if request.method == 'POST':
		redirect(url_for('waiting'))
		f = request.files['file'].read()
		#print(f.read())
		npimg = numpy.fromstring(f,numpy.uint8)
		#img = cv2.imread(f)
		#print(img.shape if img else 'None')
		img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
		resbool, grid = backend_wrapper.solve(img)
		# ret, jpeg = cv2.imencode('.jpg', img)
		# print(img.shape)
		# response = make_response(jpeg.tobytes())
		# response.headers['Content-Type'] = 'image/png'
		# return response
		message = 'If you see Reds in the Solved Sudoku, we are sorry for failing You 😔'
		if resbool == True:
			message = 'Yes! we have solved it 😃 '
		return render_template('result.html' , table = list_to_table(grid) , result = message)

if __name__ == '__main__':
	app.run()
