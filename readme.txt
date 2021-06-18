For convenience, programs are separated into directories.  Below is a description of the pipeline.  

Bowtie2 (to) SamToBowtieOutput (to) RescueAndDyadCalling/UnknownEndsDyadCallin (to) Nucleotide Frequency
                               (alternatively to) SamNucStart (to) ReadLocator
                                                              (alternatively to) bamCoverage (to) DeepToolsBedgraphMassager (to) CoverageRetriever
FilterCutsites (to) CutsiteReformatter

