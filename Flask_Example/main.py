from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World</h1>'


# using jinja2 framework
# http://127.0.0.1:5000/welcome



@app.route('/welcome')
def welcome():
    return render_template('hello.html')


# using jinja2 template for path parameter  def fun(abc/name):....for using abs in function
# http://127.0.0.1:5000/welcome/parampreet
@app.route('/welcome/<name>')
def welcome_name(name):
    return render_template('welcome.html', myname=name)  # Passing Parameter to template


@app.route('/name')
def my_name():
    return 'Parampreet<h1>Gill</h1>'


# http://127.0.0.1:5000/sum?a=10&b=29--to run

@app.route('/sum')
def add_num():
    a = request.args.get('a')
    b = request.args.get('b')
    c = int(a) + int(b)
    return 'SUM: ' + str(c)


@app.route('/user-data', methods=['GET', 'POST'])
def user_data():
    if request.method == 'POST':
        first_name = request.form.get('fname')
        last_name = request.form.get('lnm')
        #dict = {"fname": first_name, "lname": last_name}

        result = '''
                  <h1>First Name : {} </h1>
                  <h1>Last Name : {} </h1>
                  '''
        return result.format(first_name, last_name)
        #return dict
    return 'NO GET method allowed . Only POST method allowed.'


@app.route('/user')
def user_form():
    return '''
    <form method="POST" action="http://127.0.0.1:5000/user-data">
    <div><label> First Name: <input type="text" name="fname"></label></div>
    <div><label>Last Name: <input type="text" name="lnm"></label></div>
    <input type="submit" value="Submit">
    </form>
    '''


if __name__ == '__main__':
    app.run()
