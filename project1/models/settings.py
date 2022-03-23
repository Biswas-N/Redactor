from typing import Any


class Settings(object):
    def __init__(self, 
        input: list[str], 
        output: str) -> None:
        self.input = input
        self.output = output

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
        
        return True
    
    def __str__(self) -> str:
        return f'Settings (\n\tinput: {str(self.input)}\n\toutput: {str(self.output)}\n)'

    @staticmethod
    def parse(args: dict[str, Any]):
        return Settings(
            input=args['input'],
            output=args['output']
        )
