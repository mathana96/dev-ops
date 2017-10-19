import subprocess

def main():
  process = subprocess.run('ps -A | grep mysqld', shell=True)
  retcode = process.returncode

  if retcode > 0:
      print('MySQL server not running')
  else:
      print('MySQL server running')





if __name__ == __main__:
    main()
