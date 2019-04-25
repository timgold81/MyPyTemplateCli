import signal
import argparse


def signal_handler(signal, frame):
    # if needed to stop some kind of main loop
    # config.loop=0
    print("\nStopping PROGRAM NAME. Thanks for using.")
    print("Please visit https://github.com/timgold81/")
    print("contact timgold@gmail.com\n")


class Config:
    loop = 1
    some_argument = ""

    def handle_args(self):
        parser = argparse.ArgumentParser(description="PROGRAM NAME. A PROGRAM \
            THAT DOES XXX")
        parser.add_argument("-s", "--some_arg", help="SOME ARGUMENT THAT \
            DOES SOMETHING")
        args = parser.parse_args()

        if args.some_arg:
            self.some_argument = args.some_arg
        else:
            self.some_argument = "NONE"


if (__name__ == "__main__"):
    signal.signal(signal.SIGINT, signal_handler)
    global config
    config = Config()
    config.handle_args()
