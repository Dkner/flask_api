from flask import Flask, url_for, request, redirect, send_from_directory
import os


UPLOAD_FOLDER = '/Users/liliang/Downloads'
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/sum/<int:a>/<int:b>')
def sum(a, b):
    print(a, b)
    return str(a+b)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        the_file = request.files['file']
        if the_file:
            the_file.save(os.path.join(UPLOAD_FOLDER, the_file.filename))
            return redirect(url_for('uploaded_file',
                                    filename=the_file.filename))
    return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form action="" method=post enctype=multipart/form-data>
          <p><input type=file name=file>
             <input type=submit value=Upload>
        </form>
        '''

@app.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(debug=True)
