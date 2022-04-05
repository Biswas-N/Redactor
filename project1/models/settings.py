from typing import Any


class Settings(object):
    SUPPORTED_REDACTS: list[str] = [
        'names', 'genders', 'dates', 'phones', 'address']

    def __init__(self,
                 input: list[str],
                 output: str,
                 redacts: dict[str, bool],
                 concepts: list[str],
                 stats: str) -> None:

        self.input = input
        self.output = output
        self.redacts = redacts
        self.concepts = concepts
        self.stats = stats

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

        # Checking if 'concepts' are equal
        concepts_intersections = frozenset(
            __o.concepts).intersection(
            self.concepts)
        if len(concepts_intersections) != len(self.concepts):
            return False

        # Checking if 'stats' variables are equal
        if self.stats != __o.stats:
            return False

        return True

    def __str__(self) -> str:
        return f'Settings (\n\tinput: {str(self.input)}\n\toutput: {str(self.output)}\n\tredacts: {str(self.redacts)}\n\tconcepts: {str(self.concepts)}\n\tstats: {str(self.stats)}\n)'

    @staticmethod
    def parse(args: dict[str, Any]):
        redacts: dict[str, bool] = {k: v for (k, v) in args.items(
        ) if k in Settings.SUPPORTED_REDACTS}

        return Settings(
            input=args['input'],
            output=args['output'],
            redacts=redacts,
            concepts=args['concept'],
            stats=args['stats']
        )
