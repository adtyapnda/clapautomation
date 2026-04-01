# Clap Automation

Control your workflow with a double clap.

This Python script listens for audio input and triggers actions when it detects a double clap, allowing you to instantly launch your development environment.

---

## Features

* Real-time microphone input detection
* Double clap recognition
* Automatically opens:

  * VS Code (specific file or project)
  * YouTube in a new window
  * Terminal session

---

## How It Works

The script continuously listens to microphone input using `sounddevice`, measures volume levels, and detects two claps within a defined time window. Once detected, it triggers predefined system actions.

---

## Requirements

* Python 3.13 (64-bit)

Install dependencies:

```bash id="req91x"
pip install sounddevice numpy
```

---

## Usage

Run the script:

```bash id="run22k"
python clap_automation.py
```

Then clap twice to trigger the actions.

---

## Configuration (Important)

Before running the script, you may need to update the configuration values inside the file:

```python id="conf11p"
VSCODE_PATH = os.environ.get("VSCODE_PATH", "code")
PROJECT_PATH = os.environ.get("PROJECT_PATH", None)
YOUTUBE_URL = "https://www.youtube.com/watch?v=XgWUDbYfNe4&t=6s&autoplay=1"
```

* `VSCODE_PATH`: Replace this if VS Code is not available via the `code` command on your system
* `PROJECT_PATH`: Set this to the file or folder you want to open in VS Code
* `YOUTUBE_URL`: Replace with any URL you want to launch

You can either:

* Edit these values directly in the script, or
* Set them as environment variables on your system

---

## Customization

Modify the following functions to fit your workflow:

* `open_vscode()`
* `open_youtube()`
* `open_terminal()`

---

## Notes

* Works best in a quiet environment
* Requires a functioning microphone
* Default configuration is Windows-based but partially cross-platform

---

## Future Improvements

* Full cross-platform support (macOS and Linux)
* GUI-based configuration
* Custom action mapping
* Background service mode

---

## License

MIT License

---

## Author

Aditya Panda
