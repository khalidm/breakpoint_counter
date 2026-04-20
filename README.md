# breakpoint counter
A tool to count soft-clip reads per position across a region of interest by parsing the CIGAR string for each aligned read. The Python script uses the pysam library to iterate through a BAM file, count soft-clipped bases denoted by the S operation, filter by alignment and base quality thresholds, and identify exactly where a read "breaks" into a soft clip.

The tools is written in Python and utilizes the [pysam](https://pysam.readthedocs.io/en/latest/api.html) library.

# Documentation

TODO installation and usage.

# Examples

### Simple usage

```bash
python breakpoint_counter.py -b <input.bam> -i <region.bed> > breakpoint_counts.txt
```


# Authors

 * Khalid Mahmood
