#!/usr/bin/env ruby
# This script accepts one argument and pass it to
# a regular epression matching method
puts ARGV[0].scan(/hbtn/).join
puts ARGV[0].scan(/hbn/).join
