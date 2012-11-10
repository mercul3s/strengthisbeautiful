from flask import Flask, flash, render_template, request, redirect, url_for, session, g
from optparse import OptionParser
import os
import get_videos


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/work_outs', methods=['GET'])
def work_out():
	return render_template('workouts.html')

@app.route('/display_videos', methods=["POST", "GET"])
def display_videos():
	if request.method == "POST":
		keyword_search="code training women"
		options = ""
		videos = get_videos.youtube_search(options, keyword_search)
		print videos
		return render_template('exercises.html', videos = videos)	
	if request.method == "GET":
		return redirect('/exercises')
	

@app.route('/exercises', methods=['GET'])
def exercises(videos):
	if videos:
		for item in videos:	
			flash(item)
	return redirect('/exercises')
	#return render_template('exercises.html')


		
# @app.route('/youtube_auth')
# # def youtube_auth():
# # 	return redirect("https://accounts.google.com/o/oauth2/auth?",
# #   	client_id=1084945748469-eg34imk572gdhu83gj5p0an9fut6urp5.apps.googleusercontent.com&,
# #   	redirect_uri=http://localhost/oauth2callback&,
# #   	scope=https://gdata.youtube.com&,
# #   	response_type=code&,
# #   	access_type=offline)

@app.route('/test_page')
def test_page():
	return render_template('test_page.html')

app.secret_key = '(Faulties}Marinating[Ballin'

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.debug = True
	app.run(host='0.0.0.0', port=port)