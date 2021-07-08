from unittest.mock import MagicMock

from runflow import runflow

def test_smtp_send(monkeypatch):
    import runflow.contribs.mail as mail

    smtplib = MagicMock()
    monkeypatch.setattr(mail, 'smtplib', smtplib)

    runflow(path='examples/smtp_send_example.hcl', vars={
        'smtp_username': 'example',
        'smtp_password': '123456',
    })

    assert smtplib.SMTP_SSL.return_value.login.call_args[0] == ('example', '123456')
    assert smtplib.SMTP_SSL.return_value.send_message.call_count == 1
