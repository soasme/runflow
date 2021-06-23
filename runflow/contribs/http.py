from base64 import b64decode

import httpx


class HttpRequestTask:
    def __init__(
        self,
        method,
        url,
        params=None,
        headers=None,
        cookies=None,
        content=None,
        b64content=None,
        data=None,
        files=None,
        json=None,
        auth=None,
        allow_redirects=True,
        timeout=None,
        raise_for_status=True,
    ):
        self.method = method
        self.url = url
        self.params = params
        self.headers = headers
        self.cookies = cookies
        self.content = b64decode(b64content) if b64content else content
        self.data = data
        self.files = files
        self.json = json
        self.auth = auth
        self.allow_redirects = allow_redirects
        self.timeout = timeout
        self.raise_for_status = raise_for_status

    async def run(self, context):
        async with httpx.AsyncClient() as client:
            response = await client.request(
                method=self.method,
                url=self.url,
                params=self.params,
                headers=self.headers,
                cookies=self.cookies,
                content=self.content,
                data=self.data,
                files=self.files,
                json=self.json,
                auth=self.auth,
                allow_redirects=self.allow_redirects,
                timeout=self.timeout,
            )
            if self.raise_for_status:
                response.raise_for_status()
            return {"response": response}
