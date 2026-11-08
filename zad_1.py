class Student:
    def __init__(self, name, marks) -> None:
        self._name = name
        self._marks = marks

    @property
    def name(self) -> str:
        return self._name

    @marks.setter
    def marks(self, marks: int) -> None:
        self._marks = marks

    def is_passed(self) -> None:

        return self._marks > 50


student1 = Student('Ala', 87)
student2 = Student('Franek', 7)

print(student1.is_passed(), student2.is_passed())
