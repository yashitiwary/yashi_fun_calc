from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            a = float(request.form['num1'])
            b = float(request.form['num2'])
            operation = request.form['operation']

            if operation == "add":
                result = a + b
            elif operation == "sub":
                result = a - b
            elif operation == "mul":
                result = a * b
            elif operation == "div":
                result = a / b if b != 0 else "Infinity"
        except:
            result = "Invalid Input"

    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
