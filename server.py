#first set up the virtual environment--  (cd ..) (web_development\ve\Scripts\activate) 
#installing flask-- (pip install flask)
#set up server--  (cd web_development) (python server.py) (set FLASK_APP=server.py) (set FLASK_ENV=development) (python -m flask run) then copy the link (http://127.0.0.1:5000/) and paste it to the chrome...
#but due to this when we do some editing in our server.py it doesnot changes in the chrome so we need to restart our server again and again
#to solve this we put (set FLASK_ENV=development) 




from flask import Flask, render_template, url_for, request, redirect 
import csv

app = Flask(__name__)
print(__name__)

"""@app.route('/')
def hello_world():
    return 'Hello, RITIKA!'
"""


"""@app.route('/')
def hello_world():
    print(url_for('static', filename='favicon.ico'))
    return render_template("./index.html")
"""


@app.route('/')
def my_home():
    return render_template("./index.html")



@app.route('/<string:page_name>')
def home(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt',mode='a')as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('data.csv',newline='',mode='a')as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer1 = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer1.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            print(data)
            return redirect("./thanku.html")
        except:
            return "did not save to database"
    else:
        return "not submiited.. Something went wrong.. TRY AGAIN"








"""

@app.route('/index.html')
def home():
    return render_template("index.html")

@app.route('/works.html')
def works():
    return render_template("works.html")

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")


@app.route('/blog')                                                             #http://127.0.0.1:5000/blog
def blog():
    return 'THESE ARE MY THOUGHTS ON BLOGS'



@app.route('/blog/2020/dogs')                                                       #http://127.0.0.1:5000/blog/2020/dogs
def blog2():
    return 'THIS IS MY DOG'
"""
