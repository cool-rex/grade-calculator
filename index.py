score = int(input("Enter score: "))


def calculte_grade(score):
    if score >= 80:
        return "A"
    if score >= 75:
        return "B+"
    if score >= 70:
        return "B"
    if score >= 65:
        return "C+"
    if score >= 60:
        return "C"
    if score >= 55:
        return "D+"
    if score >= 50:
        return "D"
    if score >= 45:
        return "E"
    if score >= 40:
        return "F"


print("your grade is: " + calculte_grade(score))
