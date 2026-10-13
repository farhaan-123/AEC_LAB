# Discrete Probability Distributions

Educational web application for the undergraduate AIML laboratory. It is built step by step from six prompts. The current version implements the **Binomial Distribution** module; Poisson and Geometric are placeholders in the navigation.

Plain HTML, CSS and JavaScript only. No installation, build step or external libraries.

## How to run

Open `index.html` in any browser (double-click it). `index.html` in the repository root is the final version (after Prompt 6).

## Publish with GitHub Pages (optional)

1. Push the repository to GitHub.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**, select `main` and `/ (root)`, and save.
4. The site will be available at `https://<your-username>.github.io/<repository-name>/`.

## Repository structure

```text
.
├── README.md
├── index.html                      final application (Prompt 6)
├── prompt-1-basic_structure/       index.html + PROMPT.md
├── prompt-2-inputs/
├── prompt-3-statistics/
├── prompt-4-pmf/
├── prompt-5-cdf/
└── prompt-6-pmf_graph/
```

Each `prompt-N-*` folder contains the application as it stands after that prompt (`index.html`) and the exact prompt text (`PROMPT.md`). Each version builds on the previous one.

## Features of the final version

- Navigation: Home, Binomial, Poisson, Geometric
- Inputs n (default 20) and p (default 0.35) with validation
- Statistic cards: mean, variance, standard deviation, E[X²], skewness
- PMF calculator P(X = k)
- CDF calculator P(X ≤ k) and P(X > k)
- PMF bar chart with a dashed mean line and tooltip, updating when n or p changes

## Formulas

| Quantity | Formula |
|---|---|
| Mean | np |
| Variance | np(1−p) |
| Second moment E[X²] | Variance + Mean² |
| Skewness | (1−2p) / √(np(1−p)) |
| PMF | P(X=k) = C(n,k) pᵏ (1−p)ⁿ⁻ᵏ |
| CDF | P(X ≤ k) = Σ P(X=i), i = 0…k |

Check for n = 20, p = 0.35: mean = 7, variance = 4.55.

## Notes

- n is limited to 1–500 so the chart stays readable.
- Skewness is shown as "undefined" when the variance is 0 (p = 0 or p = 1).
- PMF values are computed with log-factorials for numerical stability.

## Prompts used

### Prompt 1 — Create the basic lab application

Folder: `prompt-1-basic_structure/`

```text
Create a simple educational web application for an undergraduate AIML laboratory.
Title:
Discrete Probability Distributions
The application will eventually contain:
1. Binomial Distribution
2. Poisson Distribution
3. Geometric Distribution
For now, implement only the basic application structure and the Binomial Distribution module.
Keep the UI simple and clean. Do not add unnecessary features.
Create a navigation/header with:
- Home
- Binomial
- Poisson
- Geometric
Only the Binomial page needs to be functional at this stage.
```

### Prompt 2 — Add Binomial inputs

Folder: `prompt-2-inputs/`

```text
Implement the Binomial Distribution section.
Add two input controls:
- Number of trials n
- Probability of success p
Set default values:
n = 20
p = 0.35
Validate the inputs:
- n must be a positive integer
- p must be between 0 and 1
Display the selected values clearly.
Do not add simulation yet.
```

### Prompt 3 — Calculate Binomial statistics

Folder: `prompt-3-statistics/`

```text
Add the Binomial probability calculations using the selected n and p.
Calculate and display:
- Mean
- Variance
- Standard deviation
- Second moment E[X²]
- Skewness
Use the following formulas:
Mean:
np
Variance:
np(1-p)
Second moment:
Variance + Mean²
Skewness:
(1-2p) / sqrt(np(1-p))
Display the results in simple statistic cards.
For the default values n=20 and p=0.35, verify that the mean is 7 and variance is 4.55.
```

### Prompt 4 — Add PMF

Folder: `prompt-4-pmf/`

```text
Add a Binomial PMF calculator.
For:
X ~ Binomial(n,p)
calculate:
P(X = k)
Allow the student to enter k.
Validate that:
0 <= k <= n
Display the probability clearly.
Also display the mathematical expression:
P(X=k) = C(n,k) p^k (1-p)^(n-k)
Explain in one simple sentence what the result means.
```

### Prompt 5 — Add CDF

Folder: `prompt-5-cdf/`

```text
Add a Binomial CDF calculator.
Allow the student to enter k.
Calculate:
P(X <= k)
Also calculate:
P(X > k) = 1 - P(X <= k)
Display both results.
Explain:
“P(X <= k) means the probability of getting k or fewer successes.”
```

### Prompt 6 — Add Binomial PMF graph

Folder: `prompt-6-pmf_graph/`

```text
Add a bar chart showing the Binomial PMF.
X-axis:
Number of successes X
Y-axis:
Probability P(X)
Plot values for:
X = 0, 1, 2, ..., n
Use the current values of n and p.
Add a vertical dashed reference line at the mean.
Add a tooltip showing:
X = value
P(X=value) = probability
Update the graph automatically whenever n or p changes.
```

