distance_mi = 10
is_raining = True
has_bike = True
has_car = False
has_ride_share_app = False

if not distance_mi:
    print(False)
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
elif 1 <= distance_mi <= 6:
    if not is_raining and has_bike:
        print(True)
    else:
        print(False)
elif distance_mi >= 6:
    if not has_ride_share_app and not has_car:
        print(False)
    else:
        print(True)
