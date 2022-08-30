def study_schedule(permanence_period, target_time):
    counter = 0
    for first, second in permanence_period:
        if not isinstance(first, int) or not isinstance(second, int):
            return None
        if not isinstance(target_time, int):
            return None
        if first <= target_time and second >= target_time:
            counter += 1
    return counter
