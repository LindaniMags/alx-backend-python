#!/usr/bin/env python3
"""
annotate the below function's parameters.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    returns values with the appropriate types.
    """

    return [(i, len(i)) for i in lst]
