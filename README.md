# Deeplearning-Noticer
In this project, two programs can help you take full agvantage of time on the model training with a remote server, which can push notification to your phone about the information during model training, like the model indices and unexpected interrupts. Then you can do something in time for your work.:blush:
<div align=center>
<img src="https://github.com/Gray-OREO/Deeplearning-Noticer/blob/main/images/0.png" width="500px">
</div>

## What's them?
### notice.py
In this program, the notification to be pushed can be conducted based the IFTTT App on your phone, and the Webhooks can help the trigger setting. Firstly, you shoule login the IFTTT and create a new applet with the trigger of 'Receive a web request'. Then, you should setting an Event Name, one of two parameters needed in this porgrame. Next, you should choose the notification as the response for that trigger. After the format setting, you can click 'Finish' for next phase. Clicking the Webhooks icon you will get your personal Key in the 'Documentation', another parameter in notice.py. And replace the parameters in code, you can get the notification on your phone.

<div align=center>
<img src="https://github.com/Gray-OREO/Deeplearning-Noticer/blob/main/images/a.PNG" width="300px"><img src="https://github.com/Gray-OREO/Deeplearning-Noticer/blob/main/images/b.jpg" width="300px">
</div>
Message format for the notification.

### GPU_pm.py
This is a program which can monitoring specified process on GPU. Firstly, you should know the PID by 'nvidia-smi' on terminal. After typing the PID, the program will monitor the state of this process, which will notices you when the process over or be killed.

## How to use?
1. Seeting the parameters in notice.py.
2. Run your own deeplearning program.
3. Run GPU_pm.py and type in the PID of your own program.
