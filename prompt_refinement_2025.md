# Prompt Refinement Notes — 2025 Dataset

## Case 1
**Initial (Failed):** “Which AI model had the biggest growth?”
- **Issue:** Dataset doesn’t define “growth” (no prior-period comparison metric, no adoption trend column).

**Refined:** “Which AI model had the highest number of deployments in 2025?”
- **Why it works:** Uses available per-model deployment counts from the dataset.
- **Expected outcome:** ✅ LLM can rank models by deployment count when provided.

---

## Case 2
**Initial (Failed):** “What was the global renewable energy market share?”
- **Issue:** Dataset includes country-wise energy generation data but no global aggregation.

**Refined:** “What percentage of total electricity generation in 2025 came from renewable sources in the dataset’s listed countries?”
- **Why it works:** Forces model to sum renewables across all countries, then divide by total generation.
- **Expected outcome:** ✅ LLM computes renewable share from provided table.

---

## Case 3
**Initial (Ambiguous):** “Which sector saw the most improvement in emissions reduction?”
- **Issue:** “Improvement” is vague; dataset only contains emissions totals per sector.

**Refined:** “Which sector recorded the largest absolute decrease in CO₂ emissions between 2024 and 2025?”
- **Why it works:** Defines “improvement” as numerical decrease, with a clear comparison between years.
- **Expected outcome:** ✅ LLM can calculate the difference and identify the sector.

---

## Case 4
**Initial (Failed):** “Which country led in EV adoption?”
- **Issue:** “Adoption” could mean new sales, total fleet size, or market share; dataset has separate columns.

**Refined:** “Which country had the highest number of new electric vehicle registrations in 2025?”
- **Why it works:** Uses a specific, available metric (new registrations) to define adoption.
- **Expected outcome:** ✅ LLM can rank countries by new EV registration column.
