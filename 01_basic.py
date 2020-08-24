from flask import Flask

# special variable that is the name of the module
app = Flask(__name__)

# decorator to add functionalities 

# 2 routes will make sure that same page is returned on this call
@app.route('/')
@app.route('/home')
def home():
    return '<h2>There, There!<h2>'

# about page with different function name 
@app.route('/about')
def about():
    return '<h2>There, About!<h2>'


# STEPS TO RUN APP on cmd:
# set FLASK_APP=blog.py or FLASK_DEBUG=blog.py
# flask run
# OR 
# directly use the below conditional 
# and on cmd -> python blog.py

if __name__ == '__main__':
	app.run(debug=True)