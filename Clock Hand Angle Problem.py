



def clock_hand_angle(hour: int, minutes: int):
    """
    Things to keep in mind
    :param hour: int in range [0, 11] where 0 = 12:00
    :param min: int in range [0, 59] where 0 = 0 min (duh)
    :return: returns an integer, from [0, 359] between the two hands

    1) first we note that the minute hand moves 6 degrees per minute and the hour hand
        must move 30 degrees per minute. But, the hour hand also moves based on minutes as well!
        How many degrees does the minute value offset the hour hand?

        Since 60 minutes must pass in order for the hour hand to move 30 degrees,
        one minute tacks on 0.5 degrees to the hour hand's location.

        So we can actually come up with a formula for the respective degree each hand is pointing at
        angle of hour hand = (hour * 30 degrees) + (min * 0.5)
        angle of min hand  = (min * 6 degrees)

        We define pointing straight up (at 12:00) as 0 degrees.
    """
    hour_angle = hour * 30 + minutes * 0.5
    min_angle = minutes * 6

    # don't forget we want to return the smaller angle
    return min(abs(hour_angle - min_angle), abs(min_angle - hour_angle))



print(clock_hand_angle(3, 30)) # 75
print(clock_hand_angle(0, 30)) # 165





