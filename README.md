# Indy Eleven | Fan Analytics & Attendance Forecasting

**University of Wisconsin–Madison MSBA Consulting Capstone · May 2026**  
**Team project** — developed collaboratively. This repository represents a portfolio-ready presentation of selected materials; individual contributions should be described accurately.

## Overview

Applied business analytics to a professional soccer club's fan-engagement and game-day attendance planning questions. The broader team capstone covered customer segmentation, geographic clustering, weather-based attendance forecasts, data-quality gaps and actionable marketing recommendations.

## Portfolio components

| Area | Business question | Demonstration |
|---|---|---|
| Fan segmentation | How do different ticket-buyer groups behave? | Described in original capstone recommendations; restricted Tableau extracts are excluded |
| Geographic insights | Where should marketing resources be focused? | Cluster map exists in the original project; publish only with permission |
| Attendance forecasting | How do rain, temperature and promotions relate to ticket scan rates? | **Real HTML/JavaScript prototype** in [`app/Weather.html`](app/Weather.html) |
| Model quality | How reproducible are published forecast assumptions? | Python evaluation/refit script in [`src/attendance_model.py`](src/attendance_model.py) |
| Decision support | How can findings shape operations and retention campaigns? | Narrative summary of capstone outcomes below |

## Business findings from team capstone

- Season-ticket holders accounted for about **5.9% of accounts** but **56.4% of ticket revenue**, suggesting a strong retention priority.
- Roughly **31% of transactions lacked ZIP-code information**, limiting confident geographical targeting.
- The project explored weather-sensitive game-day staffing and proactive fan communications.

**These are capstone-reported findings, not metrics calculated from the synthetic dataset in this repository.** Recommendations are proposals, not documented realized outcomes.

## Try the original predictor

Open [`app/Weather.html`](app/Weather.html) in a web browser. Enter tickets distributed, precipitation level, forecast temperature and whether a major match-day promotion is planned. The tool shows estimated scan rate and fan count alongside heuristic operational advice. This is a **historical capstone prototype**, not a validated production tool.

## Run the model-review code

```bash
python -m pip install -r requirements.txt
python src/attendance_model.py data/example_synthetic_matches.csv --refit
python -m unittest discover -s tests -v
```

The included CSV is **synthetic** and provided strictly to demonstrate how to execute the code. See [`docs/MODEL_REVIEW.md`](docs/MODEL_REVIEW.md) for the distinction between the original prototype and a statistical refit on privately held match-level data.

## Tech stack

- **Tableau:** geographic cluster visualization (original workbooks retained privately)
- **Python / NumPy:** model diagnostics and coefficient refitting
- **HTML / JavaScript:** interactive game-day attendance scenario calculator
- **Analytics:** segmentation, regression, data quality assessment, operational recommendations

## Responsible sharing

The source workbooks, customer-segmentation CSV, actual match-level CSV and Tableau packaged workbook **are intentionally excluded** because client and customer data may be confidential. Do not upload them publicly without explicit authorization. See [`docs/PRIVATE_DATA_GUIDE.md`](docs/PRIVATE_DATA_GUIDE.md).

## Credit

UW–Madison MSBA Capstone team: David Hadar, Breezy Hofmeister, Shu Kai Tan, and Chenyu Wang. Indy Eleven project context. No affiliation or endorsement is implied by this public demo.
