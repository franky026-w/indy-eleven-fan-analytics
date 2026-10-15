# Model review & reproducibility

The original HTML predictor implements the following fixed rule:

`predicted_scan_rate = clip(0.390 - 0.086 * rain_level - 0.0003 * abs(temp_F - 72) + 0.080 * is_themed, 0.05, 0.65)`

It predicts scanned attendees as `round(tickets_out * predicted_scan_rate)`.

## Private-data consistency review (not bundled)

The uploaded consolidated match data has 56 records: 17 from 2023, 20 from 2024, and 19 from 2025. An exploratory ordinary least squares refit on these 56 records produced approximate coefficients:

- Intercept: 0.39024
- Rain intensity (per level): -0.08664
- Absolute temperature deviation from 72°F: -0.000309
- `Is_Themed`: -0.02620

The prototype HTML instead uses a +0.080 theme adjustment. **These estimates are not interchangeable.** The difference could stem from the original model's feature selection, subjective intervention assumption, confounding, coding, or a different fitting sample. The fixed prototype yielded roughly **10.26 percentage-point in-sample mean absolute error** on the uploaded consolidated rows. This is descriptive in-sample evaluation, not a cross-validated performance claim.

Without holdout-year tests, confidence intervals, and permission to publish the data, do not portray the prototype as a validated production forecasting model. Treat staffing guidance in the HTML as heuristic suggestions, not formally calibrated recommendations.

To reproduce locally using data you are authorized to process:

```bash
python src/attendance_model.py private_data/final_merged_attendance_data.csv --refit
```
