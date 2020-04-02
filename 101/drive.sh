#!/usr/bin/env bash

# alias df='/mnt/crit/trees/engineerman/101/drive.sh'

cat << EOF
Filesystem      Size  Used Avail Use% Mounted on
udev             24G     0   24G   0% /dev
tmpfs           4.8G   22M  4.7G   1% /run
/dev/sda1        79G   55G   20G  74% /
tmpfs            24G  1.1G   23G   5% /dev/shm
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs            24G     0   24G   0% /sys/fs/cgroup
/dev/sdb1       253G   73G  167G  31% /home
/dev/sdd1       931G  440G  491G  48% /mnt/extra
tmpfs           4.8G   36K  4.8G   1% /run/user/1000
/proc/mxtp      4.0T     0  4.0T   0% /mnt/cpumxtp
EOF
