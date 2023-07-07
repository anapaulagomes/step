from dataclasses import dataclass, field
from typing import Any, Callable, List, Optional


def callback(*args, **kwargs):
    pass


@dataclass
class Step:
    title: str
    description: str = ""
    sub_steps: List[Any] = field(default_factory=list)
    function: Optional[Callable] = field(default_factory=callback, repr=False)
