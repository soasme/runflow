from typing import Optional

import attr


@attr.s
class QrcodeGenerateTask:

    filename: str = attr.ib(
        validator=attr.validators.instance_of(str),
    )
    version: Optional[int] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        default=None,
    )
    error_correction: int = attr.ib(
        validator=attr.validators.in_([0, 1, 2, 3]),
        default=1,
    )
    box_size: int = attr.ib(
        validator=attr.validators.instance_of(int),
        default=10,
    )
    border: int = attr.ib(
        validator=attr.validators.instance_of(int),
        default=4,
    )
    data: str = attr.ib(
        validator=attr.validators.instance_of(str),
        default="",
    )
    # reserved by runflow for advanced usage.
    image: dict = attr.ib(
        validator=attr.validators.instance_of(dict),
        factory=dict,
    )

    def run(self):
        try:
            import qrcode
        except ImportError as err:
            raise ImportError("Please install runflow[qrcode]") from err

        code = qrcode.QRCode(
            version=self.version,
            error_correction=self.error_correction,
            box_size=self.box_size,
            border=self.border,
        )

        code.add_data(self.data)
        code.make(fit=True)

        img = code.make_image(**self.image)
        img.save(self.filename)

        return {"image": img}
