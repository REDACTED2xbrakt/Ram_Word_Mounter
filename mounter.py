#!/usr/bin/python3
import subprocess, argparse

def main():
      parser = argparse.ArgumentParser()
      parser.add_argument("-ram", type=str, dest="ram", help="checks ram", default=None)
      parser.add_argument("-mount", type=str, dest="mount", help="mounts ramdisk", default=None)
      parser.add_argument("-word", type=str, dest="word", help="copies wordlist to ram", default=None)

      args = parser.parse_args()

      ram = args.ram
      mount = args.mount

      if ram:
          ram_check(ram)
      elif mount:
          mounter(mount)
      elif wordlist:
          wordlist(word)
      else:
          print("[-] Invalid option try -h for help")
    
def ram_check(ram):
    print("[+] Displaying ram...")
    subprocess.run(["free", "-g"])

def mounter(mount):
    mount_size = input("[*] Enter how much space you would like in gigabytes: ")
    print("[+] Making directory in /mnt/ramdisk")
    subprocess.run(["mkdir", "/mnt/ramdisk"])
    print("[+] Mounting " + mount_size + "gb ramdisk to /mnt/ramdisk")
    subprocess.run(["mount", "-t", "tmpfs", "-o", "size=" + mount_size + "g", "tmpfs", "/mnt/ramdisk",])
    print("[+] Done!")
def wordlist(word):
    wordlist = input("[*] Enter the directory of the wordlist you would like to put in the ram: ")
    subprocess.run(["cp", wordlist, "/mnt/ramdisk/"])
    print("[+] Done!")


main()

