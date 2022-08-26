from plyer import notification
import time
i = 0
if __name__ == '__main__':
    while i <= 2:
        notification.notify(title="** Take Rest **",
                            message="Rest is vital for better health",
                            timeout=5)
        i += 1
        time.sleep(60*60)
 