import sys

from runtime.display_manager import DisplayManager


def main():
    dm = DisplayManager()
    
    if len(sys.argv) > 1:
        dm.run_tui(sys.argv[1])
    else:
        dm.run_cli()


if __name__ == '__main__':
    main()
