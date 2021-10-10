import pyautogui
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/pause')
def pause():
	pyautogui.press('playpause')
	return '200'

@app.route('/next')
def next_track():
	pyautogui.press('nexttrack')
	return '200'

@app.route('/prev')
def prev_track():
	pyautogui.press('prevtrack')
	return '200'

@app.route('/mute')
def volume_mute():
	pyautogui.press('volumemute')
	return '200'

@app.route('/vlmup')
def volume_up():
	pyautogui.press('volumeup')
	return '200'

@app.route('/vlmdown')
def volume_down():
	pyautogui.press('volumedown')
	return '200'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)

