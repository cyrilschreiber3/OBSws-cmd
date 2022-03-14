import sys
import getopt

def main(argv):
    help_message = """usage: obsws-cmd [-s, --stream (start|stop)] [-r, --record (start|stop)]
                 [-R, --replay (start|stop|save)] [-c, --change-scene <scene>]"""
    try:
        opts, args = getopt.getopt(argv, "hs:r:R:c:", ["stream=", "record=", "replay=", "change-scene="])
    except getopt.GetoptError:
        print(help_message)
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print(help_message)
        elif opt in ("-s", "--stream"):
            print("stream " + arg)
        elif opt in ("-r", "--record"):
            print("recording " + arg)
        elif opt in ("-R", "--replay"):
            print("replay " + arg)
        elif opt in ("-c", "--change-scene"):
            print("change to scene " + arg)


if __name__ == "__main__":
   main(sys.argv[1:])