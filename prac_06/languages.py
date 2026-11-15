from prac_06.programming_language import ProgrammingLanguage

def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    java = ProgrammingLanguage("Java", "Static", True, 1995)
    c = ProgrammingLanguage("c++","static", False , 1983)
    # print(python)
    #     # print(java)
    #     # print(c)
    #     # print(ruby)
    #     # print(visual_basic)


    languages = [python, java, c, ruby, visual_basic]
    print("the dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic(typing = True):
            print(language.name)

main()