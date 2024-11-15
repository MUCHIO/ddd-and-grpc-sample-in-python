require 'benchmark'
require_relative 'route_guide_client'

test_count = 1_000
threads = []
results = []

Benchmark.bm do |x|
  x.report("Load Test") do
    test_count.times do
      threads << Thread.new do
        main('../../src/infrastructure/database/data/route_guide_db.json')
      end
    end
    threads.each(&:join)
  end
end