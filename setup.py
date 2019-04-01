#!/usr/bin/env python2

          
import setuptools 

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="VARtools",
    version="2.0.12",
    author="Arnaud Felten, Nicolas Radomski, Ludovic Mallet (pack)",
    author_email="arnaud.felten@anses.fr, nicolas.radomski@anses.fr, ludovic.mallet@anses.fr",
    description="VARtools: scripts for SNPs and INDELs analysis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/afelten-Anses/VARtools",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 2.7",
        "Operating System :: POSIX :: Linux",
    ],
        scripts=['iVARCall2/src/iReportMaker2',
             "iVARCall2/src/iVARCall2",
             "iVARCall2/src/iVCFmaker",
             "iVARCall2/src/iVCFmerge",
             "FixedVarTools/src/FixedVar",
             "FixedVarTools/src/XMLparser",
             "FixedVarTools/src/XMLtoTSV",
             "FixedVarTools/src/phyloFixedVar",
             "GOtools/src/EveryGO",
             "GOtools/src/GOslimmer_xml",
             "GOtools/src/GoXML",
             "iVARCall/src/iReportMaker",
             "iVARCall/src/iVARCall",
             "iVARCall/src/iVCFmaker_SNP",
             "iVARCall/src/iVCFmerge_SNP",
             "VARCall/src/BAMmaker",
             "VARCall/src/SNP-INDEL_merge",
             "VARCall/src/VARCall",
             "VARCall/src/VCFilter",
             "VARCall/src/VCFmaker_INDEL",
             "VARCall/src/VCFmaker_SNP",
             "VARCall/src/VCFtoFASTA",
             "VARCall/src/VCFtoMATRIX",
             "VARCall/src/VCFtoPseudoGenome",
             "VARCall/src/reportMaker",
             "iVARCall2/dep/GenomeAnalysisTK.jar",
             ],
    include_package_data=True,
    install_requires=['biopython>=1.68', 
                      'lxml',
                      'requests',
                      ],
    zip_safe=False,







)
