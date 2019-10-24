#!/usr/bin/python3
import subprocess, argparse, psutil #modules needed

# -ram argument

def main():
      parser = argparse.ArgumentParser()
      parser.add_argument("-r", type=str, dest="ram", help="checks ram", default=None)
      parser.add_argument("-m", type=str, dest="mount", help="mounts space", default=None)

      args = parser.parse_args()

      ram = ""
      mount = ""
      ram = args.ram
      mount = args.mount

      if ram:
          ram_check(ram)
      elif mount:
          mounter(mount)
      else:
          print("[-] Invaled options")
    
#Report on ram stats
def ram_check(ram):
    print("[+] Displaying ram...")
    subprocess.run(["free", "-g"])

def mounter(mount):
    mount_size = input("[*] Enter how much space you would like in gigabytes: ")
    print("[+] Making directory in /mnt/ramdisk")
    subprocess.run(["mkdir", "/mnt/ramdisk"])
    print("[+] Mounting " + mount_size + " to /mnt/ramdisk")
    subprocess.run(["mount", "-t", "tmpfs", "-o", "size=", "tmpfs", "/mnt/ramdisk",])

main()
