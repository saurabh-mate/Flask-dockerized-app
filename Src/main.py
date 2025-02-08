from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return " welcome to my Flask App! Use /hello, /add, or /multiply"

@app.route('/hello')
def hello():
    return "Hello, World!"

@app.route('/add')
def add():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = num1 + num2
        return f"The sum of {num1} and {num2} is {result}"
    except (ValueError, TypeError):
        return "Invalid input. Please provide two numbers as query parameters (num1 and num2)."
    except Exception as e: # Catching other potential errors
        return f"An error occurred: {e}"


@app.route('/multiply')
def multiply():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = num1 * num2
        return f"The product of {num1} and {num2} is {result}"
    except (ValueError, TypeError):
        return "Invalid input. Please provide two numbers as query parameters (num1 and num2)."
    except Exception as e: # Catching other potential errors
        return f"An error occurred: {e}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)  