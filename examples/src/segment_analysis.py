"""Reproducible demonstration using SYNTHETIC fan data only.
No underlying Indy Eleven customer records are included.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / 'data' / 'synthetic_fan_profiles.csv')
summary = df.groupby('fan_segment').agg(
    accounts=('fan_segment','size'),
    average_games=('annual_games','mean'),
    total_revenue=('synthetic_revenue_usd','sum')
).sort_values('accounts',ascending=False)
summary['account_share_pct'] = 100 * summary.accounts / summary.accounts.sum()
print(summary.round(2).to_string())
ax = summary['account_share_pct'].plot.barh(title='Illustrative fan segment distribution (synthetic data)')
ax.set_xlabel('Share of synthetic profiles (%)')
plt.tight_layout()
plt.savefig(ROOT / 'visualizations' / 'synthetic_segment_chart.png', dpi=170)
