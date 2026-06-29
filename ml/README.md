# Plant-health & recipe learning

Two separate layers — keep them separate, it's what makes the system trustworthy.

## 1. Perception (a CNN) — *what do I see?*
Image of the canopy → `{healthy, yellowing, curling}` + a leaf-area estimate.

- **Cold start:** transfer-learn from a pretrained backbone (e.g. MobileNetV2 on a public plant
  dataset), then fine-tune as your own batches accumulate.
- **On-device:** export to **TFLite** and run on the Pi (a Pi Zero 2 W handles this comfortably;
  a Zero W is better used as a thin client that uploads frames for off-device training).
- **Consistent scale:** park the camera at a fixed lead-screw height so leaf-area is comparable
  across days → real growth curves.

## 2. Control (a recipe tuner) — *what should I change?*
Health signal + EC/level history + stage → adjustment to the nutrient schedule.

- Keep this **interpretable** (simple feedback rules or light Bayesian optimisation over the EC
  schedule), not a black box — so the device can explain *why* it changed, which fits the
  teaching goal.
- **Don't equate yellowing with "add nutrient."** Chlorosis has many causes (N or Fe deficiency,
  pH lock-out, root rot, light, natural senescence). Perception flags the symptom; the tuner
  weighs it against EC/level/pH history before acting.

## "Remembers future batches"
Each crop gets a **recipe profile** that updates from outcomes — days-to-harvest, mean health
score, and a yield proxy (total leaf area). Over time the profile converges on a schedule that
grows healthier crops on less water and nutrient. Roadmap: a shared **recipe cloud** so every
device's learning improves all of them.

## Data layout (suggested)
```
ml/
├── data/
│   ├── <crop>/<batch_id>/<day>.jpg   # raw canopy frames
│   └── labels.csv                    # frame, crop, day, stage, health, leaf_area
├── health_model.py                   # train + export TFLite (stub)
└── recipe_tuner.py                   # outcome -> schedule update (to be added)
```
