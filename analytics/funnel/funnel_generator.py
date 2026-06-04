import json

with open(
    "data/output/kpis.json",
    "r"
) as f:
    kpis = json.load(f)

entry = kpis["footfall"]

zone_visit = int(entry * 0.85)

with open(
    "data/output/billing.json",
    "r"
) as f:
    billing = json.load(f)["billing"]

purchase = int(billing * 0.80)

funnel = {
    "entry": entry,
    "zone_visit": zone_visit,
    "billing": billing,
    "purchase": purchase
}

with open(
    "data/output/funnel.json",
    "w"
) as f:
    json.dump(
        funnel,
        f,
        indent=4
    )

print("funnel.json saved")
print(funnel)