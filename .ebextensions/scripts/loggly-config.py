import os

rsyslog_path = '/etc/rsyslog.conf'
loggly_file_path = '/etc/rsyslog.d/22-loggly.conf'

print('loggly-conf.py starts ...')

class LogglyConfig:

    def __init__(self):
        self.__linux_log()
        self.__config_loggly_for_log4j()

    def __linux_log(self):
        #not installed on this machine
        if not os.path.exists(loggly_file_path):
            os.system('rm -f configure-linux.sh')
            os.system('wget https://www.loggly.com/install/configure-linux.sh')
            os.system('sudo bash configure-linux.sh -a sle95159 -u sle95159 -p Borussia123 -s')


    def __config_loggly_for_log4j(self):
        f = open(rsyslog_path,'r')
        file_text = f.read()
        f.close()
        file_text = file_text.replace('#module(load="imudp")', 'module(load="imudp")')
        file_text = file_text.replace('#input(type="imudp" port="514")', 'input(type="imudp" port="514")')
        f = open(rsyslog_path,'w')
        f.write(file_text)
        f.close()

        os.system('service rsyslog restart')

LogglyConfig()

print('loggly-conf.py ended ...')
