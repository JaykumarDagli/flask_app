from flask import Flask, render_template, url_for

app = Flask(__name__)

posts =[
	{
		'author':'jay1',
		'title':'post1',
		'content': 'post1 content',
		'date' : 'Apr 20, 2018'
	},

	{
		'author':'jay2',
		'title':'post2',
		'content': 'post2 content',
		'date' : 'Apr 30, 2018'
	}
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
	app.run(debug=True)