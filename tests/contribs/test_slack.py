import pytest
from slack_sdk.errors import SlackApiError

import runflow.contribs.slack as slack_contrib
from runflow import runflow


def test_slack_api_call_invalid_token(mocker, capsys):
    async def chat_postMessage(**kwargs):
        raise SlackApiError('invalid_auth', {'ok': False, 'error': 'invalid_auth'})

    mock_client_class = mocker.MagicMock()
    mock_client_class.return_value.chat_postMessage = chat_postMessage
    mocker.patch('runflow.contribs.slack.AsyncWebClient', mock_client_class)

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
    mocker.patch('runflow.contribs.slack.AsyncWebClient', mock_client_class)

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
