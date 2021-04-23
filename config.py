#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "8588a7d3-3549-454b-988c-7f06967a43d8")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "9m.v8dR-1e23f_sRGArJq2Ids7oq2-zB5u")
