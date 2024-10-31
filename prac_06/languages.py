"""CP1404 Prac 06 - languages
estimated time : 15 minutes
Started at: 9:30
finished at: 9:45
"""
from prac_06.programming_language import ProgrammingLanguage


def main():
    """Run the programming language example"""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamic programming languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
