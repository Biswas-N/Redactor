import argparse


def main():
    # Download data
    pass

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--incidents", type=str, required=True,
                            help="Incident summary url.")

    args = arg_parser.parse_args()
    if args.incidents:
        main(args.incidents)