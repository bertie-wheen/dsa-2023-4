import sys

import lib.cli
import lib.tui
from lib.arg_parser import DSAArgumentParser

parser = DSAArgumentParser()

try:
    args = parser.parse_args()
except KeyError:
    print("ERROR: invalid command-line arguments given\n")
    parser.print_help()
    sys.exit(1)

if args.component is not None and args.component.full_id == "labs.lab5.plus.ecs":
    from lab5.plus.ecs import Pong

    pong = Pong()
    pong.run()
else:
    match args.interface:
        case "cli":
            lib.cli.run(args)
        case "tui":
            lib.tui.run(args)
