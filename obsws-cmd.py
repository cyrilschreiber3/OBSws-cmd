import sys
import argparse
import asyncio
import actions

# Create parser
parser = argparse.ArgumentParser()
parser.add_argument("-S", "--start", dest="start", action='store_true', help="Start OBS in mimized mode with replay enabled")
parser.add_argument("-s", "--stream", type=str, dest="stream", choices=["status", "start", "stop"], help="starts or stops the stream")
parser.add_argument("-r", "--record", type=str, dest="record", choices=["status", "start", "stop"], help="starts or stops the recording")
parser.add_argument("-R", "--replay", type=str, dest="replay", choices=["status", "start", "stop", "save"], help="starts, stops or save the replay")
parser.add_argument("-c", "--change-scene", type=str, dest="scene", metavar="scene", help="changes scene")
parser.add_argument("-C", "--change-scene-profile", type=str, dest="scene_pr", metavar="profile", help="changes scene profile")
args = parser.parse_args()

# parser logic
if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    # sys.exit(1)

if args.stream != None:
    asyncio.run(actions.stream(args.stream))
elif args.record != None:
    asyncio.run(actions.recording(args.record))
elif args.replay != None:
    asyncio.run(actions.replay(args.replay))
elif args.scene != None:
    asyncio.run(actions.chngScene(args.scene))
elif args.start == True:
    actions.startobs()
elif args.scene_pr != None:
    asyncio.run(actions.chngSceneProfile(args.scene_pr))
