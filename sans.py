import winsound
sans = [293, 293, 587, 440, 415, 391, 349, 293, 349, 391]
timing = [100, 100, 100, 200, 100, 100, 250, 100, 100, 100]
for i in range(10):
    winsound.Beep(sans[i], timing[i])
