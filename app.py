import time
import multiprocessing
import argparse
import signal

def load_cpu(target_percent, stop_event, interval=0.1):
    busy_time = interval * target_percent / 100.0
    idle_time = interval - busy_time
    while not stop_event.is_set():
        start = time.time()
        while (time.time() - start) < busy_time:
            if stop_event.is_set():
                return
        time.sleep(idle_time)

def main():
    parser = argparse.ArgumentParser(description="CPU Stress")
    parser.add_argument("-c", type=int, default=1, help="CPU cores to load")
    parser.add_argument("-l", type=int, default=80, help="CPU load per core in percent 0...100")
    args = parser.parse_args()
    stop_flag = multiprocessing.Event()
    def signal_handler(signum, frame):
        print(f"\nStopping...")
        stop_flag.set()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    print(f"Starting CPU stress: {args.c} core(s) at {args.l}% load each")

    workers = []
    for _ in range(args.c):
        p = multiprocessing.Process(target=load_cpu, args=(args.l, stop_flag))
        p.start()
        workers.append(p)
    try:
        while any(p.is_alive() for p in workers):
            time.sleep(0.2)
    except KeyboardInterrupt:
        stop_flag.set()
    for p in workers:
        p.join()

if __name__ == "__main__":
    main()
