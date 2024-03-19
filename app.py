from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def contact_form():
    return render_template('contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Here you can implement your logic to process the form data
        # For example, you could save it to a database, send an email, etc.
        
        return f"Thank you, {name}, for contacting us. We'll get back to you soon!"

if __name__ == '__main__':
    app.run(debug=True)
