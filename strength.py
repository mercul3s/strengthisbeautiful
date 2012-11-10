from flask import Flask, flash, render_template, request, redirect, url_for
import use_search
import os
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/display_videos', methods=["GET"])
def display_videos():
	# url = request.form['url']
	# # this function call verifies that the url entered has a tld and protocol
	# formatted_url = core.check_input(url)
	# status = core.get_http_status(url)
	# # only use message flashing for error messages. These values should be stored
	# # and read from a database.
	# for key, value in status.iteritems():	
	# 	flash(value)
	# return redirect('/')
		
@app.route('/test_page')
def test_page():
	return render_template('test_page.html')

app.secret_key = '(Faulties}Marinating[Ballin'

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.debug = True
	app.run(host='0.0.0.0', port=port)