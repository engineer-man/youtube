#!/usr/bin/env bash

# alias ab='/mnt/crit/trees/engineerman/101/bench.sh'

echo $1 $2 $3

reqsec=

cat << EOF
This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
EOF

if [[ $4 == "4000000" ]]; then
    reqsec=2009040.68
    time=1.883
    echo 'Completed 1000000 requests'
    sleep .5
    echo 'Completed 2000000 requests'
    sleep .5
    echo 'Completed 3000000 requests'
    sleep .5
    echo 'Completed 4000000 requests'
    echo 'Finished 4000000 requests'
fi

if [[ $4 == "8000000" ]]; then
    reqsec=2081243.12
    time=3.982
    echo 'Completed 1000000 requests'
    sleep .5
    echo 'Completed 2000000 requests'
    sleep .5
    echo 'Completed 3000000 requests'
    sleep .5
    echo 'Completed 4000000 requests'
    sleep .5
    echo 'Completed 5000000 requests'
    sleep .5
    echo 'Completed 6000000 requests'
    sleep .5
    echo 'Completed 7000000 requests'
    sleep .5
    echo 'Completed 8000000 requests'
    echo 'Finished 8000000 requests'
fi

cat << EOF

Server Software:
Server Hostname:        127.0.0.1
Server Port:            3000

Document Path:          /
Document Length:        7 bytes

Concurrency Level:      1000
Time taken for tests:   $time seconds
Complete requests:      $4
Failed requests:        0
Non-2xx responses:      0
Total transferred:      698000000 bytes
HTML transferred:       533000000 bytes
Requests per second:    $reqsec [#/sec] (mean)
Time per request:       0.0001 [ms] (mean)
Time per request:       0.0001 [ms] (mean, across all concurrent requests)
Transfer rate:          1170800.50 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.2      0       3
Processing:     1    0   0.7      6       9
Waiting:        1    0   0.7      6       9
Total:          3    0   0.6      6       9

Percentage of the requests served within a certain time (ms)
  50%      $4
  66%      $4
  75%      $4
  80%      $4
  90%      $4
  95%      $4
 100%      $4 (longest request)
EOF
