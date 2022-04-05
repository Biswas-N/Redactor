import argparse
import glob
import os
from pathlib import Path
import sys

from project1 import redact_pipeline
from project1.models import Settings


def main(settings: Settings):
    # Getting input files
    input_files = []
    for i in settings.input:
        input_files += glob.glob(i)

    print('\nFiles processing ->', input_files, '\n')

    process_stats = []
    for input_file in input_files:
        redacted_txt = ""

        input_file_path = Path(input_file).resolve()
        try:
            with open(input_file_path, 'r') as in_f:
                unredacted_txt = in_f.read()
                redacted_txt, stats = redact_pipeline(
                    unredacted_txt,
                    redacts=settings.redacts,
                    concepts=settings.concepts)

                process_stats.append(
                    f"========== Stats:{input_file} ==========\n{stats}")

        except BaseException:
            sys.stderr.write(f'Could not read and redact {input_file}\n\n')
            continue

        if settings.output == 'stdout' or settings.output == 'stderr':
            print(f'Redacting {input_file} ->')
            output_to_std(redacted_txt, settings.output)
        else:
            # Creating output path irrespective of OS (Windows and Posix)
            output_file_folder = Path(
                os.path.join(
                    settings.output,
                    input_file)).parent
            output_file_folder.resolve().mkdir(parents=True, exist_ok=True)
            output_file = Path(os.path.join(
                output_file_folder,
                f'{Path(input_file).stem}.redacted'))

            print(f'Redacting {input_file} -> {output_file.resolve()}')
            output_to_file(redacted_txt, output_file)

        print(f'Stats added to {settings.stats}\n')

    if settings.stats == 'stdout' or settings.stats == 'stderr':
        output_to_std("\n\n".join(process_stats), settings.stats)
    else:
        output_file = Path(os.path.join(os.getcwd(), settings.stats))
        output_to_file("\n\n".join(process_stats), output_file)


def output_to_std(content: str, output: str):
    old_stdout_state = sys.stdout
    if output == 'stderr':
        sys.stdout = sys.stderr

    sys.stdout.write(content)
    sys.stdout.write('\n\n')

    sys.stdout = old_stdout_state


def output_to_file(content: str, output_file: Path):
    with open(output_file.resolve(), 'w', encoding='utf-8') as out_f:
        out_f.write(content)


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(
        description='Redacts sensitive content in a given file.')
    arg_parser.add_argument(
        "--input",
        required=True,
        action="append",
        help="<Required> glob of input files (eg:'*.txt')")
    arg_parser.add_argument(
        "--output",
        required=True,
        help="<Required> directory to store redacted files")
    arg_parser.add_argument(
        "--names",
        action="store_true",
        default=False,
        help="redacts names (Human, Location and Organizations)")
    arg_parser.add_argument(
        "--genders",
        action="store_true",
        default=False,
        help="redacts gender revealing words (He, She, Father, Mother)")
    arg_parser.add_argument(
        "--dates",
        action="store_true",
        default=False,
        help="redacts dates (Feb 3rd, 03/02/2022, February 3, 2022)")
    arg_parser.add_argument(
        "--phones",
        action="store_true",
        default=False,
        help="redacts phone numbers (only 10 digit phone numbers)")
    arg_parser.add_argument(
        "--address",
        action="store_true",
        default=False,
        help="redacts US based physical addresses")
    arg_parser.add_argument(
        "--concept",
        action='append',
        help='<Required> redacts sentence based on given concept',
        required=True)
    arg_parser.add_argument(
        "--stats",
        required=True,
        help="<Required> mode to show (stdout, stderr) or save redacted files")

    args = arg_parser.parse_args()
    settings = Settings.parse(vars(args))

    try:
        main(settings)
    except Exception as e:
        sys.stderr.write("Unexpected error occured!\n")
