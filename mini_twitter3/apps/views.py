from flask import render_template, Flask, request, url_for
from apps import app
import time

from google.appengine.ext import db

class DatastoreFile(db.Model):
    image = db.BlobProperty()
    text = db.StringProperty()

@app.route('/')
@app.route('/index')
def index():



    return render_template("upload.html",all_data = DatastoreFile.all())

@app.route('/upload', methods=['POST'])
def upload_db():	

	post_image = request.files['photoo']

	post_text = request.form['text']


	filestream = post_image.read()
	if post_image:
		up_data = DatastoreFile()
		up_data.image = db.Blob(filestream)
		up_data.text = post_text
		up_data.put()

		# url = url_for("shows", key=up_data.key())

		time.sleep(1)

		return render_template("upload.html", up_data=up_data, all_data = DatastoreFile.all())

	return "hello"
		
@app.route('/show/<key>')
def shows(key):
	upload_data = db.get(key)
	return app.response_class(upload_data.image)

@app.route('/delete', methods=['POST'])
def delete():

	db.delete(request.form['delete'])

	time.sleep(1)

	return render_template("upload.html",all_data = DatastoreFile.all())










