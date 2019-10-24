#!/usr/bin/python3

import subprocess, argparse #modules needed

def main():
      parser = argparse.ArgumentParser()
      parser.add_argument("-r", type=str, dest="ram", help="checks ram", default=None)

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

main()