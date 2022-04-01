import argparse
import glob
import os
from pathlib import Path

from project1 import redact_pipeline
from project1.models import Settings


def main(settings: Settings):
    # Getting input files
    input_files = []
    for i in settings.input:
        input_files += glob.glob(i)

    print('\nFiles processing ->', input_files, '\n')
    # Creating output path irrespective of OS (Windows and Posix)
    output_path = Path(os.path.join(os.getcwd(), settings.output)).resolve()

    for raw_file in input_files:
        input_file = Path(raw_file).resolve()
        output_file_folder = Path(os.path.join(output_path, raw_file)).parent
        Path(output_file_folder).resolve().mkdir(parents=True, exist_ok=True)
        output_file = os.path.join(
            output_file_folder,
            f'{Path(raw_file).stem}.redacted')

        print(f'Redacting {raw_file} -> {output_file}')

        with open(input_file, 'r') as in_f, open(output_file, 'w') as out_f:
            unredacted_txt = in_f.read()
            redacted_txt = redact_pipeline(unredacted_txt, settings.redacts)

            out_f.write(redacted_txt)


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(
        description='Redacts sensitive content based on given flags.')
    arg_parser.add_argument(
        "--input",
        required=True,
        action="append",
        help="glob of input files (eg:'*.txt')")
    arg_parser.add_argument(
        "--output",
        required=True,
        help="directory to store redacted files")
    arg_parser.add_argument(
        "--names",
        action="store_true",
        help="redacts any type of names")

    args = arg_parser.parse_args()
    settings = Settings.parse(vars(args))
    print(settings)

    main(settings)
