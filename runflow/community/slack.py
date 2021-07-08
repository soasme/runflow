import logging


logger = logging.getLogger(__name__)


try:
    from slack_sdk.web.async_client import AsyncWebClient
    from slack_sdk.errors import SlackApiError
except ImportError:
    pass


class SlackApiCallTask:
    def __init__(self, client: dict, api_method: str, **kwargs):
        self.client = client
        self.api_method = api_method
        self.kwargs = kwargs

    async def run(self):
        try:
            client = AsyncWebClient(**self.client)
        except NameError as err:
            err = "Package slack-sdk is not installed"
            return {"response": {"ok": False, "error": err}}
        except TypeError as err:
            return {"response": {"ok": False, "error": str(err)}}

        try:
            api_call = getattr(client, self.api_method.replace(".", "_"))
            response = await api_call(**self.kwargs)
            return {"response": response}
        except SlackApiError as err:  # pylint: disable=broad-except
            return {"response": err.response}
