from classes import Student as s

student1 = s.Student('Ala', 87)
student2 = s.Student('Franek', 7)
student2.marks = 30

print(student1.is_passed(), student2.is_passed())
