import pysam
import argparse
from collections import Counter

def count_softclips(bam_path, bed_path, min_mq, min_bq):
    samfile = pysam.AlignmentFile(bam_path, "rb")
    bedfile = open(bed_path, "r")

    print("chromosome\tposition\tbreakpoint_count")

    for line in bedfile:
        if line.startswith("#") or not line.strip():
            continue
        
        chrom, start, end = line.split()[:3]
        start, end = int(start), int(end)
        
        # Dictionary to store counts for the current interval
        # Key: genomic position, Value: count
        pos_counts = Counter()

        # Fetch reads overlapping the interval
        for read in samfile.fetch(chrom, start, end):
            # 1. Quality Filters
            if read.mapping_quality < min_mq or read.is_unmapped:
                continue

            # 2. Check CIGAR for Soft Clipping
            # cigarstats returns a list of tuples: (operation, length) where 4 is the code for ('S': Soft clipping)
            cigar = read.cigartuples
            if not cigar:
                continue

            # Left Clip
            if cigar[0][0] == 4:
                clip_pos = read.reference_start # Genomic coord of the first aligned base
                if start <= clip_pos <= end:
                    # Check base quality of the clipped base
                    # read.query_qualities is 0-indexed relative to the read
                    if read.query_qualities[cigar[0][1] - 1] >= min_bq:
                        pos_counts[clip_pos] += 1

            # Right Clip
            if cigar[-1][0] == 4:
                clip_pos = read.reference_end # Genomic coord of the last aligned base
                if start <= clip_pos <= end:
                    if read.query_qualities[-cigar[-1][1]] >= min_bq:
                        pos_counts[clip_pos] += 1

        # Print results for this interval
        for pos in sorted(pos_counts.keys()):
            print(f"{chrom}\t{pos}\t{pos_counts[pos]}")

        # TODO: plot

    samfile.close()
    bedfile.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count breakpoints based on soft-clipped reads per position.")
    parser.add_argument("-b", "--bam", required=True, help="Input BAM file")
    parser.add_argument("-i", "--bed", required=True, help="Input BED file (intervals)")
    parser.add_argument("-m", "--min_mq", type=int, default=20, help="Min Mapping Quality (default: 20)")
    parser.add_argument("-q", "--min_bq", type=int, default=13, help="Min Base Quality at clip point (default: 13)")
    
    args = parser.parse_args()
    count_softclips(args.bam, args.bed, args.min_mq, args.min_bq)
