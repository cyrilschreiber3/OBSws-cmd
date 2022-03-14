# obsws-cmd

The goal of this script is to be able to do basic action via command line in [OBS Studio](https://obsproject.com/).
With simple commands, you will be able to control stream, recording and replay start and stop as well as scene switching. With time, I will probably beef if up, but for now, I will keep it to this.
Obviously, I won't just do a basic ten liner program that just does what I ask it to, as it wouldn't be fun otherwise. I want to make it a bit overkill for its use. By that, I mean that I plan on adding error checks and handling, conditions, logging and more to make it the more stable and user-friendly possible.

## 14/03/2022 - Testing done

I tested argument support and the websocket communications with obs separately, and now I can start writing the actual program.