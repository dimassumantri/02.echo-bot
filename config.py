#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "ac8027f8-2716-48d3-b962-ecbfcf49f958")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", ".BMoVX-uIZ-B3TWY6iEo05F_r1gq7H~ltQ")
