#!/usr/bin/python3
import subprocess, argparse, psutil #modules needed

# -ram argument

def main():
      parser = argparse.ArgumentParser()
      parser.add_argument("-r", type=str, dest="ram", help="checks ram", default=None)
      parser.add_argument("-m", type=str, dest="mount", help="mounts space", default=None)


      args = parser.parse_args()

      ram = ""
      ram = args.ram

      if ram:
          ram_check(ram)
      else:
          print("[-] Invaled options")
 
def ram_check(ram):
    print("[+] Displaying ram...")
    subprocess.run(["free", "-g"])
   #needs changed to Gigs

# -m Mount the ramdisk
def mounter(mount):
    mount_size = input("[*] Enter how much space you would like: ")
    print("[+] Making directory in /mnt/ramdisk")
    subprocess.run(["mkdir", "/mnt/ramdisk"])
main()
