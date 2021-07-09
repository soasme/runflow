from base64 import b64decode
from typing import Union, Dict, List, Optional

import attr
import httpx


@attr.s(
    auto_attribs=True,
    kw_only=True,
    frozen=True,
)
class HttpRequestTask:
    """This task sends out an HTTP request."""

    method: str = attr.ib(
        validator=[
            attr.validators.instance_of(str),
            attr.validators.in_(
                ["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD"]
            ),
        ]
    )
    url: str = attr.ib(
        validator=attr.validators.instance_of(str),
    )
    params: Dict[str, str] = attr.ib(
        validator=attr.validators.instance_of(dict),
        factory=dict,
    )
    data: Dict[str, str] = attr.ib(
        validator=attr.validators.instance_of(dict),
        factory=dict,
    )
    json: Dict[str, str] = attr.ib(
        validator=attr.validators.instance_of(dict),
        factory=dict,
    )
    headers: Dict[str, str] = attr.ib(
        validator=attr.validators.instance_of(dict),
        factory=dict,
    )
    cookies: Dict[str, str] = attr.ib(
        validator=attr.validators.instance_of(dict),
        factory=dict,
    )
    files: Dict[str, str] = attr.ib(
        validator=attr.validators.instance_of(dict),
        factory=dict,
    )
    content: Optional[str] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(str)),
        default=None,
    )
    b64content: Optional[bytes] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(bytes)),
        default=None,
    )
    auth: Optional[Union[List[str], tuple]] = attr.ib(
        validator=attr.validators.optional(
            attr.validators.instance_of((tuple, list))
        ),
        default=None,
    )
    allow_redirects: bool = attr.ib(
        validator=attr.validators.instance_of(bool),
        default=True,
    )
    timeout: Optional[Union[Dict[str, float], float]] = attr.ib(
        validator=attr.validators.optional(
            attr.validators.instance_of(
                (
                    dict,
                    float,
                    int,
                )
            )
        ),
        default=None,
    )
    raise_for_status: bool = attr.ib(
        validator=attr.validators.instance_of(bool),
        default=True,
    )

    async def run(self):
        async with httpx.AsyncClient() as client:
            response = await client.request(
                method=self.method,
                url=self.url,
                params=self.params,
                headers=self.headers,
                cookies=self.cookies,
                content=(
                    b64decode(self.b64content)
                    if self.b64content
                    else self.content
                ),
                data=self.data,
                files=self.files,
                json=self.json,
                auth=self.auth,
                allow_redirects=self.allow_redirects,
                timeout=(
                    httpx.Timeout(**self.timeout)
                    if isinstance(self.timeout, dict)
                    else self.timeout
                ),
            )
            if self.raise_for_status:
                response.raise_for_status()
            return {"response": response}
