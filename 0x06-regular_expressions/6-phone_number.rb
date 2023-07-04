#!/usr/bin/env ruby
# Expression that matches 10 digits
puts ARGV[0].scan(/^[0-9]{10}$/).join
