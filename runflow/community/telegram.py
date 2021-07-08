class TelegramApiCallTask:
    def __init__(self, client: dict, api_method: str, **api_params: dict):
        self.client = client or {}
        self.api_method = api_method
        self.api_params = api_params

    def run(self):
        try:
            from telegram import Bot

            client = Bot(**self.client)
        except (ImportError, TypeError) as err:
            raise (
                ImportError("Please install runflow[telegram]")
                if isinstance(err, ImportError)
                else TypeError("Invalid telegram client")
            ) from err

        if not hasattr(client, self.api_method):
            raise ValueError(f"Invalid telegram api_method: {self.api_method}")

        method = getattr(client, self.api_method)
        result = method(**self.api_params)
        return {"result": result}
