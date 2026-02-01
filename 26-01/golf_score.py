def golf_score(par, strokes):
    if strokes == 1:
        return "Hole in one!"
    
    if par - strokes  == 2:
        return "Eagle"
    
    if par - strokes == 1:
        return "Birdie"
    
    if par == strokes:
        return "Par"
    
    if strokes - par == 1:
        return "Bogey"
    
    if strokes - par == 2:
        return "Double bogey"

    return "ELF"

print(golf_score(5, 7))