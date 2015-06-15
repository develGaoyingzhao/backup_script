#!/usr/bin/env python
# filename - backup_ver4.py

import os
import time

source = ['/home/yzgao/web', '/home/yzgao/code', '/home/yzgao/work_log', '/home/yzgao/Documents']

target_dir = '/home/yzgao/backup/'

today = target_dir + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

if not os.path.exists(today):
	os.mkdir(today)
	print 'Successfully creat directory', today

comment = raw_input('Enter the change:')
if len(comment) == 0:
	target = today + os.sep + now + '.tar.gz'
else:
	target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.tar.gz'

tar_command = "tar -czf '%s' %s" % (target, ' '.join(source))

if os.system(tar_command) == 0:
	print 'successful backup.'
else:
	print 'backup FAILED.'
