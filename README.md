# Rare Disease Genomic Challenge (MVA Hackathon 2026)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build: GRCh38](https://img.shields.io/badge/Genome_Build-GRCh38-blue.svg)]()
[![Track 1: Completed](https://img.shields.io/badge/Track_1-Completed-success.svg)]()

Whole-genome sequencing (WGS) variant interpretation and candidate drug discovery pipeline for the **SageBio Rare Disease Genomic Challenge (MVA Hackathon 2026)**.

---

## 🧬 Clinical Phenotype & Dual Molecular Diagnosis

### Proband Phenotypic Profile
- **Primary Malignancy**: Rhabdomyosarcoma (`HP:0002859`)
- **Congenital Renal Finding**: Nephrocalcinosis (`HP:0000121`, present since birth)
- **Growth & Perinatal Abnormalities**: Short stature (`HP:0004322`), Failure to thrive (`HP:0001508`), Skeletal muscle atrophy (`HP:0003202`), Premature birth at 32 weeks (`HP:0001622`), SGA (~1 kg birth weight, `HP:0001518`)
- **Parental History**: Recurrent spontaneous miscarriages (`HP:0200067`)

---

### Molecular Findings

#### 1. Primary Finding: Mosaic Variegated Aneuploidy (MVA) Syndrome 1 (*BUB1B*, OMIM #257300)
- **Genotype**: Compound Heterozygous
- **Variant 1A**: `chr15:40259762 G>A` – Novel heterozygous missense variant (`p.Gly412Asp` / `c.1235G>A`, GT: `0/1`, High Quality QD=16.13, GQ=99)
- **Variant 1B**: `chr15:40192892 C>T` (`rs185599777`) – Heterozygous intronic/regulatory variant (`c.1059-3653C>T`, GT: `0/1`, ClinVar ID 1676498)
- **Mechanism**: MVA1 is an autosomal recessive chromosome segregation disorder causing premature chromatid separation, mosaic aneuploidy, severe prenatal/postnatal growth retardation, and high predisposition to embryonal rhabdomyosarcoma. Parental miscarriages reflect inherited/de novo mitotic and meiotic chromosome instability.

#### 2. Secondary Finding: Antenatal Bartter Syndrome Type 1 (*SLC12A1*, OMIM #601678)
- **Genotype**: Homozygous
- **Variant 2**: `chr15:48288516 T>C` (`rs3577326` / ClinVar 3577326) – Homozygous pathogenic splicing variant (`c.2873_2873+1delinsCGTT`, GT: `1/1`, Depth 32 reads, GQ=95)
- **Mechanism**: Loss of renal NKCC2 cotransporter function causes Antenatal Bartter Syndrome Type 1, directly explaining the **congenital nephrocalcinosis** present from birth and severe polyhydramnios/preterm birth at 32 weeks.

---

## 📁 Repository Structure

```
├── README.md                           # Project documentation
├── track1_submission.csv               # Track 1 official submission file
├── methods_description_completed.txt   # Completed Track 1 methods description form
├── download_data.py                    # Script to download essential VCF and clinical docs
├── download_all_fastq.py               # Script to download raw 85 GB FASTQ sequencing dataset
├── check_variants.py                   # dbSNP & ClinVar variant lookup utility
├── templates/                          # Hackathon official templates
└── docs/                               # Hackathon dataset announcements & compliance guidelines
```

---

## 🛡️ IRB & Data Use Compliance

This repository complies strictly with SageBio and MVA Hackathon Data Use Agreements:
- All raw patient sequencing data (`data/*.vcf.gz`, `data/*.fastq.gz`) and environment secrets (`.env`) are explicitly ignored via `.gitignore` and **never committed or re-shared**.
- Generative AI processing was performed strictly under commercial processor terms with zero data retention or training on customer inputs.

---

## ⚖️ License

Distributed under the MIT License. See `LICENSE` for details.
