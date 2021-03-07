from flask import Flask
from flask import render_template
from flask import Markup

from get_requests.get_astro import get_astro_name, get_astro_profile, nasa_pic_of_the_day

app = Flask(__name__)


@app.route('/', methods=['GET'])
def test_index():
    potd = nasa_pic_of_the_day()
    return render_template('pages/index.html', potd=potd)

@app.route('/about', methods=['GET'])
def test_about():
    return render_template('pages/about.html')

@app.route('/astronauts', methods=['GET'])
def astronauts():
    astro_names = get_astro_name()
    return render_template('pages/astronauts.html', astro_names=astro_names)

@app.route('/astronauts/<name>', methods=['GET'])
def astronauts_page(name):
    astro_profile = get_astro_profile(name)
    return render_template('pages/astro_page.html', name=name, astro_profile=astro_profile)

@app.route('/proj1', methods=['GET'])
def test_proj1():
    return render_template('pages/proj1.html')

@app.route('/projects', methods=['GET'])
def test_projects():
    return render_template('pages/projects.html')

@app.route('/singlepost', methods=['GET'])
def test_singlepost():
    return render_template('pages/singlepost.html')

@app.route('/wheres_iss', methods=['GET'])
def wheres_iss():
    return render_template('pages/wheres_iss.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80 )