#!/usr/bin/env php
<?php

$start_num = $argv[1];
$count = $argv[2];

$list = [];

for ($i = 0; $i < $count; ++$i) {
    array_push($list, $i * $start_num);
}

$sum = 0;
$divisible = 0;

foreach ($list as $num) {
    $sum += $num;
    if ($num % 10 == 0) ++$divisible;
}

echo $sum . ' ' . $divisible;
