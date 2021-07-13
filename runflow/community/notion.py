"""This module performs api call to notion.so service."""


class NotionApiCallTask:
    """Run notion.so api call."""

    def __init__(self, *, client: dict, api_method: str, **api_payload: dict):
        try:
            from notion_client import AsyncClient

            self.client = AsyncClient(**client)
        except (TypeError, ImportError) as err:
            raise (
                ImportError("Please install runflow[notion]")
                if isinstance(err, ImportError)
                else TypeError("Invalid notion client")
            ) from err

        self.api_method = api_method
        self.api_payload = api_payload

    async def run(self):
        method = self.client
        try:
            for attribute in self.api_method.split("."):
                method = getattr(method, attribute)
        except (ValueError,) as err:
            raise ValueError(
                f"{self.api_method} is not a valid api method"
            ) from err

        return await method(**self.api_payload)
