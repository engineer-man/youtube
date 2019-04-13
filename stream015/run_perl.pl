#!/usr/bin/env perl

use strict;

print "How many lines? ";
my $num = <STDIN>;
$num > 0 or die "Num must be positive.  You entered $num";

my $accum = "";
my $sep = "";
while(my $line = <STDIN>) {
    chomp $line;
    if($line eq "STOP!") { last; }
    $accum = "$accum$sep$line";
    if(--$num == 0) { last; }
    $sep = " ";
}

print "$accum\n";
