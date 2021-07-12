"""This module performs api call to notion.so service."""

import inspect

from notion_client import AsyncClient


class NotionApiCallTask:
    """Run notion.so api call."""

    def __init__(self, *, client: dict, api_method: str, **api_payload: dict):
        self.client = AsyncClient(**client)
        self.api_method = api_method
        self.api_payload = api_payload

    async def run(self):
        method = self.client
        try:
            for attribute in self.api_method.split("."):
                method = getattr(method, attribute)
            assert inspect.ismethod(method)
        except (ValueError, AssertionError) as err:
            raise ValueError(
                f"{self.api_method} is not a valid api method"
            ) from err

        return await method(**self.api_payload)
