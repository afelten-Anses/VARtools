#!/usr/bin/env python2.7

          
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="iVarCall2",
    version="2",
    author="Arnaud Felten, Nicolas Radomski",
    author_email="arnaud.felten@anses.fr, nicolas.radomski@anses.fr",
    description="his workflow called iVARCall2 for \"independant variant calling 2\" aims to perform the variant calling analysis from Illumina paired-end reads based on the GATK HaplotypeCaller algorithm. Each sample are processed independently and a g.vcf file is produce for each of them. This allows combination of several iVARCall2 results if the same reference genome is used.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/afelten-Anses/VARtools/tree/master/iVARCall2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: GPLv2",
        "Operating System :: Unix/Linux",
    ],
        scripts=['iVARCall2/src/iReportMaker2',
             "iVARCall2/src/iVARCall2",
             "iVARCall2/src/iVCFmaker",
             "iVARCall2/src/iVCFmerge",
             "iVARCall2/dep/GenomeAnalysisTK.jar",
             ],
    include_package_data=True,
    install_requires=['biopython>=1.68', 
                      'lxml',
                      'requests',
                      ],
    zip_safe=False,







)
