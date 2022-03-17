import os
import sys
import time
import json
import subprocess
import websockets
from datetime import datetime, timedelta

async def stream(action):
    # connecting to OBS
    print("Connecting to OBS...", end=" ", flush=True)
    async with websockets.connect("ws://localhost:4444") as websocket:
        await websocket.send(json.dumps({"request-type":"GetStreamingStatus","message-id":"1"}))
        status_response = json.loads(await websocket.recv())
        if status_response["status"] != "ok":
            print("Error: " + status_response["message-id"] + ", " + status_response["error"])
            sys.exit(1)
        else:
            print("Connected")

        match action:
            case "status":
                # Returning streaming status
                if status_response["streaming"]:
                    print("Stream active")
                else:
                    print("Stream inactive")
            
            case "start":
                # Starting OBS stream
                print("Sending request...", end=" ", flush=True)
                await websocket.send(json.dumps({"request-type":"StartStreaming","message-id":"2"}))
                response = json.loads(await websocket.recv())
                if response["status"] != "ok": # if an error occurs, print the error
                    print("Error: " + response["message-id"] + ", " + response["error"])
                    sys.exit(1)
                elif response["status"] == "ok": # if not, print success
                    print("Stream started")
            
            case "stop":
                # Stopping OBS stream
                print("Sending request...", end=" ", flush=True)
                await websocket.send(json.dumps({"request-type":"StopStreaming","message-id":"2"}))
                response = json.loads(await websocket.recv())
                if response["status"] != "ok":
                    print("Error: " + response["message-id"] + ", " + response["error"])
                    sys.exit(1)
                elif response["status"] == "ok": # if not, print success
                    print("Stream stopped")

async def recording(action):
    # connecting to OBS
    print("Connecting to OBS...", end=" ", flush=True)
    async with websockets.connect("ws://localhost:4444") as websocket:
        await websocket.send(json.dumps({"request-type":"GetRecordingStatus","message-id":"1"}))
        status_response = json.loads(await websocket.recv())
        if status_response["status"] != "ok": # if an error occurs, print the error
            print("Error: " + status_response["message-id"] + ", " + status_response["error"])
            sys.exit(1)
        else:
            print("Connected")

        match action:
            case "status":
                # Returning recording status
                if status_response["isRecording"]:
                    print("Recording active")
                else:
                    print("Recording inactive")

            case "start":
                # Starting OBS recording
                print("Sending request...", end=" ", flush=True)
                await websocket.send(json.dumps({"request-type":"StartRecording","message-id":"2"}))
                response = json.loads(await websocket.recv())
                if response["status"] != "ok": # if an error occurs, print the error
                    print("Error: " + response["message-id"] + ", " + response["error"])
                    sys.exit(1)
                elif response["status"] == "ok": # if not, print success
                    print("Recording started")

            case "stop":
                # Stop OBS recording
                print("Sending request...", end=" ", flush=True)
                await websocket.send(json.dumps({"request-type":"StopRecording","message-id":"2"}))
                response = json.loads(await websocket.recv()) 
                if response["status"] != "ok": # if an error occurs, print the error
                    print("Error: " + response["message-id"] + ", " + response["error"])
                    sys.exit(1)
                elif response["status"] == "ok": # if not, print success
                    print("Recording stopped")
                    time.sleep(2)

                    # Setup file names
                    print("Processing files...", end=" ", flush=True)
                    today = datetime.now()
                    yesterday = today + timedelta(days=-1)
                    fileName = f"{today.strftime('%Y-%m-%d')}"
                    fileName2 = f"{yesterday.strftime('%Y-%m-%d')}"
                    replaysToProcess_paths = [] # list for file names with full paths
                    replaysToProcess_names = [] # list for file names only
                    
                    for file in os.listdir(r"C:\Users\swisscom\Videos"): # Search for the file
                        if file.startswith(fileName): # If file is found, add it to both lists
                            replaysToProcess_paths.append(os.path.join(r"C:\Users\swisscom\Videos", file))
                            replaysToProcess_names.append(file)
                    if len(replaysToProcess_paths) == 0: # If no file is found with current date, search for files from yesterday
                        for file in os.listdir(r"C:\Users\swisscom\Videos"):
                            if file.startswith(fileName2): # If file is found, add it to both lists
                                replaysToProcess_paths.append(os.path.join(r"C:\Users\swisscom\Videos", file))
                                replaysToProcess_names.append(file)
                    print("Done")

                    print(f"Found {len(replaysToProcess_names)} replay(s) to process")
                    for id, file in enumerate(replaysToProcess_names): # move files and change names
                        # setup file names and paths
                        oldFileNameDate = datetime.strptime(file, '%Y-%m-%d %H-%M-%S.mp4')
                        newFileNameDate = oldFileNameDate.strftime("Squadron 42 - Star Citizen %Y.%m.%d - %H.%M.%S.00.OBS.REC.mp4")
                        oldFilePath = replaysToProcess_paths[id]
                        newFilePath = os.path.join( "D:", "Vidéos", "Squadron 42 - Star Citizen", newFileNameDate)
                        # run copy command
                        subprocess.run(["move", os.path.join(oldFilePath), f"{newFilePath}"], shell=True)

