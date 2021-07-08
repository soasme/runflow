class SlackApiCallTask:
    """Call Slack web API."""

    def __init__(self, client: dict, api_method: str, **kwargs):
        self.client = client
        self.api_method = api_method
        self.kwargs = kwargs

    async def run(self):
        try:
            from slack_sdk.web.async_client import AsyncWebClient
            from slack_sdk.errors import SlackApiError

            client = AsyncWebClient(**self.client)
        except (ImportError, TypeError) as err:
            err = (
                str(err)
                if isinstance(err, TypeError)
                else "Please install runflow[slack]"
            )
            return {"response": {"ok": False, "error": err}}

        try:
            api_call = getattr(client, self.api_method.replace(".", "_"))
            response = await api_call(**self.kwargs)
            return {"response": response}
        except SlackApiError as err:
            return {"response": err.response}
