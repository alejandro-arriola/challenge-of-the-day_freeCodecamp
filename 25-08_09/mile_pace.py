def mile_pace(miles:int, duration:str) -> str:
    duration = duration.split(":")
    duration = (int(duration[0]) * 60 + int(duration[1])) // miles
    duration = [ int(duration // 60) , int(duration % 60) ]
    
    return str(duration[0]).zfill(2) + ":" + str(duration[1]).zfill(2)

print(mile_pace(26.2, "120:35")) #return "03:30".