from flask import Flask, render_template,request,jsonify

app = Flask(__name__)

@app.route("/test",methods=["POST"])

def basic_calculator_via_postman():
    if (request.method=='POST'):
        operation = request.json['operation']
        num1  =int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(operation=='add'):
            sum = num1 + num2
            result = 'the sum of ' + str(num1)+'and'+ str(num2)+" is = " + str(sum)
        if (operation == 'subtraction'):
            sum = num1 - num2
            result = 'the difference of  ' + str(num1) + 'and' + str(num2) + " is = " + str(sum)
        if (operation == 'multiply'):
            sum = num1 * num2
            result = 'the product of' + str(num1) + 'and' + str(num2) + " is = " + str(sum)
        if (operation == 'division'):
            sum = num1 /num2
            result = 'the quotient of ' + str(num1) + 'and' + str(num2) + " is = " + str(sum)
        if (operation == "dividend"):
            sum = num1 % num2
            result = 'the remainder of  ' + str(num1) + 'and' + str(num2) + " is = " + str(sum)
        return jsonify(result)

@app.route("/rang",methods=["POST"])
def new_func():
    x = request.json['a']
    y = request.json['b']
    return jsonify(x**y)


if __name__ == '__main__':
    app.run()
