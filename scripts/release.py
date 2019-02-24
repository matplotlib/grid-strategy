#! python3.7

import glob
import subprocess


def upload(release):
    if release:
        repository = ["-r", "pypi"]
    else:
        repository = ["--repository-url", "https://test.pypi.org/legacy/"]

    dist_files = glob.glob("dists/*")
    args = ["twine", "upload"] + repository + dist_files

    subprocess.check_call(args)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Make a release")
    parser.add_argument(
        "--release", action="store_true", help="Used to make a real release"
    )

    args = parser.parse_args()

    upload(args.release)
