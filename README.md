# flask_test

### virtual environment

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

### packages ที่ต้องการ

- `flask`
- `gunicorn`  # application server สำหรับ python ไม่จำเป็น แต่มีดีกว่าตอนที่อัปโหลด

`pandas` มันกิน ram เยอะ ถ้าไม่จำเป็นก็ไม่ต้อง install

ถ้าใช้ github หรือ heroku ต้องเขียน `.gitignore` เพื่อที่จะไม่อัปโหลดไฟล์ที่ไม่ต้องการ

`.gitignore`
~~~
.venv
.gitignore
(other files ที่ไม่ต้องการ)
~~~

### directories 

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

### `app.py`

~~~python:
import random
from flask import Flask, request, jsonify, render_template

app = Flask(__name__) # flask app instance

# top page
@app.route('/', methods=['GET', 'POST'])
def page_top():
    return render_template('top.html') # rendering "top.html"

# length page - return character length of the word
@app.route('/<word>', methods=['GET', 'POST'])
def page_length(word):
    return jsonify({'length': len(word)})

if __name__ == "__main__":
    # debug=True -> reload automatically when update app.py
    app.run(host="0.0.0.0", port=8000, debug=True)
~~~

### `jsonify` vs `render_template`

`jsonify()` จะ return ข้อมูลอย่างเดียว (เหมือน PokeAPI) 

ส่วน `render_template` จะให้ HTML file ที่พร้อมข้อมูลและ rendering เรียบร้อยแล้ว จึงใช้เวลานานกว่าส่งข้อมูลอย่างเดียว

ถ้าข้อมูลใหญ่ ควรส่งข้อมูลอย่างเดียวและให้ JavaScript เปลี่ยนเนื้อหาเว็บไซต์ (เช่น Ajax + vue.js)


