from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    input_text = request.form['input_text']
    # 在这里对接收到的数据进行处理，例如输出到控制台或返回给前端页面
    print("Received input text:", input_text)
    return "Input text received: " + input_text



if __name__ == '__main__':
    app.run(debug=True)
