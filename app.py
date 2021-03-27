from flask import Flask , render_template, request ,  make_response
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import cv2
from PIL import Image
import numpy
import backend_wrapper
from utils import list_to_table
app = Flask(__name__)

@app.route('/')
def upload_file():
	return render_template('home.html')

@app.route('/uploader' , methods = ['GET' , 'POST'])
def upload_file_1():
	if request.method == 'POST':
		f = request.files['file'].read()
		#print(f.read())
		npimg = numpy.fromstring(f,numpy.uint8)
		#img = cv2.imread(f)
		#print(img.shape if img else 'None')
		img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
		grid = backend_wrapper.solve(img)
		# ret, jpeg = cv2.imencode('.jpg', img)
		# print(img.shape)
		# response = make_response(jpeg.tobytes())
		# response.headers['Content-Type'] = 'image/png'
		# return response
		return list_to_table(grid)

if __name__ == '__main__':
	app.run(debug = True)
