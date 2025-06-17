# Import Required Libraries
from tkinter import *
import datetime
import time
import winsound
from threading import *
import wave
import contextlib

# Create Tkinter Window
root = Tk()
root.geometry("400x250")
root.title("Alarm Clock")

# Global flag to stop alarm
stop_alarm_flag = False

# Function to get WAV duration
def get_wav_duration(filename):
    with contextlib.closing(wave.open(filename, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        return frames / float(rate)

# Function to stop the alarm
def stop_alarm():
    global stop_alarm_flag
    stop_alarm_flag = True
    winsound.PlaySound(None, winsound.SND_PURGE)  # Stop sound

# Function to start alarm thread
def Threading():
    global stop_alarm_flag
    stop_alarm_flag = False
    t1 = Thread(target=alarm)
    t1.start()

# Alarm logic
def alarm():
    set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    print(f"Alarm set for: {set_alarm_time}")

    while True:
        if stop_alarm_flag:
            print("Alarm stopped before time")
            break

        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        # Check if current time matches alarm time
        if current_time == set_alarm_time:
            print("Time to Wake up!")
            sound_file = "mixkit-rooster-crowing-in-the-morning-2462.wav"
            duration = get_wav_duration(sound_file)
            print(f"Sound duration: {duration:.2f} seconds")

            start_time = time.time()
            while time.time() - start_time < 10:
                if stop_alarm_flag:
                    print("Alarm stopped manually")
                    return
                winsound.PlaySound(sound_file, winsound.SND_ASYNC)
                time.sleep(duration)
            break

        # Only print current time once per second while checking
        print("Checking time:", current_time)
        time.sleep(1)

# UI: Labels and time selectors
Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
Label(root, text="Set Time (24-hour format)", font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack(pady=5)

# Hour dropdown
hour = StringVar(root)
hours = [f"{i:02d}" for i in range(0, 24)]
hour.set(hours[0])
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

# Minute dropdown
minute = StringVar(root)
minutes = [f"{i:02d}" for i in range(0, 60)]
minute.set(minutes[0])
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

# Second dropdown
second = StringVar(root)
seconds = [f"{i:02d}" for i in range(0, 60)]
second.set(seconds[0])
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

# Buttons to set and stop alarm
Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=10)
Button(root, text="Stop Alarm", font=("Helvetica 15"), command=stop_alarm).pack()

# Run the Tkinter event loop
root.mainloop()