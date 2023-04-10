import tellopy
import time
import logging
import threading

# Tello 드론 객체 생성
drone = tellopy.Tello()

# 드론 연결 함수
def connect_drone():
    try:
        drone.connect()
    except Exception as ex:
        logging.error('Could not connect to Tello drone: {}'.format(ex))

# 배터리 수준 체크 함수
def check_battery_level():
    while True:
        try:
            battery = drone.get_battery()
            logging.info('Current battery level: {}%'.format(battery))

            # 임계치 이하일 때 알림 보내기
            if battery < 30:
                send_low_battery_notification()
        except Exception as ex:
            logging.error('Error while checking battery level: {}'.format(ex))

        time.sleep(30)  # 30초마다 체크

# 배터리 임계치 이하일 때 알림 보내는 함수
def send_low_battery_notification():
    # 여기에 알림 보내는 코드 작성
    logging.warning('Low battery level detected! Sending notification...')

# 드론 연결 쓰레드 실행
connect_drone_thread = threading.Thread(target=connect_drone)
connect_drone_thread.daemon = True
connect_drone_thread.start()

# 드론 연결 대기
while not drone.is_connected:
    time.sleep(1)

# 배터리 수준 체크 쓰레드 실행
check_battery_thread = threading.Thread(target=check_battery_level)
check_battery_thread.daemon = True
check_battery_thread.start()

# 계속 실행하기 위해 대기
while True:
    time.sleep(1)