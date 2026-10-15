# Data privacy and publication notes

This repository intentionally excludes original Indy Eleven attendance spreadsheets, match-level data exports, customer segmentation CSVs, and embedded Tableau extracts. These might be non-public business data even where names and emails are not present.

Keep original source files privately. Do not commit `.twbx` files without permission: Tableau packaged workbooks may embed sensitive extracts. Never upload customer identifiers, email addresses, ZIP-level segmentation tied to individuals, or internal notes without express authorization.

The included `data/example_synthetic_matches.csv` is generated from a simulation for code demonstrations, not the team's actual match results. The `app/Weather.html` file is the user-supplied historical prototype. Confirm permission to publicly distribute client-specific code and the model's coefficients before making the repository public.

A screenshot of the original cluster map should only be added with team/client permission; avoid distributing embedded underlying data.
