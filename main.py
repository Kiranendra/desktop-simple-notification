from plyer import notification
from time import sleep

print("\n\tDO NOT CLOSE THE COMMAND PROMPT")
while True:
    notification.notify(
        title='IMPORTANT',
        message='PLEASE DRINK A GLASS OF WATER',
        timeout=9
    )
    sleep(3600) # 60 (seconds) = 1 minute
