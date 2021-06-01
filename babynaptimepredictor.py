# Baby Nap Time Predictor
# This program predicts when a 8-12 month old baby should take their 2 naps a day and bedtime.
# Assumption: 3-3.5 hours of wake time between sleep

def welcome():
    print ("*** WELCOME TO THE BABY NAP TIME PREDICTOR! ***")
    print ("This program will help you predict when it's time for your baby to go to sleep.")
    print ("This program is currently for babies on 2 naps a day.")
    print ("Please enter (i) hours in 24 hours (ii) minutes converted to 2 decimal points.")
    print ("")


def predict_nap1(firstname):
    print ("FIRST NAP TIME PREDICTION")
    # prompt baby sleep & wake times
    bedtime_sleep = float(input("What time did " + str(firstname) + " go to bed the night before? "))
    bedtime_wake = float(input("What time today did " + str(firstname) + " wake up? "))

    # calc how many hours baby slept at night
    if 12 <= bedtime_sleep <= 24:
        sleep_time = (24 - float(bedtime_sleep)) + bedtime_wake
    else:
        sleep_time = bedtime_wake - bedtime_sleep

    # comment + state how many hours baby slept
    if sleep_time < 9:
        print ("Oh no! " + str(firstname) + " did not get enough sleep at only " + str(sleep_time) + " hours. Try to encourage " + str(firstname) + " to sleep between 9-11 hours at night.")
    elif 9 <= sleep_time <= 11:
        print ("Wonderful! " + str(firstname) + " had a good night sleep with " + str(sleep_time) + " hours.")
    else:
        print (str(firstname) + " overslept at " + str(sleep_time) + " hours. Try to limit bedtime sleep between 9-11 hours max.")
    # predict nap1
    predict_nap1_window_start = float(bedtime_wake + 3)
    predict_nap1_window_end = float(bedtime_wake + 3.5)
    # state nap1 prediction
    print (str(firstname) + "'s first nap window will be between " + str(predict_nap1_window_start) + " and " + str(
        predict_nap1_window_end) + ". Good luck!")
    print ("")
    return sleep_time


def predict_nap2(firstname):
    print ("SECOND NAP TIME PREDICTION")
    # prompt baby sleep & wake times for nap1
    nap1_sleep = float(input("What time did " + str(firstname) + " fall asleep for nap 1? "))
    nap1_wake = float(input("What time did " + str(firstname) + " wake up from nap 1? "))
    # calc how many hours baby slept for nap1
    nap1_time = nap1_wake - nap1_sleep

    # comment + state how many hours baby slept
    if nap1_time < 0.5:
        print ("Oh no!" + str(firstname) + " had a light first nap at only " + str(nap1_time) + " hours. Try to encourage baby to sleep at least 30 mins.")
    elif 0.5 <= nap1_time <= 2:
        print ("Wonderful! " + str(firstname) + " had a good first nap at " + str(nap1_time) + " hours.")
    else:
        print (str(firstname) + " overslept at " + str(nap1_time) + " hours. Try to limit naps to 2 hours max.")

    # predict nap2
    predict_nap2_window_start = float(nap1_wake + 3)
    predict_nap2_window_end = float(nap1_wake + 3.5)
    # state nap2 prediction
    print (str(firstname) + "'s second nap window will be between " + str(predict_nap2_window_start) + " and " + str(
        predict_nap2_window_end) + ". Good luck!")
    print ("")
    return nap1_time


def predict_bedtime(firstname):
    print ("BEDTIME PREDICTION")
    # prompt baby sleep & wake times for nap2
    nap2_sleep = float(input("What time did " + str(firstname) + " fall asleep for nap 2? "))
    nap2_wake = float(input("What time did " + str(firstname) + " wake up from nap 2? "))

    # calc how many hours baby slept for nap2
    nap2_time = nap2_wake - nap2_sleep
    # comment + state how many hours baby slept
    if nap2_time < 0.5:
        print ("Oh no! " + str(firstname) + " had a light second nap at only " + str(nap2_time) + " hours. Try to encourage " + str(firstname) + " to sleep at least 30 mins.")
    elif 0.5 <= nap2_time <= 2:
        print ("Wonderful!"  + str(firstname) + " had a good second nap at " + str(nap2_time) + " hours.")
    else:
        print (str(firstname) + " overslept at " + str(nap2_time) + " hours. Try to limit naps to 2 hours max.")

    # predict bedtime
    predict_bedtime_window_start = float(nap2_wake + 3)
    predict_bedtime_window_end = float(nap2_wake + 3.5)
    # state bedtime prediction
    print (str(firstname) + "'s bedtime window will be between " + str(predict_bedtime_window_start) + " and " + str(
        predict_bedtime_window_end) + ". Good luck!")
    print ("")
    return nap2_time


def total_sleep(firstname, sleep_time, nap1_time, nap2_time):
    total_sleep = float(sleep_time + nap1_time + nap2_time)
    print ("TOTAL SLEEP")
    print ("Over the last day, " + str(firstname) + " slept a total of " + str(total_sleep) + " hours.")

def main():
    welcome()
    firstname = raw_input("What is your baby's name? ")
    print ("")
    sleep_time = predict_nap1(firstname)
    nap1_time = predict_nap2(firstname)
    nap2_time = predict_bedtime(firstname)
    total_sleep(firstname, sleep_time, nap1_time, nap2_time)


if __name__ == '__main__':
    main()
