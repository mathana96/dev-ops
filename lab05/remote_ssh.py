import subprocess

def main():
  general_path = '~/Desktop/applied-computing/year-3/semester-1/dev-ops/'
  path_to_key = 'lab04/lab4-instance.pem'
  instance_ip = 'ec2-user@54.229.112.109'

  command = 'ssh -i ' + general_path + path_to_key + ' ' + instance_ip + ' \'python3 check_webserver.py\''

  # process = subprocess.run(['ssh -i', general_path + path_to_key, instance_ip, 'pwd'], shell=True)
  process = subprocess.run([command], shell=True)

  # print(command)










if __name__ == '__main__':
    main()
