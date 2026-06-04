from enum import StrEnum


class StudyMode(StrEnum):
    daily_communication = "daily_communication"
    academic_purpose = "academic_purpose"


class CEFRLevel(StrEnum):
    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"


class Skill(StrEnum):
    listening = "listening"
    reading = "reading"
    writing = "writing"
    speaking = "speaking"


class ObjectiveType(StrEnum):
    communicative_goal = "communicative_goal"
    grammar = "grammar"
    vocabulary = "vocabulary"
    listening = "listening"
    speaking = "speaking"
    reading = "reading"
    writing = "writing"
    culture = "culture"
    academic_certification = "academic_certification"
