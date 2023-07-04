#!/usr/bin/env ruby
# The regular expression should exactly match a string starting with "h", ending with "n", and allowing any single character in between.
puts ARGV[0].scan(/h.n/).join
