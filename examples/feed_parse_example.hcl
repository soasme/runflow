flow "feed_parse" {
  task "feed_parse" "paulgraham" {
    url = "http://www.aaronsw.com/2002/feeds/pgessays.rss"
  }

  task "file_write" "out" {
    filename = "/dev/stdout"
    content = tojson({
      website = task.feed_parse.paulgraham.feed.title
      latest_article_title = task.feed_parse.paulgraham.entries[0].title
      latest_article_url=task.feed_parse.paulgraham.entries[0].link
    }, {indent=2}...)
  }
}
