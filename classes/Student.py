class Student:
    def __init__(self, name, marks) -> None:
        self._name = name
        self._marks = marks

    @property
    def name(self) -> str:
        return self._name

    @property
    def marks(self) -> int:
        return self._marks
    @marks.setter
    def marks(self, marks: int) -> None:
        self._marks = marks

    def __str__(self):
        return f'Imię: {self.name}'
    
    def is_passed(self) -> None:

        return self.marks > 50
