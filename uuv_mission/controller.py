def pd_controller(references, depths):
    print('this is the x time this function is called')
    kp = 0.15
    kd = 0.6
    error_1 = references[1] - depths[1, 0] # error at time t
    error_0 = references[0] - depths[0, 0] # error at time t-1
    control_action = kp * error_0 + kd * (error_0 - error_1)

    return control_action