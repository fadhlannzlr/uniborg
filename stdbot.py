# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging

from uniborg import Uniborg

logging.basicConfig(level=logging.INFO)

borg = Uniborg(
    "stdbot",
    plugin_path="botplugins",
    admins=[12345],
    connection_retries=None
)

borg.run_until_disconnected()
