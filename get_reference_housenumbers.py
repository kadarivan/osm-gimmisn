#!/usr/bin/env python3
#
# Copyright 2019 Miklos Vajna. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

"""The get_reference_housenumbers module allows fetching referene house numbers for a relation."""

import configparser
import os
import sys
import helpers


def main() -> None:
    """Commandline interface to this module."""

    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), "wsgi.ini")
    config.read(config_path)

    if len(sys.argv) > 1:
        relation_name = sys.argv[1]

    reference = config.get('wsgi', 'reference_local').strip()
    datadir = os.path.join(os.path.dirname(__file__), "data")
    workdir = config.get('wsgi', 'workdir').strip()
    helpers.get_reference_housenumbers(reference, datadir, workdir, relation_name)


if __name__ == "__main__":
    main()

# vim:set shiftwidth=4 softtabstop=4 expandtab:
