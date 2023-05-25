# import multiprocessing as mp
# import os
# from Drone import main as drone_main
# from OCR import main as ocr_main
#
# def run_drone():
#     drone_main()
#
# def run_ocr():
#     ocr_main()
#
# if __name__ == '__main__':
#     drone_process = mp.Process(target=run_drone)
#     ocr_process = mp.Process(target=run_ocr)
#
#     drone_process.start()
#     ocr_process.start()
#
#     drone_process.join()
#     ocr_process.join()
# ---
import multiprocessing as mp
import os
import signal
from Drone import main as drone_main
from OCR import main as ocr_main

def run_drone():
    drone_main()

def run_ocr():
    ocr_main()

if __name__ == '__main__':
    drone_process = mp.Process(target=run_drone)
    ocr_process = mp.Process(target=run_ocr)

    drone_process.start()
    ocr_process.start()

    try:
        while True:
            user_input = input("Press 'q' to quit: ")
            if user_input == 'q':
                break
    except KeyboardInterrupt:
        pass
    finally:
        # Terminate the processes
        drone_process.terminate()
        ocr_process.terminate()

        # Wait for the processes to finish
        drone_process.join()
        ocr_process.join()
