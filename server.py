'''Coding Dojo Flask Fundamentals "Dojo Survey" assignment
by: Troy Center, troycenter1@gmail.com, Coding Dojo Python fundamentals, June 2017
'''
#pylint: disable=C0103

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def formpage():
    '''page has form, passes data in.'''
    return render_template("index.html")

@app.route('/process', methods=['GET', 'POST'])
def processpage():
    '''This is the process page that the user is redirected to after form submission. '''
    print "Got Post Info"
    print request.form
    name = request.form['name']
    dojo = request.form['dojo']
    language = request.form['language']
    comment = request.form['comment']
    return render_template("process.html", name=name, dojo=dojo, language=language, comment=comment)
app.run(debug=True)
