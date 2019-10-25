#!/usr/bin/python3
import subprocess, argparse

def main():
      parser = argparse.ArgumentParser()
      parser.add_argument("-ram", type=str, dest="ram", help="checks ram", default=None)
      parser.add_argument("-mount", type=str, dest="mount", help="mounts space", default=None)

      args = parser.parse_args()

      ram = args.ram
      mount = args.mount

      if ram:
          ram_check(ram)
      elif mount:
          mounter(mount)
      else:
          print("[-] Invalid option try -h for help")
    
def ram_check(ram):
    print("[+] Displaying ram...")
    subprocess.run(["free", "-g"])

def mounter(mount):
    mount_size = input("[*] Enter how much space you would like in gigabytes: ")
    print("[+] Making directory in /mnt/ramdisk")
    subprocess.run(["mkdir", "/mnt/ramdisk"])
    print("[+] Mounting " + mount_size + " to /mnt/ramdisk")
    subprocess.run(["mount", "-t", "tmpfs", "-o", "size=" + mount_size, "tmpfs", "/mnt/ramdisk",])
    print("[+] Done!")
    wordlist = input("[*] Enter wordlist you would like to put in the ram: ")
    subprocess.run(["cp", wordlist])
    print("[+] Done!")


main()

