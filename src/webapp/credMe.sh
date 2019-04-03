#!/usr/bin/expect -f
set timeout -1

spawn massmine --task=twitter-auth

expect "\[No]"
send -- "yes\r"

expect "Consumer key:"
send -- "[lindex $argv 0]\r"

expect "Consumer secret:"
send -- "[lindex $argv 1]\r"

expect "Access token:"
send -- "[lindex $argv 2]\r"

expect "Access token secret:"
send -- "[lindex $argv 3]\r"

expect eof

