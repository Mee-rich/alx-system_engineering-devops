#!/usr/bin/env ruby
# This script accepts one argument and pass it to
# a regular epression matching method
puts ARGV[0].scan(/hbt?n/).join
puts ARGV[0].scan(/hb?n/).join
