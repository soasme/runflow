import logging


logger = logging.getLogger(__name__)


try:
    from slack_sdk.web.async_client import AsyncWebClient
    from slack_sdk.errors import SlackApiError
except ImportError:
    logger.warning("Package slack-sdk is not installed.")
    AsyncWebClient = None
    SlackApiError = Exception


class SlackApiCallTask:
    def __init__(self, client: dict, api_method: str, **kwargs):
        if not AsyncWebClient:
            raise ImportError("Package slack-sdk is not installed.")
        self.client = AsyncWebClient(**client)
        self.api_method = api_method
        self.kwargs = kwargs

    async def run(self):
        try:
            api_call = getattr(self.client, self.api_method.replace(".", "_"))
            response = await api_call(**self.kwargs)
            return {"response": response}
        except SlackApiError as err: # pylint: disable=broad-except
            return {"response": err.response}
