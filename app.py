# import flask library
from flask import Flask, render_template, request
import requests
app = Flask(__name__)

# initialize flask

# route your webpage


@app.route('/')
def visitors():

    # Load current count
    counter_read_file = open("count.txt", "r")
    visitors_count = int(counter_read_file.read())
    counter_read_file.close()

    # Increment the count
    visitors_count = visitors_count + 1

    # Overwrite the count
    counter_write_file = open("count.txt", "w")
    counter_write_file.write(str(visitors_count))
    counter_write_file.close()
    return render_template("index.html", count=visitors_count)

# Render HTML with count variable

# route your webpage


@app.route('/', methods=['POST'])
def covid_stats():
    # # Load current count
    # counter_read_file = open("count.txt", "r")
    # visitors_count = int(counter_read_file.read())
    # counter_read_file.close()

    selected_option = request.form['operation']
    expression = request.form['expression']
    if expression != '':

        math_url = "https://newton.vercel.app/api/v2/"+selected_option+"/"+expression
        print(math_url)
        data = requests.get(math_url)

        information = data.json()

        # print(information)
        print("Result for given equation : "+information['result'])
        return render_template("index.html", result=information['result'])
    else:
        return render_template("index.html", result="Error")
# complete the code


# add code for executing flask
if __name__ == "__main__":
    app.run()
