import json

from runflow import runflow


def test_feed_parse(capsys):
    runflow(path="examples/feed_parse_example.hcl", vars={})
    out, err = capsys.readouterr()
    data = json.loads(out)
    assert 'website' in data
    assert 'latest_article_title' in data
    assert 'latest_article_url' in data
