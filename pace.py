def minspermile(minutes,seconds,miles):
    sec_fraction = seconds/60
    total_minutes = minutes + sec_fraction
    pace_fraction = total_minutes / miles
    pace_minutes = int(pace_fraction)
    pace_seconds = round((pace_fraction - pace_minutes) * 60)

    print(f"{pace_minutes} min {pace_seconds:02d} sec")

minspermile(10,13,1)
minspermile(17,17,1.5)
minspermile(23,45,2)
minspermile(28,47,2.5)
minspermile(33,46,3)


'''
1- 10:13
1.5- 17:17
2- 23:45 (beat 19:51)
2.5- 28:47, 29:35
3- 33:46 
3.1- 
'''