async def replay(action):
    # Connecting to OBS
    print("Connecting to OBS...", end=" ", flush=True)
    async with websockets.connect("ws://localhost:4444") as websocket:
        await websocket.send(json.dumps({"request-type":"GetReplayBufferStatus","message-id":"1"}))
        status_response = json.loads(await websocket.recv())
        if status_response["status"] != "ok": # if an error occurs, print the error
            print("Error: " + status_response["message-id"] + ", " + status_response["error"])
            sys.exit(1)
        else:
            print("Connected")

        match action:
            case "status":
                # Returning replay status
                if status_response["isReplayBufferActive"]:
                    print("Replay buffer active")
                else:
                    print("Replay buffer inactive")

            case "start":
                # starting OBS replay
                print("Sending request...", end=" ", flush=True)
                await websocket.send(json.dumps({"request-type":"StartReplayBuffer","message-id":"2"}))
                response = json.loads(await websocket.recv())
                if response["status"] != "ok": # if an error occurs, print the error
                    print("Error: " + response["message-id"] + ", " + response["error"])
                    sys.exit(1)
                elif response["status"] == "ok": # if not, print success
                    print("Replay buffer enabled")

            case "stop":
                # Stop OBS replay
                print("Sending request...", end=" ", flush=True)
                await websocket.send(json.dumps({"request-type":"StopReplayBuffer","message-id":"2"}))
                response = json.loads(await websocket.recv())
                if response["status"] != "ok": # if an error occurs, print the error
                    print("Error: " + response["message-id"] + ", " + response["error"])
                    sys.exit(1)
                elif response["status"] == "ok": # if not, print success
                    print("Replay buffer disabled")

            case "save":
                # Save OBS replay
                print("Sending save request...", end=" ", flush=True)
                await websocket.send(json.dumps({"request-type":"SaveReplayBuffer","message-id":"2"}))
                response = json.loads(await websocket.recv())
                if response["status"] != "ok": # if an error occurs, print the error
                    print("Error: " + response["message-id"] + ", " + response["error"])
                    sys.exit(1)
                time.sleep(2)
                print("Saved")

                # Setup file names
                print("Processing files...", end=" ", flush=True)
                today = datetime.now()
                yesterday = today + timedelta(days=-1)
                fileName = f"Replay {today.strftime('%Y-%m-%d')}"
                fileName2 = f"Replay {yesterday.strftime('%Y-%m-%d')}"
                replaysToProcess_paths = [] # list for file names with full paths
                replaysToProcess_names = [] # list for file names only
                
                for file in os.listdir(r"C:\Users\swisscom\Videos"): # Search for the file
                    if file.startswith(fileName): # If file is found, add it to both lists
                        replaysToProcess_paths.append(os.path.join(r"C:\Users\swisscom\Videos", file))
                        replaysToProcess_names.append(file)
                if len(replaysToProcess_paths) == 0: # If no file is found with current date, search for files from yesterday
                    for file in os.listdir(r"C:\Users\swisscom\Videos"):
                        if file.startswith(fileName2): # If file is found, add it to both lists
                            replaysToProcess_paths.append(os.path.join(r"C:\Users\swisscom\Videos", file))
                            replaysToProcess_names.append(file)
                print("Done")

                print(f"Found {len(replaysToProcess_names)} replay(s) to process")
                for id, file in enumerate(replaysToProcess_names): # move files and change names
                    # setup file names and paths
                    oldFileNameDate = datetime.strptime(file, 'Replay %Y-%m-%d %H-%M-%S.mp4')
                    newFileNameDate = oldFileNameDate.strftime("Squadron 42 - Star Citizen %Y.%m.%d - %H.%M.%S.00.OBS.DVR.mp4")
                    oldFilePath = replaysToProcess_paths[id]
                    newFilePath = os.path.join( "D:", "Vidéos", "Squadron 42 - Star Citizen", newFileNameDate)
                    # run copy command
                    subprocess.run(["move", os.path.join(oldFilePath), f"{newFilePath}"], shell=True)


async def chngScene(scene):
    print(f"Changing to scene {scene}...", end=" ", flush=True)
    async with websockets.connect("ws://localhost:4444") as websocket:
        await websocket.send(json.dumps({"request-type":"SetCurrentScene","scene-name":f"{scene}","message-id":"1"}))
        response = json.loads(await websocket.recv())
        print("Done")
        return response

async def chngSceneProfile(profile):
    print(f"Changing to scene profile {profile}...", end=" ", flush=True)
    async with websockets.connect("ws://localhost:4444") as websocket:
        await websocket.send(json.dumps({"request-type":"SetCurrentSceneCollection","sc-name":f"{profile}","message-id":"1"}))
        response = json.loads(await websocket.recv())
        print("Done")
        return response

def startobs():
    cwd = os.getcwd()
    os.chdir("C:\\Program Files\\obs-studio\\bin\\64bit\\")
    subprocess.Popen(["C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe", "--startreplaybuffer", "--collection 'Replay'", "--minimize-to-tray"])
    os.chdir(cwd)

