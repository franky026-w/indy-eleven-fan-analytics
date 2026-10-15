"""Reproduce and evaluate the attendance predictor on authorized CSV exports.

No original team data is distributed in this public portfolio template.
"""
import argparse
import csv
import math
from pathlib import Path

FIELDS = ("Tickets_Out", "Attendance_Pct", "Rain_Level", "Temp_Dev", "Is_Themed")


def deployed_prediction(rain_level, temp_dev, is_themed):
    """Formula in the supplied 2026 Weather.html, clipped to [5%,65%]."""
    p = .390 - .086 * rain_level - .0003 * temp_dev + .08 * is_themed
    return min(.65, max(.05, p))


def load_rows(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader=csv.DictReader(f)
        missing=set(FIELDS)-set(reader.fieldnames or ())
        if missing: raise ValueError("Missing fields: " + ", ".join(sorted(missing)))
        rows=[]
        for r in reader:
            if not all(r.get(k) for k in FIELDS): continue
            vals={k:float(r[k]) for k in FIELDS}
            if vals["Tickets_Out"]<=0 or not (0<=vals["Attendance_Pct"]<=1): continue
            rows.append(vals)
    if not rows: raise ValueError("No valid rows")
    return rows


def fit_ols(rows):
    """Least squares with 4 coefficients; numpy is required only for refitting."""
    import numpy as np
    x=np.array([[1, r["Rain_Level"],r["Temp_Dev"],r["Is_Themed"]] for r in rows], dtype=float)
    y=np.array([r["Attendance_Pct"] for r in rows],dtype=float)
    beta=np.linalg.lstsq(x,y,rcond=None)[0]
    return beta.tolist()


def evaluate(rows):
    err=[abs(r["Attendance_Pct"]-deployed_prediction(r["Rain_Level"],r["Temp_Dev"],r["Is_Themed"])) for r in rows]
    return {"n":len(rows),"mae_pct_points":100*sum(err)/len(err)}


def main():
    p=argparse.ArgumentParser()
    p.add_argument("csv_path",type=Path,help="Authorized match-level dataset (use demo CSV to test)")
    p.add_argument("--refit",action="store_true",help="Refit OLS on supplied input; exploratory, not deployment")
    args=p.parse_args()
    rows=load_rows(args.csv_path)
    metrics=evaluate(rows)
    print(f"Rows: {metrics['n']} | Existing-tool MAE: {metrics['mae_pct_points']:.2f} percentage points")
    if args.refit:
        b=fit_ols(rows)
        print("OLS coefficients [intercept, rain_level, abs(temp-72F), theme]:", [round(v,6) for v in b])
        print("Caution: in-sample association != causal effect; validate on unseen seasons before using coefficients.")

if __name__=='__main__':main()
