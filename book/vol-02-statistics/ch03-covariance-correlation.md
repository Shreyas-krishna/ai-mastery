# Volume 02 — Probability & Statistics
# Chapter 3: Covariance & Correlation, From First Principles

> Same method: story → intuition → each symbol justified → paper → code. This chapter reuses
> two things you own: **deviations** (xᵢ − x̄) and **"pool, then share"**. Nothing else is new
> except one idea: *multiply two deviations together*.

---

## Warm-up — story problems (paper, before §1)

Three problems, three distinct ideas.

1. **Ice cream and sunburn.** A beach kiosk logs daily temperature (°C) and ice creams sold
   for five days: (20, 30), (25, 45), (30, 60), (35, 70), (40, 95). Compute the mean of each
   column. For each day, write whether temperature was *above or below its mean*, and whether
   sales were *above or below theirs*. What do you notice about the pattern of above/below?
2. **Umbrellas.** Same kiosk, five *other* days, tracking rainfall (mm) and ice creams sold:
   (0, 90), (5, 70), (10, 55), (20, 30), (30, 10). Same exercise: means, then above/below for
   each. How does the pattern differ from problem 1?
3. **Shoe size and exam score.** Five students: shoe size and math score: (7, 80), (9, 45),
   (8, 90), (10, 60), (6, 55). Same exercise. What pattern — if any — do you see?

Problem 1 is "move together," 2 is "move opposite," 3 is "no relationship." The rest of
the chapter turns those three words into one number.

---

## 1. From one column to two

Chapters 1–2 described **one** variable: where it sits (mean), how much it spreads
(variance). Real questions are almost always about **two**: does studying more raise scores?
does temperature drive sales? does a bigger model mean lower loss? Every one of these asks:
*when x goes up, what does y do?*

Variance measured how x wobbles around its own mean. We now want: **when x is above its
mean, is y also above its mean?** That's the whole question. The tool is already in your
hands — deviations.

## 2. The sign trick — what multiplying two deviations tells you

Take one day from warm-up 1. Temperature 35 (mean 30 → deviation **+5**). Sales 70
(mean 60 → deviation **+10**). Both above their means. Now the move that makes the chapter:

**multiply the two deviations: (+5)(+10) = +50.**

Why multiply? Because of what signs do under multiplication:

| x deviation | y deviation | product | meaning |
|---|---|---|---|
| + | + | **+** | both above their means — moving together |
| − | − | **+** | both below — still moving together |
| + | − | **−** | x above, y below — moving opposite |
| − | + | **−** | x below, y above — moving opposite |

A **positive product** means "on this day, x and y were on the *same side* of their means."
A **negative product** means "opposite sides." And a product near **zero** means at least one
of them was sitting near its mean — no information either way.

That's the entire trick. Multiplication turns "same side / opposite side" into "+ / −", with
the *size* of the product saying how strongly.

## 3. Covariance: pool the products, share equally

One product describes one day. To describe the *relationship*, do what you did for variance:
compute the product for every day, pool them, share by n.

$$\text{Cov}(x, y) = \frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})$$

| Symbol | What it is |
|---|---|
| $x_i - \bar{x}$ | x's deviation on day i — how far above/below its own mean |
| $y_i - \bar{y}$ | y's deviation on day i |
| $(x_i - \bar{x})(y_i - \bar{y})$ | the sign trick: + if same side, − if opposite |
| $\sum_{i=1}^{n}$ | pool all n products |
| $\frac{1}{n}$ | share equally — the *mean* product |
| $\text{Cov}(x,y)$ | **covariance**: "co-variance" — how x and y vary *together* |

Read aloud: *"For each observation, multiply x's deviation by y's deviation; average the
products."*

- **Cov > 0** → mostly same-side → x and y rise and fall together (warm-up 1)
- **Cov < 0** → mostly opposite → one rises as the other falls (warm-up 2)
- **Cov ≈ 0** → signs cancel → no *linear* relationship (warm-up 3)

