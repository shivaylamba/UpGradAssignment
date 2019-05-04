from flask_mail import Mail, Message
import config

config.app.config.update(
    DEBUG=True,
    # EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    # change this to your gmail username and password
    MAIL_USERNAME='your_gmail',
    MAIL_PASSWORD='your_gmail_apps_password_key'
)
mail = Mail(config.app)
