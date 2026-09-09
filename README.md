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
- **Variant 1A (Nonsense / Truncating Allele)**: `chr15:40209701 T>G` (`rs759242053`) – Heterozygous stop_gained variant (`c.2210T>G`, `p.Leu737*`, GT: `0/1`, ClinVar Pathogenic/Likely Pathogenic, gnomAD AF=9.98e-05, GQ=99)
- **Variant 1B (Novel Missense Allele)**: `chr15:40220612 T>G` – Heterozygous novel missense variant (`c.3006T>G`, `p.Asn1002Lys`, GT: `0/1`, SIFT=Deleterious, PolyPhen-2=Probably Damaging, Novel, GQ=99)
- **Mechanism**: MVA1 is an autosomal recessive chromosome segregation disorder causing premature chromatid separation (PCS), mosaic variegated aneuploidy, severe prenatal/postnatal growth retardation, and high predisposition to early-childhood embryonal malignancies, particularly **rhabdomyosarcoma** and Wilms tumor. Complete homozygous null alleles are lethal; patients carry a truncating null allele in trans with a hypomorphic missense allele. Parental miscarriages reflect constitutional/germline chromosome missegregation.

#### 2. Secondary Finding: Factor V Leiden Thrombophilia Risk (*F5*, OMIM #188055)
- **Genotype**: Heterozygous
- **Variant 2**: `chr1:169549811 C>T` (`rs6025`) – Heterozygous missense variant (`c.1601G>A`, `p.Arg506Gln`, GT: `0/1`, DP=54, GQ=99)
- **Clinical Relevance**: Established genetic risk factor for venous thromboembolism, clinically relevant for pediatric oncological care and catheter management.

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
