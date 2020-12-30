"""
Initialises Mail and defines our html-mail template.
"""
# Library Imports
from flask_mail import Mail
from flask import current_app

# App_specific imports
from utils.logging import filelogger

mail = Mail()

register_template = """
Registering User {0}
"""

def sendmail(subject, recipients, template, data):
    body = ""
    if template == "register":
        body = register_template.format(data["username"])

    mail.send(
        Message(
            subject=f"{subject}",
            sender=current_app.config["DEFAULT_MAIL_SENDER"],
            html = body,
            recipients=recipients,
        )
    )
    filelogger.debug("Mail send to %s" % data["email"])


