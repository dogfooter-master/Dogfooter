from cryptography.fernet import Fernet
import pickle
import os, sys
import time
import likeyoubot_license

day = input('License duration days: ')

current_date = time.time()
license_due_date = current_date + int(day)*24*60*60

try:
	likeyoubot_license.LYBLicense().generate_license(license_due_date)
	print('successfully created.')
except:
	print('fail')
# remain_time = LYBLicense().read_license()

# print('REMAIN_TIME: ', int(remain_time/(24*60*60)), '일', int(remain_time/(60*60)), '시간', int(remain_time%60), '분')