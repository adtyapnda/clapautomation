import sounddevice as sd
import numpy as np
import time
import subprocess
import os
import webbrowser

THRESHOLD = 0.35
CLAP_GAP = 1.5
CLAP_BLOCK_TIME = 0.4

clap_times = []
last_clap_time = 0
triggered = False


# -------- CONFIG --------
VSCODE_PATH = os.environ.get("VSCODE_PATH", "code")
PROJECT_PATH = os.environ.get("PROJECT_PATH", None)
YOUTUBE_URL = "https://www.youtube.com/watch?v=XgWUDbYfNe4&t=6s&autoplay=1" #Back in Black - AC/DC (Iron Man 2 Soundtrack)
# ------------------------


def trigger_actions():
    global triggered
    triggered = True
    print("Double clap detected. Launching...")

    open_vscode()
    time.sleep(1)

    open_youtube()
    time.sleep(1)

    open_terminal()


def open_vscode():
    try:
        if PROJECT_PATH:
            subprocess.Popen([VSCODE_PATH, "-n", PROJECT_PATH])
        else:
            subprocess.Popen([VSCODE_PATH])
    except Exception as e:
        print("Failed to open VS Code (Check for errors)", e)


def open_youtube():
    try:
        webbrowser.open(YOUTUBE_URL)
    except Exception as e:
        print("Failed to open YouTube:", e)


def open_terminal():
    try:
        if os.name == "nt":
            subprocess.Popen(["cmd", "/k"])
        else:
            subprocess.Popen(["gnome-terminal"])
    except Exception as e:
        print("Failed to open terminal:", e)


def detect_clap(indata, frames, time_info, status):
    global clap_times, last_clap_time, triggered

    if triggered:
        return

    volume = np.linalg.norm(indata)
    now = time.time()

    if volume > THRESHOLD:
        if now - last_clap_time < CLAP_BLOCK_TIME:
            return

        last_clap_time = now
        clap_times.append(now)

        clap_times = [t for t in clap_times if now - t <= CLAP_GAP]

        if len(clap_times) >= 2:
            trigger_actions()


def main():
    global triggered

    print("Listening for double claps...")

    try:
        with sd.InputStream(callback=detect_clap):
            while not triggered:
                time.sleep(0.1)
    except KeyboardInterrupt:
        print("Stopped")


if __name__ == "__main__":
    main()