def study_schedule(permanence_period, target_time):
    counter = 0
    try:
        for first, second in permanence_period:
            if first <= target_time and second >= target_time:
                counter += 1
        return counter
    except:
        return None
