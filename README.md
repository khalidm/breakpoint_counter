# breakpoint counter
A tool counts soft-clip reads per position across a region of interest by parsing the CIGAR string for each aligned read. The Python script uses the pysam library to iterate through a BAM file, counts soft-clipped bases denoted by the S operation, filter by alignment abd base quality thresholds, and identify exactly where a read "breaks" into a soft clip.

The tools is written in Python and utilizes the [pysam] (https://pysam.readthedocs.io/en/latest/api.html) library.

# Authors

 * Khalid Mahmood
