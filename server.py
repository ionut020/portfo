from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

def write_to_file(data):
	with open('./database.txt', mode='a') as f:
		email = data['email']
		subject = data['subject']
		message = data['message']
		text = f.write(f'\n{email}{subject}{message}')

def write_to_csv(data):
	with open('./database.csv',newline ='', mode='a') as f2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_file = csv.writer(f2, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		csv_file.writerow([email,subject,message])		

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	try:
    		data = request.form.to_dict()
    		# write_to_file(data)
    		write_to_csv(data)
    		return redirect('multumesc.html')    	
    	except :
    		return 'Datele nu s-au salvat in baza de date !'
    else:
    	return 'Something wrong Try again !'

# @app.route('/<username>/<int:post_id>')
# def hello_world(username = None, post_id = None):
# 	return render_template('index.html', name=username, post_id=post_id)

# @app.route('/blog/dog')
# def blog():
# 	return 'My first blog'

# @app.route('/blog/2021/dog')
# def blog2():
# 	return 'My dog'

# @app.route('/blog')
# def blog3():
# 	print(url_for('static', filename='ico1.ico'))
# 	return render_template('./index.html')