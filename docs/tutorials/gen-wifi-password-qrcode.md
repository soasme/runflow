---
sidebar: auto
---

# Generate WiFi Credential QRCode Card

## Overview

It's a good practice to set a random sequence of characters for your
WiFi password, such as `1k3dk038dkd077xlsqosal3`.

It'd be an issue for your guest though - It's hard for them to type
these annoying characters.

To solve this problem, you can print out a QRCode and stick it in front
of your fridge. Whoever visiting your house can simply scan the QRCode
and connect to your WiFi.

## WiFi-Credential-Card Flow

<<< @/examples/wifi_credential_qrcode.hcl

::: details Click me to view run output
Run
```bash
$ runflow run examples/wifi_credential_qrcode.hcl --var output=print.png
[2021-07-13 15:37:11,876] "task.hcl2_template.login" is started.
[2021-07-13 15:37:11,876] "task.hcl2_template.login" is successful.
[2021-07-13 15:37:11,876] "task.qrcode_generate.card" is started.
[2021-07-13 15:37:11,946] "task.qrcode_generate.card" is successful.
```
:::

Got it! Now scan the file `print.png` using your Phone camera and have it a try.

