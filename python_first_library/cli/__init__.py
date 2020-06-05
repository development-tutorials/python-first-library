#!/usr/bin/env python


from argparse import ArgumentParser
from os.path import basename
from sys import argv

from python_first_library import First_Library


__license__ = """
First Python Library example usage script
Copyright (C) 2020 S0AndS0

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


arg_parser = ArgumentParser(prog = basename(argv[0]),
                            usage = '%(prog)s --string "Spam!" --float 4.2',
                            epilog = 'https://github.com/S0AndS0')

arg_parser.add_argument('--string',
                        help = 'String like argument',
                        required = True,
                        type = str)

arg_parser.add_argument('--float',
                        help = 'Optional, float like argument',
                        required = False,
                        default = 1.0,
                        type = float)

arg_parser.add_argument('--license',
                        help = 'Prints license and exits',
                        required = False,
                        default = False,
                        action = 'store_true')

arg_parser.add_argument('--verbose', '-v',
                        help = 'Loudness of this script',
                        action = 'count',
                        default = 0)


args = vars(arg_parser.parse_args())

first_library = First_Library(**args)


def main():
    if args.get('license'):
        print(__license__)
        exit(0)

    first_library.print_keyword_arguments()
