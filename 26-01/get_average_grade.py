def get_average_grade(scores):
    avg = sum(scores)/len(scores)

    score_dict = {
        avg >= 0 : "F",
        avg >= 60 : "D-",
        avg >= 63 : "D",
        avg >= 67 : "D+",
        avg >= 70 : "C-",
        avg >= 73 : "C",
        avg >= 77 : "C+",
        avg >= 80 : "B-",
        avg >= 83 : "B",
        avg >= 87 : "B+",
        avg >= 90 : "A-",
        avg >= 93 : "A",
        avg >= 97 : "A+",
    }
    
    return score_dict[True]

print(get_average_grade([84, 89, 85, 100, 91, 88, 79]))