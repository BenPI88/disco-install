import os
def splash():
  os.system("clear")
  print(" ______   ___   _______  _______  _______  ______    ______     ___   __    _  _______  _______  _______  ___      ___      _______  ______   \n|      | |   | |       ||       ||       ||    _ |  |      |   |   | |  |  | ||       ||       ||   _   ||   |    |   |    |       ||    _ |  \n|  _    ||   | |  _____||       ||   _   ||   | ||  |  _    |  |   | |   |_| ||  _____||_     _||  |_|  ||   |    |   |    |    ___||   | ||  \n| | |   ||   | | |_____ |       ||  | |  ||   |_||_ | | |   |  |   | |       || |_____   |   |  |       ||   |    |   |    |   |___ |   |_||_ \n| |_|   ||   | |_____  ||      _||  |_|  ||    __  || |_|   |  |   | |  _    ||_____  |  |   |  |       ||   |___ |   |___ |    ___||    __  |\n|       ||   |  _____| ||     |_ |       ||   |  | ||       |  |   | | | |   | _____| |  |   |  |   _   ||       ||       ||   |___ |   |  | |\n|______| |___| |_______||_______||_______||___|  |_||______|   |___| |_|  |__||_______|  |___|  |__| |__||_______||_______||_______||___|  |_|")
splash()
print("Installing...")
os.system("sudo dpkg -i discord-0.0.25.deb")
print("Discord Has Been Installed. Would You Like To Install BetterDiscord? (y/n)")
option = input("")
bd = False
if option == "y":
  splash()
  print("!WARNING!\nBetterDiscord is technically against Discord's ToS according to the following phrase taken from the Discord ToS.\n\nYou may not copy, modify, create derivative works based upon, distribute, sell, lease, or sublicense any of our software or services. You also may not reverse engineer or decompile our software or services, attempt to do so, or assist anyone in doing so, unless you have our written consent or applicable law permits it.\n\nContinue? (y/n)")
  option = input("")
  if option == "y":
    splash()
    os.system("chmod -x BetterDiscord-Linux.AppImage")
    os.system("./BetterDiscord-Linux.AppImage")
    splash()
    print("Done!")
    bd = True
if bd == False:
  splash()
  print("If you ever want to install BetterDiscord, a file has been dropped that will install BetterDiscord. You can run this file with the command\n\n        bash ~/.bd.sh")
  os.system("echo chmod -x .BetterDiscord-Linux.AppImage && ./BetterDiscord-Linux.AppImage > .bd.sh")
  os.system("cp .BetterDiscord-Linux.AppImage ~/.BetterDiscord-Linux.AppImage")
