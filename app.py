from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here.
    return 'Hello World! from Christian Morris I am adding my first code change'

@app.route('/favorite-course')
def favorite_course():
    print('You entered your favorite course as:' + request.args.get('subject'))
    print('With the course number:' + request.args.get('c_number'))

    return render_template('favorite-course.html')

@app.route('/contact', methods = ['GET','POST'] )
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')



@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
