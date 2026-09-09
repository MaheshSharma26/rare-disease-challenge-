import urllib.request
import json
import ssl

ctx = ssl._create_unverified_context()

rsids = ['rs28570325', 'rs372589327', 'rs28620590', 'rs185599777', 'rs28521889']

print("=== Checking dbSNP for known variants in BUB1B ===")
for rs in rsids:
    clean_id = rs.replace('rs', '')
    url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=snp&id={clean_id}&retmode=json'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Python'})
        res = json.loads(urllib.request.urlopen(req, context=ctx, timeout=10).read())
        doc = res['result'].get(clean_id, {})
        print(f"\n{rs}:")
        print("  Title:", doc.get('title'))
        print("  Class:", doc.get('fxn_class'))
        print("  Global MAF:", doc.get('global_maf'))
        print("  ClinVar Significance:", doc.get('clinical_significance'))
    except Exception as e:
        print(f"Error checking {rs}: {e}")

# Check ClinVar for BUB1B variants directly
print("\n=== Checking ClinVar for BUB1B pathogenic variants ===")
cv_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=clinvar&term=BUB1B[gene]+AND+pathogenic[clinsig]&retmode=json&retmax=20"
try:
    req = urllib.request.Request(cv_url, headers={'User-Agent': 'Python'})
    cv_res = json.loads(urllib.request.urlopen(req, context=ctx, timeout=10).read())
    idlist = cv_res.get('esearchresult', {}).get('idlist', [])
    print(f"Found {len(idlist)} ClinVar pathogenic variant IDs in BUB1B: {idlist[:10]}")
    if idlist:
        sum_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=clinvar&id={','.join(idlist[:10])}&retmode=json"
        req2 = urllib.request.Request(sum_url, headers={'User-Agent': 'Python'})
        sum_res = json.loads(urllib.request.urlopen(req2, context=ctx, timeout=10).read())
        for vid in idlist[:10]:
            vdata = sum_res.get('result', {}).get(vid, {})
            print(f"ClinVar {vid}: {vdata.get('title')} | Sig: {vdata.get('clinical_significance', {}).get('description')}")
            for loc in vdata.get('variation_set', [{}])[0].get('variation_loc', []):
                if loc.get('assembly_name') == 'GRCh38':
                    print(f"    GRCh38: chr{loc.get('chr')}:{loc.get('start')} {loc.get('ref_allele')}->{loc.get('alt_allele')}")
except Exception as e:
    print(f"Error querying ClinVar: {e}")
