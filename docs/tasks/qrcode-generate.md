---
sidebar: auto
---

# QRCode Generate Task

This task generates a QRCode image file.

Added since v0.10.0

::: tip
This feature requires installing `qrcode[pil]`:
```bash
$ pip install runflow[qrcode]
```
:::

## Generate QRCode PNG File

* Set `data`, usually it's an URI.
* Set `filename`.

<<< @/examples/qrcode_generate_example.hcl

::: details Click me to view the run output
Run:
```bash
$ runflow run examples/qrcode_generate_example.hcl
[2021-07-13 14:52:18,608] "task.qrcode_generate.runflow-org" is started.
[2021-07-13 14:52:21,824] "task.qrcode_generate.runflow-org" is successful.
```
:::

After running the flow, it should generate such an image:

![runflow-qrcode](/images/runflow-qrcode.png)

## Set Colors For QRCode

* Set `image.back_color` as the background color of the image file.
* Set `image.fill_color` as the filling color of the image file.

<<< @/examples/qrcode_generate_color.hcl

::: details Click me to view the run output
Run:
```bash
$ runflow run examples/qrcode_generate_color.hcl
[2021-07-13 14:52:18,608] "task.qrcode_generate.runflow-org" is started.
[2021-07-13 14:52:21,824] "task.qrcode_generate.runflow-org" is successful.
```
:::

After running the flow, it should generate such an image:

![runflow-qrcode](/images/runflow-qrcode-color.png)

## Argument Reference

* `filename` - (Required, str) The path to the output image file.
* `data` - (Required, str) The data string to be encoded.
* `version` - (Optional, int) An integer from 1 to 40 that controls the size of the QR Code. The smallest version 1 is a 21x21 matrix. When not set or set to null, the size will be automatically calculated.
* `error_correction` - (Optional, int) The error correction used for the QR Code. When set to 0, about 7% or less errors can be corrected. When set to 1, about 15% or less errors can be corrected. When set to 2, about 25% or less errors can be corrected. When set to 3, about 30% or less errors can be corrected. Default is 1.
* `box_size` - (Optional, int) How many pixels each "box" of the QR code is. Default is 10.
* `border` - (Optional, int) How many boxes thick the border should be. It should be a number greater than 4. Default is 4.
* `image` - (Optional, map) Advanced settings for the image generation.
  * `back_color` - (Optional, str or tuple) The background color.
  * `fill_color` - (Optional, str or tuple) The filling color.

## Attributes Reference

* `image` - A PIL image instance.
