# cs-review

Basic DS and Algorithm implementations

## Latency

- L1: 1ns
- L2: 4ns (4x slower)
- L3: 11ns (11x slower)
- Mutex lock/unlock: 25ns (25x)
- DDR4 RAM: 100ns (100x slower)
- NVMe SSD: 120,000ns or 120k ns (120,000x slower)
- SATA/SAS SSD: 400,000ns or 400k ns (400,000x slower)
- Rotational HDD: 2–6ms (2,000,000x slower)

- Read 1 MB sequentially from memory: 250,000ns or 250 us
- Read 1 MB sequentially from SSD: 1,000,000ns or 1,000us or 1 ms ~1GB/sec SSD, 4X memory

*Note: Approx rounded number*

## Latency Units

- 1 ns(nano) = 10^-9 seconds
- 1 us(micro) = 10^-6 seconds = 1,000 ns
- 1 ms(milli) = 10^-3 seconds = 1,000 us = 1,000,000 ns

**Source:**
- https://nickcraver.com/blog/2019/08/06/stack-overflow-how-we-do-app-caching/
- https://github.com/donnemartin/system-design-primer#latency-numbers-every-programmer-should-know
