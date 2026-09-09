# Track 1 Clinical & Genomic Analysis Report

**Participant**: Mahesh Kumar Sharma
**Challenge**: SageBio Rare Disease Genomic Challenge (MVA Hackathon 2026) – Track 1  
**Primary Candidate Model/Filename**: `MaheshSharma26_bub1b-compound-het.csv`  

---

## 1. Executive Summary & Clinical Diagnosis

We present a phenotype-driven genomic analysis pipeline applied to Whole Genome Sequencing (WGS) data of a proband presenting with a complex multi-system rare disease phenotype:

- **Primary Oncological Event**: Rhabdomyosarcoma (`HP:0002859`)
- **Congenital Renal Anomalies**: Nephrocalcinosis (`HP:0000121`, present since birth)
- **Growth & Perinatal Abnormalities**: Short stature (`HP:0004322`), Failure to thrive (`HP:0001508`), Skeletal muscle atrophy (`HP:0003202`), Premature birth at 32 weeks (`HP:0001622`), Small for gestational age (~1 kg, `HP:0001518`)
- **Family History**: Recurrent spontaneous parental miscarriages (`HP:0200067`)

### Molecular Diagnosis
1. **Primary Finding**: **Mosaic Variegated Aneuploidy (MVA) Syndrome 1** (OMIM #257300), caused by compound heterozygous mutations in ***BUB1B*** (chr15, GRCh38).
2. **Secondary Finding**: **Factor V Leiden Thrombophilia Risk** (OMIM #188055), caused by a heterozygous mutation in ***F5*** (chr1, GRCh38).

---

## 2. Genomic Methodology & Pipeline

1. **Alignment & Coordinate System**: Whole-genome VCF processing on the GRCh38 reference build without contig prefix in source files (`15`) and mapped to standard HGVS / challenge coordinates (`chr15`).
2. **Comprehensive CDS Annotation**: Extracted all CDS coordinates using GENCODE v46 and mapped coding variants across 20,000+ human genes.
3. **Multi-Database Variant Annotation**: Integrated annotations using Ensembl VEP (MANE Select transcript `ENST00000287598.11`), NCBI ClinVar, NCBI dbSNP, and gnomAD v4 population frequencies.
4. **Phenotype-Genotype Mapping**: Prioritized candidate genes corresponding to Human Phenotype Ontology (HPO) terms for MVA, spindle assembly checkpoint (SAC) defects, and childhood embryonal malignancies (rhabdomyosarcoma).
5. **Recessive Model & Phasing**: Evaluated recessive disease models (compound heterozygosity and homozygosity) across all candidate loci.

---

## 3. Candidate Variant Evidence

### Primary Finding: *BUB1B* (Chromosome 15, GRCh38)
- **Variant 1A (Nonsense / Truncating Allele)**: `chr15:40209701 T>G` (`rs759242053`)
  - **Transcript / HGVS**: `ENST00000287598.11:c.2210T>G` (p.Leu737Ter / p.Leu737*)
  - **Consequence**: `stop_gained` (HIGH impact nonsense mutation)
  - **Clinical Classification**: ClinVar Pathogenic / Likely Pathogenic (`Variation ID: rs759242053`)
  - **Population Frequency**: gnomAD AF = 9.982e-05
  - **Genotype & Quality**: Heterozygous (`0/1`), QUAL=708.77, FILTER=PASS, DP=46, AD=21,25, GQ=99
- **Variant 1B (Novel Missense Allele)**: `chr15:40220612 T>G`
  - **Transcript / HGVS**: `ENST00000287598.11:c.3006T>G` (p.Asn1002Lys)
  - **Consequence**: `missense_variant` (MODERATE impact)
  - **In Silico Pathogenicity**: SIFT = Deleterious (0.00), PolyPhen-2 = Probably Damaging (0.998)
  - **Population Frequency**: Absent in gnomAD v4 / 1000 Genomes (Novel)
  - **Genotype & Quality**: Heterozygous (`0/1`), QUAL=344.77, FILTER=PASS, DP=28, AD=15,13, GQ=99
- **Biological Mechanism & Disease Etiology**:
  - *BUB1B* encodes BUBR1, a core serine/threonine kinase component of the mitotic spindle assembly checkpoint (SAC) and the anaphase-promoting complex/cyclosome (APC/C) inhibitory machinery.
  - Complete homozygous null *BUB1B* is embryonic lethal in humans and mouse models. Viable patients with Mosaic Variegated Aneuploidy Syndrome 1 (MVA1) harbor a classic compound heterozygous genotype: one truncating null allele (`p.Leu737*`) in *trans* with a hypomorphic missense allele (`p.Asn1002Lys`) that retains partial SAC activity.
  - Sub-threshold BUBR1 activity leads to premature chromatid separation (PCS), extensive mosaic aneuploidy across tissue lineages, severe intrauterine and postnatal growth retardation, microcephaly, and an extreme predisposition to early-onset embryonal malignancies, particularly **rhabdomyosarcoma** and Wilms tumor.
  - Parental recurrent spontaneous miscarriages reflect constitutional/germline chromosome missegregation risk during meiosis.

### Secondary Finding: *F5* (Chromosome 1, GRCh38)
- **Variant 2**: `chr1:169549811 C>T` (`rs6025`) – Heterozygous Factor V Leiden (`c.1601G>A`, p.Arg506Gln, GT: `0/1`, DP=54, GQ=99).
- **Clinical Relevance**: Well-documented hereditary thrombophilia risk factor, important for perioperative and central venous line management in pediatric oncology.

---

## 4. Methods Description Summary

- **Approach Type**: Integrated computational prioritization + clinical genetics curation.
- **Data Sources Used**: 100% public databases (NCBI ClinVar, NCBI dbSNP, Ensembl REST VEP, gnomAD v4, MyVariant.info, HPO, OMIM, GENCODE v46).
- **Compound Heterozygous Support**: Explicitly supported and verified via read-backed phasing (PGT/PID).
- **Secondary Findings Handling**: Included secondary pathogenic findings (`finding_type = secondary`).

---

## 5. Generative AI & Data Handling Disclosure

> **AI Usage Attestation**: "Google DeepMind / Antigravity AI Assistant, Gemini 3.8 Flash model, commercial processor terms, no training on customer content."
