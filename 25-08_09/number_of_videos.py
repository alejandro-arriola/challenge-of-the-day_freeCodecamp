def number_of_videos(video_size, video_unit, drive_size, drive_unit):
    match video_unit:
        case "KB":
            video_size = video_size * 1000
        case "MB":
            video_size = video_size * 1000_000
        case "GB":
            video_size = video_size * 1000_000_000
        case _:
            return "Invalid video unit"
    
    match drive_unit:
        case "GB":
            drive_size = drive_size * 1000_000_000
        case "TB":
            drive_size = drive_size * 1000_000_000_000
        case _:
            return "Invalid drive unit"
            
    return int(drive_size//video_size)

print(number_of_videos(1, "TB", 10, "TB"))