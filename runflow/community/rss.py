import time
import datetime
from typing import Union, Dict, List


class FeedParseTask:
    def __init__(
        self,
        url: str,
        etag: str = None,
        modified: Union[str, datetime.datetime, time.struct_time] = None,
        agent: str = None,
        referrer: str = None,
        handlers: List = None,
        request_headers: Dict[str, str] = None,
        response_headers: Dict[str, str] = None,
        resolve_relative_uris: bool = None,
        sanitize_html: bool = None,
    ):
        self.url = url
        self.etag = etag
        self.modified = modified
        self.agent = agent
        self.referrer = referrer
        self.handlers = handlers
        self.request_headers = request_headers
        self.response_headers = response_headers
        self.resolve_relative_uris = resolve_relative_uris
        self.sanitize_html = sanitize_html

    def run(self):
        try:
            from feedparser import parse
        except ImportError as err:
            raise ImportError("Please install runflow[rss]") from err

        feed = parse(
            self.url,
            etag=self.etag,
            modified=self.modified,
            agent=self.agent,
            referrer=self.referrer,
            handlers=self.handlers,
            request_headers=self.request_headers,
            response_headers=self.response_headers,
            resolve_relative_uris=self.resolve_relative_uris,
            sanitize_html=self.sanitize_html,
        )
        return feed
