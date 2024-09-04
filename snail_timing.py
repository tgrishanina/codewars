def can_snail_reach_end(length, speed, length_increases):
    time = length/ (speed - length_increases)
    if time <= 525600 and time >= 0:
        return True
    else:
        return False