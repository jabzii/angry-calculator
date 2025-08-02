from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ""
    angry_message = ""
    
    if request.method == 'POST':
        operator = request.form.get('operator')
        num1 = float(request.form.get('num1', 0))
        num2 = float(request.form.get('num2', 0))
        
        if operator == '+':
            result = num1 + num2
            angry_message = "If you needed help with that , I fear for humanity"
        elif operator == '-':
            result = num1 - num2
            angry_message = "Go get a pen and paper find it yourself ...."
        elif operator == '*':
            result = num1 * num2
            angry_message = "Not in a mood to answer such a lame question"
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
                angry_message = "are you such a dum KIDOOO.. go do it yourself"
            else:
                angry_message = "Error! Division by zero is not possible."
                result = "Error"
        elif operator == '**':
            result = num1 ** num2
            angry_message = "I am not in a mood to answer these stupid questions"
            
        else:
            angry_message = "Enter the correct operator you fool...."
            result = "Error"
            
    return render_template('calculator.html', result=result, angry_message=angry_message)

if __name__ == '__main__':
    app.run(debug=True)
