from dataclasses import dataclass
from typing import List, Any, Callable


@dataclass
class Step:
    title: str
    description: str
    sub_steps: List[Any]  # to handle the lack of self
    function: Callable = lambda x: x
