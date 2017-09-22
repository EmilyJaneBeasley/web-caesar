from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/" method="post">
        <label for="rotate-by"> Rotate by: </label>
        <input type="text" name="rot" value=0 />
        <textarea name="text"> </textarea>
        <input type="submit"/>
        </form>
    </body>
    
</html>
"""


@app.route("/")
def index ():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    caesar_message = request.form['text']
    caesar_rotate = request.form['rot']
    ceasar_message = str(caesar_message)
    caesar_rotate = int(caesar_rotate)
    encrypted_message = rotate_string(caesar_message, caesar_rotate)
    return '<h1>' + encrypted_message + '<h1>'
    
    
app.run()