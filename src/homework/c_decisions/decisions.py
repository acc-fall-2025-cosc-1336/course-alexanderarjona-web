def get_options_ratio(option, total):
    return option / total if total != 0 else 0

def get_faculty_rating(ratio):
    if 0.9 <= ratio < 1:
        return "Excellent"
    if ratio > 0.8:
        return "Very Good"
    if ratio > 0.7:
        return "Good"
    if ratio > 0.6:
        return "Needs Improvement"
    return "Unacceptable"
