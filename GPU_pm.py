import sys
import pynvml  # 获取GPU信息
import time
from datetime import datetime
from notice import send_notice

print('Please type the process ID on GPU_0 to be supervised:')
pid = input()
print('Begin the monitoring of process_{} on GPU_0...', pid)
while 1:
    time.sleep(1)
    print('GPU_Monitor=======PID:{}======={}================='
          .format(pid, datetime.now().strftime("%m/%d_%H:%M:%S")))
    pynvml.nvmlInit()
    gpu_id = 0
    handle = pynvml.nvmlDeviceGetHandleByIndex(gpu_id)
    info_list = pynvml.nvmlDeviceGetComputeRunningProcesses(handle)
    pynvml.nvmlShutdown()

    stat = 0
    for each_pidinfo in info_list:
        # print(type(each_pidinfo))
        # print(each_pidinfo.__dict__)  # 打印pid的属性
        # print(each_pidinfo.pid)1
        if each_pidinfo.pid==int(pid):
            stat = 1
            print('Every thing is OK~')
            break
        else:
            continue

    if not stat:
        print('Process{} is not on GPU'.format(pid))
        Text = "Learning over or breakdown, good luck..."
        send_notice(Text)
        sys.exit()
