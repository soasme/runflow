import os
import ssl
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List


class SmtpSendTask:
    """Send email via SMTP server."""

    def __init__(
        self,
        subject: str = "",
        message: str = "",
        html_message: str = "",
        email_from: str = None,
        email_to: str = None,
        email_to_cc: str = None,
        email_to_bcc: str = None,
        attachments: List[str] = None,
        client: dict = None,
    ):
        self.subject = subject
        self.message = message
        self.html_message = html_message
        self.email_from = email_from
        self.email_to = email_to
        self.email_to_cc = email_to_cc
        self.email_to_bcc = email_to_bcc
        self.attachments = attachments or []
        self.client = client or {}

    def run(self):
        message = MIMEMultipart()

        message["Subject"] = self.subject
        message["From"] = self.email_from
        message["To"] = self.email_to

        if self.email_to_cc:
            message["Cc"] = self.email_to_cc

        if self.email_to_bcc:
            message["Bcc"] = self.email_to_bcc

        if self.message:
            message.attach(MIMEText(self.message, "plain"))

        if self.html_message:
            message.attach(MIMEText(self.html_message, "html"))

        for attachment in self.attachments:
            part = MIMEBase("application", "octet-stream")
            with open(attachment, "rb") as file:
                part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {os.path.basename(attachment)}",
            )
            message.attach(part)

        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL(
            context=context,
            **{
                "host": self.client.get("host") or "",
                "port": int(self.client.get("port") or 465),
                "local_hostname": self.client.get("local_hostname"),
                "timeout": self.client.get("timeout"),
                "source_address": self.client.get("source_address"),
            },
        )

        username = self.client["username"]
        password = self.client["password"]
        server.login(username, password)

        try:
            server.send_message(message)
        finally:
            server.quit()
