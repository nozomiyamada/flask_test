# virtual environment

- สร้าง virtual environment (ชื่อ `.venv`) 
- activate virtual environment
- pip install

~~~
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install flask
(.venv) $ pip install numpy
(.venv) $ pip install pandas
...
~~~

install package ที่ต้องการเสร็จแล้ว เขียนไว็เป็น `requirements.txt`

~~~
(.venv) $ pip freeze > requirements.txt
~~~

# packages ที่ต้องการ

- `flask`
- `gunicorn`  # application server สำหรับ python ไม่จำเป็น แต่มีดีกว่าตอนที่อัปโหลด

`pandas` มันกิน ram เยอะ ถ้าไม่จำเป็นก็ไม่ต้อง install

ถ้าใช้ github หรือ heroku ต้องเขียน `.gitignore` เพื่อที่จะไม่อัปโหลดไฟล์ที่ไม่ต้องการ

`.gitignore`
~~~
.venv
(other files ที่ไม่ต้องการ)
~~~

# directories 

~~~
(root directory)/
　├ .venv/
　├ .gitignore  # list of files ที่ไม้ต้องอัปโหลดโดย git
　├ static/  # folder ที่ใส่ static file เช่น `.jpg`
　├ templates/  # folder ที่ใส่ file `.html` 
　│　├ layout.html
　│　└ top.html
　├ requirements.txt  # list of python packages
　├ run.sh  # shell script ที่จะรันโปรแกรม (ไม่จำเป็น)
　└ app.py  # main program
~~~

# `app.py`

~~~python
import random
from flask import Flask, request, jsonify, render_template

app = Flask(__name__) # flask app instance

### top page ###
@app.route('/', methods=['GET', 'POST'])
def page_top():
    return render_template('toppage.html') # rendering "toppage.html"

### second page ###
@app.route('/2', methods=['GET', 'POST'])
def page_second():
	if request.method == 'GET':
		return render_template('page2.html') # rendering "page2.html"
	elif request.method == 'POST':
		text = request.form['input_text'].upper() # get text from form -> uppercase
		return render_template('page2.html', return_text=text) # re-rendering "page2.html" with variable "return_text"

### third page ###
@app.route('/3', methods=['GET', 'POST'])
def page_third():
    return render_template('page3.html') # rendering "page3.html"

# length page - return character length of the word as JSON
@app.route('/<word>', methods=['GET', 'POST'])
def page_length(word):
    return jsonify({'word': word, 'length': len(word)})

if __name__ == "__main__":
    # debug=True -> reload automatically when update app.py
    app.run(host="0.0.0.0", port=8000, debug=True)
~~~


# `jsonify` vs `render_template`

`jsonify()` จะ return ข้อมูลอย่างเดียว (เหมือน PokeAPI) 

ส่วน `render_template` จะให้ HTML file ที่พร้อมข้อมูลและ rendering เรียบร้อยแล้ว จึงใช้เวลานานกว่าส่งข้อมูลอย่างเดียว

ถ้าข้อมูลใหญ่ ควรส่งข้อมูลอย่างเดียวและให้ JavaScript เปลี่ยนเนื้อหาเว็บไซต์ (เช่น Ajax + vue.js)

# run application

~~~
$ source .venv/bin/activate  # activate 
(.venv) $ python app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 261-778-169
~~~

ใส่ `http://0.0.0.0:8000/` ใน URL bar 

เวลาปิด application กด `CTRL+C` or `command+C`

# top page -> rendering page 

`http://0.0.0.0:8000/`

![toppage](https://user-images.githubusercontent.com/44984892/111415872-61cfbf80-8715-11eb-90f4-d711cbe3f5cd.png)

# second page -> rendering page & send form (POST method)

`http://0.0.0.0:8000/2`

![page2](https://user-images.githubusercontent.com/44984892/111420500-ea525e00-871d-11eb-9e5d-fbecc81c7b84.png)

# third page -> rendering page with static file

`http://0.0.0.0:8000/3`

![page3](https://user-images.githubusercontent.com/44984892/111420593-179f0c00-871e-11eb-9505-748dadf4d50e.png)

# any word -> return json 

`http://0.0.0.0:8000/(anyword)`

![anyword](https://user-images.githubusercontent.com/44984892/111415865-5ed4cf00-8715-11eb-967d-e5b24db1ee7b.png)
