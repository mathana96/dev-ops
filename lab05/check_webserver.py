import subprocess

def main():

  process = subprocess.run('ps -A | grep nginx | grep -v grep', shell=True, stdout=subprocess.PIPE)
  retcode = process.returncode
  if retcode > 0:
    print('nginx not running')
  else:
    print('nginx running')

if __name__ == '__main__':
  main()
