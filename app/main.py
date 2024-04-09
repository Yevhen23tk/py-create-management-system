from dataclasses import dataclass
import pickle
from datetime import datetime


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as p_file:
        pickle.dump(groups, p_file)

    return max(([len(student.students) for student in groups]), default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file_st:
        pickle.dump(students, file_st)

    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as gr_file:
        file_gr = pickle.load(gr_file)
        return set([gr.specialty.name for gr in file_gr])


def read_students_information() -> list:
    with open("students.pickle", "rb") as st_file:
        return pickle.load(st_file)
