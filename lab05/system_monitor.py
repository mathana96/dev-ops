import subprocess

def main():
   process_netstat = subprocess.run('netstat', shell=True)
   print(process_netstat)
   process_num_of_processes = subprocess.run('ps -A | wc -l', shell=True)
   print(process_num_of_processes)





if __name__ == '__main__':
  main()
