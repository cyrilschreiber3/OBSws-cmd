import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--stream", type=str, dest="stream", choices=["status", "start", "stop"], help="starts or stops the stream")
parser.add_argument("-r", "--record", type=str, dest="record", choices=["status", "start", "stop"], help="starts or stops the recording")
parser.add_argument("-R", "--replay", type=str, dest="replay", choices=["status", "start", "stop", "save"], help="starts, stops or save the replay")
parser.add_argument("-c", "--change-scene", type=str, dest="scene", metavar="scene", help="changes scene")
args = parser.parse_args()

if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)

if args.stream != None:
    print("stream " + args.stream)
if args.record != None:
    print("recording " + args.record)
if args.replay != None:
    print("replay " + args.replay)
if args.scene != None:
    print("scene " + args.scene)