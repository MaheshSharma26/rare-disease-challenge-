import os
import sys
from huggingface_hub import snapshot_download

def get_token() -> str:
    token = os.environ.get("HF_TOKEN")
    if token and token.strip():
        return token.strip()

    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    if os.path.exists(env_path):
        try:
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("HF_TOKEN="):
                        val = line.split("=", 1)[1].strip().strip('"').strip("'")
                        if val:
                            return val
        except Exception:
            pass

    return input("Enter your Hugging Face token: ").strip().strip('"').strip("'")

token = get_token()

print("\nDownloading ESSENTIAL files only (Clinical doc + VCF variant calls ~290 MB)...")
print("Skipping raw 80+ GB FASTQ sequencing reads.\n")

# Download only clinical phenotypes and VCF files (ignore massive FASTQ files)
dataset_dir = snapshot_download(
    repo_id="SageBio/mva-hackathon-2026-data",
    repo_type="dataset",
    local_dir="./data",
    allow_patterns=[
        "*.docx",
        "*.pdf",
        "*.json",
        "*.txt",
        "*.vcf.gz",
        "*.vcf.gz.tbi",
    ],
    token=token,
)

print(f"\n✓ Essential files downloaded successfully to: {dataset_dir}")
