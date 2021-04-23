#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("7d07150e-1682-4c90-ba5f-575f5569a06a", "")
    APP_PASSWORD = os.environ.get("YASw2BTHr4fgk4_8Y72BtQzNj.zt-_dv6w", "")
