from typing import Any


class Settings(object):
    SUPPORTED_REDACTS: list[str] = ['names']

    def __init__(self,
                 input: list[str],
                 output: str,
                 redacts: dict[str, bool]) -> None:

        self.input = input
        self.output = output
        self.redacts = redacts

    def __eq__(self, __o: object) -> bool:
        # Finding if the inputs list in self and __o are equal
        # irrespective of their order
        # Eg: ['*.txt', '*.csv'] == ['*.csv', '*.txt']
        input_intersections = frozenset(__o.input).intersection(self.input)
        if len(input_intersections) != len(self.input):
            return False

        # Checking if 'output' variables are equal
        if self.output != __o.output:
            return False

        # Checking if 'redacts' are equal
        if len(__o.redacts) != len(self.redacts):
            return False

        redact_indexes = list(frozenset(__o.redacts))
        for i in redact_indexes:
            if __o.redacts[i] != self.redacts[i]:
                return False

        return True

    def __str__(self) -> str:
        return f'Settings (\n\tinput: {str(self.input)}\n\toutput: {str(self.output)}\n\tredacts: {str(self.redacts)}\n)'

    @staticmethod
    def parse(args: dict[str, Any]):
        redacts: dict[str, bool] = {k: v for (k, v) in args.items(
        ) if k in Settings.SUPPORTED_REDACTS and v is True}

        return Settings(
            input=args['input'],
            output=args['output'],
            redacts=redacts
        )
