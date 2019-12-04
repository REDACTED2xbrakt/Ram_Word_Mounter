#!/usr/bin/python3
import subprocess, argparse

def main():
      parser = argparse.ArgumentParser()
      parser.add_argument("-r", type=str, dest="ram", help="checks ram", default=None, action='store_true')
      parser.add_argument("-m", type=str, dest="mount", help="mounts ramdisk", default=None, action='store_true')
      parser.add_argument("-w", type=str, dest="word", help="copies wordlist to ram", default=None, action='store_true')

      args = parser.parse_args()

      ram = args.ram
      mount = args.mount
      word = args.word

      if ram:
          ram_check(ram)
      elif mount:
          mounter(mount)
      elif word:
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

