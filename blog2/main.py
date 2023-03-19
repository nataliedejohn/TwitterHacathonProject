# This is a sample Python script.
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return 'Help me'

# def print_hi(name):
#    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

