import argparse

from .boilerplate import BoilerPlate

def gen_bp():
    parser = argparse.ArgumentParser(description="Flask Boilerplate Generator")
    parser.add_argument("--dir", help="Path to directory (relative/absolute) where all boilerplate is to be dumped")
    args = parser.parse_args()

    bp = BoilerPlate(path=args.dir)
    bp.run()