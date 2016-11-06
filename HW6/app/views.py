from flask import render_template
from flask import Flask, redirect, request, url_for
from app import app
from .forms import QueryForm
from werkzeug import secure_filename

@app.route('/')
@app.route('/index')
def index():
    form = QueryForm()
    return render_template('Query.html', title = 'Home', db_empty=False, form = form)

@app.route('/index', methods=['GET', 'POST'])
def query():
    form = QueryForm()
    return render_template('Query.html', title = 'Home', db_empty=False, form=form)

@app.route('/query', methods = ['GET', 'POST'])
def upload_file():
   #if request.method == 'POST':
    #  f = request.files['file']
    #  f.save(secure_filename(f.filename))
    #  return 'file uploaded successfully'
    form = QueryForm()
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template('Query.html', title = 'Home', db_empty=False, form=form)
    #return '''
    #<!doctype html>
    #<title>Upload new File</title>
    #<h1>Upload new File</h1>
    #<form action="" method=post enctype=multipart/form-data>
    #  <p><input type=file name=file>
    #<input type=submit value=Upload>
    #</form>
    #'''
