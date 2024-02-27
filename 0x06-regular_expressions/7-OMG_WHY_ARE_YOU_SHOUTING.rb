#!/usr/bin/env ruby
# This regular expression only matches capital letters
puts ARGV[0].scan(/[A-Z]/).join
