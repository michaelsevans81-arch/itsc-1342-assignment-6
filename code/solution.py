
# Michael Evans - Assignment 6

def filter_critical_scores(score_list, min_severity=70):
    critical_list = []

    for score in score_list:
        if score > min_severity:
            if score > 100:
                critical_list.append(100)
            else:
                critical_list.append(score)

    return critical_list
