#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "3b6b88c3-b5e7-4202-9c65-e69d65e91220")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "i4zTeVCDBKAPJGO6d.-_.B-6Vi05BR5mKk")
