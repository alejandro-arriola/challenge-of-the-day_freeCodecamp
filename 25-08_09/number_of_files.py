def number_of_files(file_size, file_unit, drive_size_gb):
    match file_unit:
        case "MB":
            drive_size_gb = drive_size_gb * 1000
        case "KB":
            drive_size_gb = drive_size_gb * 1000_000
        case "B":
            drive_size_gb = drive_size_gb * 1000_000_000
            
    return int(drive_size_gb//file_size)

print(number_of_files(220.5, "KB", 100))