def format_duration(seconds):
    minute = 60
    hour = 3600
    day = 86400
    year = 31536000

    year_count = seconds // year
    seconds %= year #shorthand for seconds = seconds % year
    day_count = seconds // day
    seconds %= day
    hour_count = seconds // hour
    seconds %= hour
    minute_count = seconds // minute
    seconds %= minute
    
    parts = []
    if year_count:
        parts.append(f"{year_count} year" + ("s" if year_count > 1 else ""))
    if day_count:
        parts.append(f"{day_count} day" + ("s" if day_count > 1 else ""))
    if hour_count:
        parts.append(f"{hour_count} hour" + ("s" if hour_count > 1 else ""))
    if minute_count:
        parts.append(f"{minute_count} minute" + ("s" if minute_count > 1 else ""))
    if seconds:
        parts.append(f"{seconds} second" + ("s" if seconds > 1 else ""))
        
    if len(parts) > 1:
        return ", ".join(parts[:-1]) + " and " + parts[-1]
    elif parts:
        return parts[0]
    else:
        return "now"
    
