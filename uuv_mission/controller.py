def pd_controller(references, depths, time):
    kp = 0.15
    kd = 0.6
    if time > 0:
        error_1 = references[time] - depths[time, 1] # error at time t
        error_0 = references[time-1] - depths[time-1, 1] # error at time t-1
    else:
        error_1 = references[time] - depths[time, 1] 
        error_0 = 0

    control_action = kp * error_1 + kd * (error_1 - error_0)
    return control_action