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
# Discrete Probability Distributions Explorer

An interactive educational web application for exploring the **Binomial**, **Poisson** and **Geometric** distributions. Built for **Lab Program 2** (Module 2, CO2) of the *Statistical Data Analysis & Visualization* laboratory, Semester III.

Change a distribution's parameters and instantly see its statistics, probabilities and PMF graph update.

> **Aim of the lab:** to compute and visualize discrete probability distributions, and to calculate their expectations, moments and variance using real-world, ML-relevant examples.

---

## Table of Contents

- [Features](#features)
- [Distributions Covered](#distributions-covered)
- [Formulas Used](#formulas-used)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Lab Exercises](#lab-exercises)
- [Verification Values](#verification-values)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Author and Acknowledgements](#author-and-acknowledgements)
- [License](#license)

---

## Features

The app has four navigation items: **Home**, **Binomial**, **Poisson** and **Geometric**. Each distribution tab provides the same five sections:

1. **Parameter inputs** with validation and a clear display of the selected values
2. **Statistics cards:** Mean, Variance, Standard Deviation, Second Moment E[X²] and Skewness
3. **PMF calculator:** P(X = k), with the formula and a one-line plain-English meaning
4. **CDF calculator:** P(X ≤ k) and P(X > k)
5. **PMF bar chart** with a dashed vertical line at the mean and a hover tooltip, updating live as parameters change

Other highlights:

- Inline validation, so invalid input never produces `NaN` or a crash
- Numerically stable probability calculations (no raw factorial overflow for large n or k)
- Clean, responsive layout that works on laptop and phone
- Runs entirely in the browser, with no backend

---

## Distributions Covered

| Distribution | Main question | ML / industry example |
|---|---|---|
| **Binomial**(n, p) | How many successes occur in n trials? | Number of correct predictions out of 20; defective products in a batch |
| **Poisson**(λ) | How many events occur in a fixed interval? | Anomalies per hour; security alerts per 10 minutes |
| **Geometric**(p) | How many trials until the first success? | Attempts until the first successful candidate; retries until a request succeeds |

A simple way to remember them:

- Binomial → **count successes**
- Poisson → **count events**
- Geometric → **count attempts**

---

## Formulas Used

| | Binomial(n, p) | Poisson(λ) | Geometric(p) |
|---|---|---|---|
| **Support** | k = 0, 1, …, n | k = 0, 1, 2, … | k = 1, 2, 3, … |
| **PMF** | C(n,k) pᵏ (1−p)ⁿ⁻ᵏ | e⁻λ λᵏ / k! | (1−p)ᵏ⁻¹ p |
| **Mean** | np | λ | 1/p |
| **Variance** | np(1−p) | λ | (1−p)/p² |
| **Skewness** | (1−2p) / √(np(1−p)) | 1/√λ | (2−p) / √(1−p) |
| **P(X ≤ k)** | Σ PMF(i), i = 0..k | Σ PMF(i), i = 0..k | 1 − (1−p)ᵏ |
| **P(X > k)** | 1 − P(X ≤ k) | 1 − P(X ≤ k) | (1−p)ᵏ |

Common to all three:

- Standard deviation = √Variance
- Second moment: E[X²] = Variance + Mean²

The Geometric distribution here uses the **"number of trials until the first success"** definition (support starting at 1), matching `scipy.stats.geom`.

---

## Getting Started

### Prerequisites

- A modern web browser (Chrome, Edge, Firefox or Safari)
- *(Optional)* Node.js, if the project uses a build step

### Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### Run the app

**If the project is plain HTML/CSS/JS:** open `index.html` in your browser, or serve it locally:

```bash
# Python
python -m http.server 8000
# then visit http://localhost:8000
```

**If the project uses Node (for example React or Vite):**

```bash
npm install
npm run dev
```

> Update this section to match how your project is actually built and run.

---

## Usage

1. Open the app and pick a distribution from the header (**Binomial**, **Poisson** or **Geometric**).
2. Enter the parameters. Inputs are validated as you type.
3. Read the statistics cards for the mean, variance, standard deviation, E[X²] and skewness.
4. Enter a value of **k** in the PMF and CDF calculators to get P(X = k), P(X ≤ k) and P(X > k).
5. Study the PMF graph. Hover over a bar to see its exact probability, and watch the dashed line mark the mean.

### Default values

| Distribution | Default parameters |
|---|---|
| Binomial | n = 20, p = 0.35 |
| Poisson | λ = 4 |
| Geometric | p = 0.25 |

### Input validation

| Distribution | Parameter rules | Rules for k |
|---|---|---|
| Binomial | n is a positive integer; 0 ≤ p ≤ 1 | integer, 0 ≤ k ≤ n |
| Poisson | λ > 0 | integer, k ≥ 0 |
| Geometric | 0 < p ≤ 1 | integer, k ≥ 1 |

---

## Lab Exercises

These exercises follow the lab sheet and use the app instead of Python code. For each one, record your numerical results, graph observations and an inference.

### Use case 1: Manufacturing quality control

An AI vision system classifies each product as defective or non-defective (assumed defect probability p = 0.05).

| Step | Module | Inputs | What to do |
|---|---|---|---|
| 1 | Binomial | n = 20, p = 0.05 | Note the mean and variance, and compute P(X = 2). The lab sheet gives P(X = 2) ≈ 0.1887 and an expected 1 defect per batch. |<img width="1052" height="380" alt="binomial p=0 05" src="https://github.com/user-attachments/assets/578ac46d-69bc-4047-b08c-8bc41fc36317" />

| 2 | Binomial | n = 20, p = 0.10 | Observe how the distribution shifts toward larger defect counts. |
<img width="1052" height="380" alt="binomial p=0 10" src="https://github.com/user-attachments/assets/ef57dd5d-412c-48e6-b052-ad13097d4b3f" />

| 3 | Poisson | λ = 5 (5 defects per 100 products) | Compute P(X = 3) ≈ 0.1404 and compare with the Binomial results. |<img width="1052" height="380" alt="poisons lambda=5" src="https://github.com/user-attachments/assets/345f01f2-2963-4b35-a1ed-d9133194e7f8" />

| 4 | Geometric | p = 0.05 | Examine the chance of the first defect on different inspections. The expected wait is 20 inspections. |<img width="1052" height="380" alt="geomectric X=1" src="https://github.com/user-attachments/assets/057beb51-5b9a-409a-9e0e-7758431c67f7" />


### Use case 2: Cloud operations and cybersecurity monitoring

Based on 12 ten-minute monitoring intervals (1,200 API requests, 27 failures, 36 security alerts):
observed failure rate = 27/1200 = 0.0225, and average alerts per interval = 36/12 = 3.

| Step | Module | Inputs | What to do |
|---|---|---|---|
| 1 | Binomial | n = 100, p = 0.0225 | Compute P(X = 3) failures and view the PMF. Expected failures = 2.25. |
<img width="1052" height="380" alt="geomectric X=1" src="https://github.com/user-attachments/assets/f137f445-d8a0-40df-932c-8339b001508d" />
| 2 | Poisson | λ = 3 | Compute P(0), P(1), P(2), P(3) and higher counts. P(X = 5) ≈ 0.1008. |
<img width="1052" height="380" alt="geomectric X=1" src="https://github.com/user-attachments/assets/7b23fae8-2ca5-4ca9-ae00-eb993d0607df" />
<img width="1052" height="380" alt="geomectric X=1" src="https://github.com/user-attachments/assets/9eafb432-59cd-4a22-99b4-2ee7ce53580a" />
<img width="1052" height="380" alt="geomectric X=1" src="https://github.com/user-attachments/assets/7d610cc9-10f7-4229-879a-e7f6a440231c" />
<img width="1052" height="380" alt="geomectric X=1" src="https://github.com/user-attachments/assets/092f4d8f-85ed-46d8-b1a4-a803eaac339f" />

| 3 | Poisson | λ = 2, 3, 5 | Compare the three graphs and observe the shift. |
<img width="1052" height="380" alt="geomectric X=1" src="https://github.com/user-attachments/assets/4900cc29-798a-4dd4-8d60-f671e7463285" />
<img width="1052" height="380" alt="geomectric X=1" src="https://github.com/user-attachments/assets/72135c96-89fe-4fd5-a607-3c781f325b1b" />
<img width="1052" height="380" alt="geomectric X=1" src="https://github.com/user-attachments/assets/b7bb0a70-4757-408f-94ac-406e6018093e" />
| 4 | Geometric | p = 0.8 | Compute success on the 1st, 2nd and 3rd attempt. P(X = 3) = 0.032 and E[X] = 1.25. |
<img width="1052" height="380" alt="geomectric X=1" src="https://github.com/user-attachments/assets/046c3fbf-c45d-46bf-8b1c-f664ea0be2dc" />
<img width="1052" height="380" alt="geomectric X=1" src="https://github.com/user-attachments/assets/88418b9d-3ac4-4ff6-abfe-ecf2787863dc" />
<img width="1052" height="380" alt="geomectric X=1" src="https://github.com/user-attachments/assets/c236f404-74bf-44e2-a8a8-83d7f45d6dfd" />


> The retry probability (p = 0.8) is an assumed parameter, not estimated from the monitoring table. Real retries may be dependent, particularly during an outage.

### Other worked examples from the lab sheet

- **Binomial, ML classification:** 20 images, p = 0.35 → mean 7 correct classifications. P(X ≤ 10) and P(X = 7) are the lab's CDF and PMF examples.
- **Geometric, candidate generation:** p = 0.3 → E[X] = 3.3333, P(X = 1) = 0.3 and P(X > 5) = 0.7⁵ ≈ 0.1681.

---

## Verification Values

Use these to confirm the app calculates correctly. These are derived from the formulas above.

| Case | Expected results |
|---|---|
| **Binomial**, n = 20, p = 0.35 | Mean 7, Variance 4.55, Std ≈ 2.1331, E[X²] = 53.55, Skewness ≈ 0.1406 |
| **Poisson**, λ = 4 | Mean 4, Variance 4, Std 2, E[X²] = 20, Skewness 0.5, P(X = 3) ≈ 0.195367, P(X ≤ 3) ≈ 0.433470 |
| **Geometric**, p = 0.25 | Mean 4, Variance 12, Std ≈ 3.4641, E[X²] = 28, Skewness ≈ 2.0207, P(X = 3) = 0.140625, P(X ≤ 3) = 0.578125 |
| **Geometric**, p = 0.3 | Mean ≈ 3.3333, P(X = 1) = 0.3, P(X > 5) ≈ 0.1681 |

Sanity checks that should always hold:

- PMF values sum to approximately 1 across the plotted range
- P(X ≤ k) + P(X > k) = 1 for every k

---

## Project Structure


.
├── index.html          # App shell and navigation
├── css/
│   └── styles.css      # Styling
├── js/
│   ├── main.js         # Tab navigation and shared utilities
│   ├── binomial.js     # Binomial module
│   ├── poisson.js      # Poisson module
│   └── geometric.js    # Geometric module
└── README.md
```

---


---

## Author and Acknowledgements

- **Author:** *FARHAAN AHMED*
- **Course:** Statistical Data Analysis & Visualization Laboratory, Semester III
- **Lab Program 2** designed by Prof. Sanjay M. Belgaonkar

---

