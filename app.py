from flask import Flask , render_template, request , redirect , url_for
import cv2
import numpy
import backend_wrapper
from utils import *

# Creating the flask app
app = Flask(__name__)

# ------------------------------------------Main Routes ----------------------------------------------------------------
# ---- Under work Currently ------------------
@app.route('/about')
def about_site():
	return render_template('about.html')

# ---- Home Route ----------------------------
@app.route('/')
def upload_file():
	return render_template('home.html')

# --- Temporary Testing Route ----------------
@app.route('/waiting')
def waiting():
	return render_template('wait.html')

# ------- Route for Uploading and processing Table
@app.route('/uploader' , methods = ['GET' , 'POST'])
def upload_file_1():
	if request.method == 'POST':
		# Retriving the files
		redirect(url_for('waiting'))
		f = request.files['file'].read()

		# input to opencv directly without saving
		npimg = numpy.fromstring(f,numpy.uint8)
		img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
		resbool, grid = backend_wrapper.solve(img)

		# a flash message about results of the sudoku
		message = 'We are sorry for failing You 😔'
		if resbool == True:
			message = 'Yes! we have solved it 😃 '
		return render_template('result.html' , table = list_to_table_styled(grid) , result = message)


if __name__ == '__main__':
	app.run()
