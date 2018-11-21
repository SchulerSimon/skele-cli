"""
skele

Usage:
  skele hello
  skele -h | --help
  skele --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  skele hello

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/rdegges/skele-cli
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import skele.commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items():
        if hasattr(unchained.commands, k) and v:
            module = getattr(unchained.commands, k)
            unchained.commands = getmembers(module, isclass)
            command = [c for c in unchained.commands if
                       c[0].lower() == k.lower()][0][1]
            command = command(options)
            command.run()
