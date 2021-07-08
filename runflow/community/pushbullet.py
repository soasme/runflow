class PushbulletPushTask:
    """Push notifications to Android via Pushbullet service."""

    def __init__(
        self,
        title: str = "",
        body: str = "",
        url: str = "",
        file_type: str = "",
        file_name: str = "",
        file_url: str = "",
        channel: str = "",
        email: str = "",
        client: dict = None,
    ):
        self.title = title
        self.body = body
        self.url = url
        self.file_type = file_type
        self.file_name = file_name
        self.file_url = file_url
        self.channel = channel
        self.email = email
        self.client = client or {}

    def run(self):
        try:
            from pushbullet import Pushbullet

            client = Pushbullet(
                api_key=self.client["api_key"],
                proxy={
                    "https": self.client.get("https_proxy") or "",
                },
            )
        except (ImportError, KeyError) as err:
            raise (
                KeyError("Please set api_key for pushbullet_push")
                if isinstance(err, KeyError)
                else ImportError("Please install runflow[pushbullet]")
            ) from err

        channel = client.get_channel(self.channel) if self.channel else None

        if self.url:
            return client.push_link(
                title=self.title,
                url=self.url,
                body=self.body,
                email=self.email,
                channel=channel,
            )

        if self.file_url and self.file_name and self.file_type:
            return client.push_file(
                file_url=self.file_url,
                file_type=self.file_type,
                file_name=self.file_name,
                body=self.body,
                title=self.title,
                email=self.email,
                channel=channel,
            )

        if self.body:
            return client.push_note(
                title=self.title,
                body=self.body,
                email=self.email,
                channel=channel,
            )

        return {"iden": ""}
