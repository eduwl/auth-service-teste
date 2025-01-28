from typing import TypeVar, Protocol

I = TypeVar('I')
O = TypeVar('O')

class UseCase(Protocol[I, O]):
    def execute(self, input: I) -> O:
        raise NotImplementedError("Must implement execute")