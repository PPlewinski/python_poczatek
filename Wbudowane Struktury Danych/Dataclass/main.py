from dataclasses import dataclass, field
from typing import ClassVar
from typing import List

@dataclass(frozen = True)
class Subject:
    identifier: str
    name: str
    is_obligatory: bool
    teachers_names: List[str] = field(default_factory=list)
    FAILING_GRADE: ClassVar = 1


mathematics = Subject(identifier = '1', name = 'Mathematics', is_obligatory = True)
print(mathematics)
print(mathematics.FAILING_GRADE)