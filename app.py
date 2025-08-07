from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # You can change this to any secure string

# Gmail SMTP configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'syhamqassim@gmail.com'        # <-- Replace with your Gmail
app.config['MAIL_PASSWORD'] = 'qtqi yyfp llhn ycfm'          # <-- Replace with your Gmail App Password
app.config['MAIL_DEFAULT_SENDER'] = 'syhamqassim@gmail.com'  # <-- Same as MAIL_USERNAME

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    try:
        msg = Message(
            subject=f'New Contact Form Submission from {name}',
            recipients=['yourgmail@gmail.com'],  # You can send it to yourself or a team email
            body=f"From: {name}\nEmail: {email}\n\nMessage:\n{message}"
        )
        mail.send(msg)
        flash("Message sent successfully!", "success")
    except Exception as e:
        print("Email sending failed:", e)
        flash("Failed to send message. Please try again later.", "error")

    return redirect(url_for('home'))
