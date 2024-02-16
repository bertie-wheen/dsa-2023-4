from argparse import Namespace

from lib.tui.app import DSAApp


def run(args: Namespace) -> None:
    app = DSAApp(args)
    app.run()
