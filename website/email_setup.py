from .models import mail, log
from flask_mail import Message
from flask import current_app
import os
# html mailer
class Mailer:
    def __init__(self):
        self.sender =  os.environ.get('MAIL_USERNAME')
    def html_mail(self, recipients, subject, body):
        msg = Message(subject,sender=self.sender, recipients=recipients)
        msg.html = body
        mail = current_app.extensions['mail']
        mail.send(msg)
        log.info(f"Email sent to {recipients} with subject: {subject}")