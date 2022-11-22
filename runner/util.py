def to_pace(distance_in_km, duration_in_min):
    return duration_in_min / distance_in_km

def to_seconds(hours, minutes, seconds):
    return int(hours * 3600 + minutes * 60 + seconds)

def to_minutes(hours, minutes, seconds):
    return hours * 60 + seconds / 60 + minutes
