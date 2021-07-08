import pytest
from runflow import runflow


pytest.importorskip('telegram')


def test_send_telegram_message(mocker):
    def send_message(chat_id, text):
        return {'chat_id': chat_id, 'text': text}

    mock_client_class = mocker.MagicMock()
    #mock_client_class.return_value.send_message = send_message
    mocker.patch('telegram.Bot', mock_client_class)

    runflow(path="examples/telegram_send_message.hcl", vars={
        "telegram_token": "ANY",
        "chat_id": "ANY",
    })


    mock_client_class.return_value.send_message.assert_called_with(text='Hello World! - Send From Runflow', chat_id="ANY", timeout=10)


def test_bad_telegram_client(capsys):
    runflow(source="""
flow "bad_telegram_client" {

  variable "telegram_token" {}
  variable "chat_id" {}

  task "telegram_api_call" "this" {
    client = {
      api_key= var.telegram_token
    }
    api_method = "send_message"
    chat_id = var.chat_id
    text = "Hello World! - Send From Runflow"
    timeout = 10
  }

}

    """, vars={
        "telegram_token": "ANY",
        "chat_id": "ANY",
    })
    out, err = capsys.readouterr()
    assert 'Invalid telegram client' in err
