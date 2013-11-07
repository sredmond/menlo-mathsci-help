from decorators import async
from flask import render_template
from flask.ext.mail import Message
from app import mail
from config import REPLY_RECEIVER

@async
def send_async_email(msg):
    mail.send(msg)

def send_email(subject, recipients, text_body, html_body):
    msg = Message(subject, recipients = recipients, reply_to = REPLY_RECEIVER)
    msg.body = text_body
    msg.html = html_body
    send_async_email(msg)