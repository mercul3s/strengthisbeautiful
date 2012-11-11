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

@app.route('/display_videos', methods=["POST"])
def display_videos():
	return redirect('/arm_results')

@app.route('/navigation', methods=["GET"])
def navigation():
		return render_template('navigation.html')

@app.route('/display_core_vids', methods=["POST"])
def display_core_vids():
	return redirect('/core_results')

@app.route('/display_leg_vids', methods=["POST"])
def display_leg_vids():
	return redirect('/leg_results')

@app.route('/arm_results', methods=["GET"])
def arm_results(): 
	videos =[]  
	keyword_search="arms training women"
	options = ""
	videos = get_videos.youtube_search(options, keyword_search)
	return render_template('specific_results.html', videos = videos)

@app.route('/core_results', methods=["GET"])
def core_results(): 
	videos =[]  
	keyword_search="core training women"
	options = ""
	videos = get_videos.youtube_search(options, keyword_search)
	return render_template('specific_results.html', videos = videos)

@app.route('/leg_results', methods=["GET"])
def leg_results(): 
	videos =[]  
	keyword_search="leg training women"
	options = ""
	videos = get_videos.youtube_search(options, keyword_search)
	return render_template('specific_results.html', videos = videos)

# @app.route('/youtube_auth')
# # def youtube_auth():
# # 	return redirect("https://accounts.google.com/o/oauth2/auth?",
# #   	client_id=1084945748469-eg34imk572gdhu83gj5p0an9fut6urp5.apps.googleusercontent.com&,
# #   	redirect_uri=http://localhost/oauth2callback&,
# #   	scope=https://gdata.youtube.com&,
# #   	response_type=code&,
# #   	access_type=offline)

app.secret_key = '(Faulties}Marinating[Ballin'

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.debug = True
	app.run(host='0.0.0.0', port=port)