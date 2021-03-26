#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright (C) 2021 Daniele Viganò <daniele@vigano.me>
#
# BITE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BITE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import csv
import time
import shutil
import argparse

from datetime import datetime, timedelta
from ptftplib import tftpclient


def main(args):
    while True:
        with open(args.csv_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            if not os.path.exists('data'):
                os.mkdir('data')
            os.chdir('data')
            for row in csv_reader:
                if row[0].startswith("#"):
                    continue

                serial = row[0]
                ip_address = row[1]

                src = "*.{ext}".format(ext=args.ext)
                dest = "{serial}_{datetime}.{ext}".format(
                    serial=serial,
                    datetime=datetime.now().strftime("%Y%m%d%H%M%S"),
                    ext=args.ext
                )

                tftp = tftpclient.TFTPClient((ip_address, 69), mode='octet')
                tftp.connect()
                tftp.get(['-f', src])
                tftp.finish()
                shutil.move(src, dest)  # an ugly hack

        next_time = datetime.today() + timedelta(hours=args.delay)
        print("Wait for the next iteration at {next_time}".format(
            next_time=next_time))
        time.sleep(args.delay * 60 * 60)  # hours


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file",
                        help="CSV file to be parsed")
    parser.add_argument("--ext", "-e", type=str, default="log",
                        help="File extension to be used (default: log)")
    parser.add_argument("--delay", "-d", type=int, default=12,
                        help="Delay between collections in hrs (default: 12)")
    args = parser.parse_args()

    main(args)
