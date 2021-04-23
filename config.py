#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "94d0f980-12c5-4c0c-a5b1-0444be6f51d8")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "z.EUA2foIn_HB6~hFuXmEgf-5kn~F8Id2k")
