from dataclasses import dataclass, field
from typing import Any, Callable, List


@dataclass
class Step:
    title: str
    description: str = ""
    sub_steps: List[Any] = field(default_factory=list)
    function: Callable = lambda x: x  # noqa
