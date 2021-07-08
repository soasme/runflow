import pytest
from slack_sdk.errors import SlackApiError

from runflow import runflow


pytest.importorskip('slack_sdk')


def test_slack_api_call_invalid_token(mocker, capsys):
    async def chat_postMessage(**kwargs):
        raise SlackApiError('invalid_auth', {'ok': False, 'error': 'invalid_auth'})

    mock_client_class = mocker.MagicMock()
    mock_client_class.return_value.chat_postMessage = chat_postMessage
    mocker.patch('slack_sdk.web.async_client.AsyncWebClient', mock_client_class)

    runflow(source="""
flow "send_slack_message" {
    task "slack_api_call" "this" {
        client = {
            token = "ANY"
        }
        api_method = "chat.postMessage"
        channel = "#random"
        text = "hello world"
    }
    task "file_write" "output" {
        filename = "/dev/stdout"
        content = tojson(eval(str(task.slack_api_call.this.response)))
    }
}
    """, vars={})
    out, err = capsys.readouterr()
    assert out == '{"ok": false, "error": "invalid_auth"}\n'

def test_slack_api_call_successful(mocker, capsys):
    async def chat_postMessage(**kwargs):
        return {'ok': True}

    mock_client_class = mocker.MagicMock()
    mock_client_class.return_value.chat_postMessage = chat_postMessage
    mocker.patch('slack_sdk.web.async_client.AsyncWebClient', mock_client_class)

    runflow(source="""
flow "send_slack_message" {
    task "slack_api_call" "this" {
        client = {
            token = "ANY"
        }
        api_method = "chat.postMessage"
        channel = "#random"
        text = "hello world"
    }
    task "file_write" "output" {
        filename = "/dev/stdout"
        content = tojson(eval(str(task.slack_api_call.this.response)))
    }
}
    """, vars={})
    out, err = capsys.readouterr()
    assert out == '{"ok": true}\n'

def test_slack_api_call_missing_argument(capsys):
    source = """
flow "send_slack_message" {
    task "slack_api_call" "this" {
        client = {
            token = "ANY"
        }
        channel = "#random"
        text = "hello world"
    }
    task "file_write" "output" {
        filename = "/dev/stdout"
        content = tojson(eval(str(task.slack_api_call.this.response)))
    }
}
    """
    runflow(source=source, vars={})
    out, err = capsys.readouterr()
    assert 'TypeError' in err


def test_slack_api_call_invalid_client(capsys):
    runflow(source="""
flow "send_slack_message" {
    task "slack_api_call" "this" {
        client = {}
        api_method = "chat.postMessage"
        channel = "#random"
        text = "hello world"
    }
    task "file_write" "output" {
        filename = "/dev/stdout"
        content = tojson(eval(str(task.slack_api_call.this.response)))
    }
}
    """, vars={})
    out, err = capsys.readouterr()
    assert out == '{"ok": false, "error": "not_authed"}\n'

def test_slack_api_call_invalid_client2(capsys):
    runflow(source="""
flow "send_slack_message" {
    task "slack_api_call" "this" {
        client = {
            token = "ANY"
            some_random_argument = 1
        }
        api_method = "chat.postMessage"
        channel = "#random"
        text = "hello world"
    }
    task "file_write" "output" {
        filename = "/dev/stdout"
        content = tojson(eval(str(task.slack_api_call.this.response)))
    }
}
    """, vars={})
    out, err = capsys.readouterr()
    assert "got an unexpected keyword argument 'some_random_argument'" in out
