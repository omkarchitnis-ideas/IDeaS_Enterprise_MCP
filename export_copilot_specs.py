import os
import json
import requests

out_dir = r"C:\Users\omchit\OneDrive - SAS\Documents\Python Scripts\IDeaS_Enterprise_MCP\copilot_specs"
os.makedirs(out_dir, exist_ok=True)

base_url = "http://localhost:8550"

domains = ["composite", "sfdc", "optix", "cma", "confluence", "datadog", "ups", "all"]

for domain in domains:
    if domain == "all":
        url = f"{base_url}/openapi.json"
        fname = "openapi_all.json"
    else:
        url = f"{base_url}/api/v1/openapi/{domain}.json"
        fname = f"openapi_{domain}.json"
    
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            spec = r.json()
            # Set server URL in the spec to host machine IP
            spec["servers"] = [{"url": "http://172.27.210.162:8550", "description": "SAS IDeaS Master Enterprise Gateway"}]
            file_path = os.path.join(out_dir, fname)
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(spec, f, indent=2)
            path_count = len(spec.get("paths", {}))
            print(f"Exported {fname} ({path_count} paths)")
        else:
            print(f"Failed {fname}: HTTP {r.status_code}")
    except Exception as e:
        print(f"Error {fname}: {e}")
