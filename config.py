#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "aaf8d1e0-abeb-4e04-820c-3ba403435b9f")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", ".hkeq.92-MN13~re_g9gixHuIi6X~61CK0")
