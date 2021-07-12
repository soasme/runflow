import pytest

from runflow import runflow

pytest.importorskip("notion_client")


def test_update_notion_title(mocker):
    client = mocker.MagicMock()
    mocker.patch("notion_client.AsyncClient", client)

    runflow(
        path="examples/notion_update_title.hcl",
        vars={
            "notion_token": "any",
        },
    )

    client.return_value.pages.update.assert_called_with(
        page_id="ee5b6cd7-a7a3-40d7-9ae5-ae28c52b67ea",
        properties={
            "title": {
                "id": "title",
                "title": [{"text": {"content": "Runflow Test"}, "type": "text"}],
                "type": "title",
            }
        },
    )