**Now the punchline you should see coming.** What is Cov(x, x) — the covariance of a
variable *with itself*? Substitute y = x in the formula: $(x_i - \bar{x})(x_i - \bar{x}) =
(x_i - \bar{x})^2$. So

$$\text{Cov}(x, x) = \frac{1}{n}\sum(x_i - \bar{x})^2 = \text{Var}(x)$$

**Variance is covariance with yourself.** Chapter 2 was a special case of this chapter. Every
time a formula generalizes an old one like this, check that the old one falls out — it's the
cheapest correctness test in mathematics.

## 4. The problem with covariance: units and scale

Compute Cov for warm-up 1 (you'll do this on paper): you'll get a number like **+230**. Big,
positive. Good — but 230 *what*? The product of a temperature deviation (°C) and a sales
deviation (ice creams) is in **°C · ice creams**. Meaningless as a unit, exactly as
"rupees²" was in Chapter 2.

Worse: it's not comparable. Measure temperature in Fahrenheit instead and every x-deviation
gets multiplied by 1.8 — so covariance is multiplied by 1.8 too — but the *relationship*
hasn't changed at all. **Covariance's size depends on the units you chose**, not just on how
tightly x and y move together. It tells you the *direction* reliably and the *strength* not
at all.

You've solved this exact problem once already. In Chapter 2, variance had squared units, so
you took a square root to get back to data units. Here, covariance has *mixed* units — so
we need to divide out *both* variables' scales.

## 5. Correlation: covariance with the units divided out

What has x's units? Its standard deviation σₓ. What has y's units? σᵧ. Divide covariance by
both:

$$r = \frac{\text{Cov}(x, y)}{\sigma_x \, \sigma_y}$$

| Symbol | What it is |
|---|---|
| $\text{Cov}(x,y)$ | the mean product of deviations, units: (x units)·(y units) |
| $\sigma_x$ | SD of x, units: x units |
| $\sigma_y$ | SD of y, units: y units |
| $r$ | **Pearson correlation coefficient** — units cancel completely: a pure number |

Look at the units: (x·y) / (x·y) = **dimensionless**. Switch to Fahrenheit: Cov gets ×1.8,
σₓ gets ×1.8, they cancel, r is unchanged. **Correlation is what's left of covariance once
you remove everything that depended on your choice of units.**

And it has a remarkable property that you'll prove in a later chapter: **−1 ≤ r ≤ +1**,
always, for any data.

- **r = +1** → every point sits exactly on a rising straight line
- **r = −1** → every point exactly on a falling line
- **r = 0** → no *linear* relationship
- **r = +0.8** → strong positive; **r = −0.3** → weak negative

*Why* it's bounded by 1: think of it as "covariance divided by the *largest* covariance the
two spreads could possibly produce" — the two SDs multiplied together is the ceiling. Full
proof needs an inequality you'll meet in linear algebra (Cauchy–Schwarz). Flagged, owed.

### Another view of the same formula

Standardize each variable first — the Chapter 2 laws in action: subtract the mean (shift,
doesn't change spread), divide by SD (scale to spread 1). Call these **z-scores**:

$$z_{x,i} = \frac{x_i - \bar{x}}{\sigma_x}, \qquad z_{y,i} = \frac{y_i - \bar{y}}{\sigma_y}$$

Then **r is just the covariance of the z-scores** — equivalently, the mean of the products
of z-scores. Correlation = covariance after putting both variables on the same
unit-free ruler. (Prove this equivalence on paper: exercise 7.)

## 6. Two warnings that interviewers love

**Correlation is not causation.** Ice cream sales and drowning deaths correlate strongly
(both rise in summer). Neither causes the other; a third variable — temperature — drives both.
r tells you two things move together; it is silent on *why*. Every "we found a correlation
between X and Y" headline you'll ever read should be met with "what's the third variable?"

**r measures *linear* relationship only.** Data on a perfect U-shape (y = x²) can have
r = 0 — y clearly depends on x, but not in a straight-line way. Warm-up 3's shoe sizes can
have r ≈ 0 because there's *no* relationship; a parabola has r ≈ 0 because the relationship
*isn't linear*. r can't tell these apart. Always plot before you trust a correlation
(you'll get plotting tools in Phase 1).

**Where you'll meet this forever:** the covariance matrix (Phase 2 linear algebra — PCA is
literally "find the directions of largest covariance"), feature correlation in every dataset
you'll ever clean, the "correlation between train and validation loss," attention scores
as (scaled) dot products of standardized vectors — the cosine similarity you'll use in RAG
is correlation's cousin.

## 7. On paper (no calculator; fractions and decimals are fine)

Photos to `exercises/vol-02/ch03/`.

**Easy**
1. For warm-up 1's data, build the full table: x, y, x−x̄, y−ȳ, product. Sum the products,
   divide by 5. That's Cov(x, y). Is the sign what you predicted?
2. Same for warm-up 2. Confirm the sign flips.

**Medium**
3. Warm-up 3 (shoes/scores). Compute Cov. Is it near zero? Now compute σ for each column
   and the correlation r. Is |r| small?
4. Compute σₓ and σᵧ for warm-up 1, then r. Then *redo* with temperature converted to
   Fahrenheit (F = 1.8C + 32). Cov changes — by what factor? r — does it change? Explain
   using the Chapter 2 shift/scale laws.
5. Take x = (1, 2, 3, 4, 5) and y = 2x = (2, 4, 6, 8, 10). Predict r before computing. Then
   compute. Then y = −2x + 20 — predict, compute.

**Hard**
6. Prove Cov(x, x) = Var(x) formally from the definition (two lines). Then prove
   Cov(x, y) = Cov(y, x) — why is this obvious once you write it down?
7. Prove that the mean of the products of z-scores equals Cov(x, y)/(σₓσᵧ). (The constants
   1/σₓ and 1/σᵧ can be pulled out of a sum — the H7 move.)
8. **Computational formula, again.** Chapter 2's H7 gave Var = mean(x²) − x̄². Derive the
   analogue: Cov(x, y) = mean(x·y) − x̄·ȳ. Same three moves: expand (xᵢ − x̄)(yᵢ − ȳ), split
   the sum into four, use Σxᵢ = n·x̄ and Σyᵢ = n·ȳ. Verify numerically on warm-up 1.

## 8. Into the computer

`src/stats/covariance.py` (or extend `variance.py` into `dispersion.py` — a design decision,
defend it). Reuse `mean`, `variance`, `std_dev`, `sqrt_newton`. Forbidden: `sum`, `len`,
`zip` (build the index loop yourself — you need to walk two lists in lockstep; think about
how, and what to do if their lengths differ), `statistics`, `numpy`.

```
def covariance(x, y):
    # guard: same length (how do you check without len?), non-empty, >= 2 points
    # x_bar, y_bar once; one loop over indices; pool products; share by n

def correlation(x, y):
    # covariance / (std_dev(x) * std_dev(y))
    # guard: what if either std_dev is 0? What does that mean about the data,
    # and what should r be — or should it raise? Decide and defend.
```

Test block, tolerance-based:
- Cov(x, x) == variance(x) for Dataset A — the generalization check
- Cov(x, y) == Cov(y, x)
- correlation of x with 2x → 1 (within tol); with −2x+20 → −1
- warm-up 1 paper answers for Cov and r
- Fahrenheit invariance: correlation(x, y) == correlation(1.8x+32, y)
- H8 computational formula cross-check, computed independently in the test block
- guards: mismatched lengths raise; constant y (σ = 0) does whatever you decided

**Gate questions (debrief, no book):**
- Why multiply the two deviations? What does the sign of the product mean?
- Cov(x, x) equals what? Why does that matter as a check?
- Why does covariance fail as a measure of *strength*? What fixes it?
- What are the bounds of r, and what do the extremes mean?
- Two things r cannot tell you.

---
*Next: Chapter 4 — from summary statistics to data you haven't seen: what "probability"
means, and why the mean of a sample is not the mean of the population.*
