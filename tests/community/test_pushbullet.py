import pytest

from runflow import runflow

pytest.importorskip('slack_sdk')


def test_pushbullet_push_note(mocker):
    pb = mocker.MagicMock()
    mocker.patch('pushbullet.Pushbullet', pb)

    runflow(path="examples/pushbullet_push_note.hcl", vars={
        'pushbullet_api_key': 'any'
    })

    pb.return_value.push_note.assert_called_with(
        title='This is the title',
        body='This is the note',
        email='',
        channel=None,
    )

def test_pushbullet_push_link(mocker):
    pb = mocker.MagicMock()
    mocker.patch('pushbullet.Pushbullet', pb)

    runflow(path="examples/pushbullet_push_link.hcl", vars={
        'pushbullet_api_key': 'any'
    })

    pb.return_value.push_link.assert_called_with(
        title='This is the title',
        url='https://runflow.org',
        body='',
        email='',
        channel=None,
    )

def test_pushbullet_push_file(mocker):
    pb = mocker.MagicMock()
    mocker.patch('pushbullet.Pushbullet', pb)

    runflow(path="examples/pushbullet_push_file.hcl", vars={
        'pushbullet_api_key': 'any',
    })

    pb.return_value.push_file.assert_called_with(
        title='This is the title',
        body='This is the body',
        file_type='image/jpeg',
        file_name='cat.jpg',
        file_url='https://i.imgur.com/IAYZ20i.jpg',
        email='',
        channel=None,
    )

def test_pushbullet_invalid_client(mocker, capsys):
    pb = mocker.MagicMock()
    mocker.patch('pushbullet.Pushbullet', pb)
    runflow(source="""
flow "invalid_client" {
  task "pushbullet_push" "this" {
    client = {
    }
  }
}
    """)
    out, err = capsys.readouterr()
    assert 'set api_key' in err
