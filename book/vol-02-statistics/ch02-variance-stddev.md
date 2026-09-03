# Volume 02 — Probability & Statistics
# Chapter 2: Variance & Standard Deviation, From First Principles

> Built the same way as Chapter 1: intuition → each symbol named → each operation
> justified → by hand on paper → only then code.

---

## 1. The mean's blind spot — a problem you already discovered

These are *your* datasets from the re-drill:

- **Dataset A:** 0, 5, 25 → pot = 30, mean = 10
- **Dataset B:** 10, 10, 10 → pot = 30, mean = 10

Identical means. Utterly different realities. In B, the mean *is* the data. In A, the mean
describes nobody — no value in A even equals 10. This is the information the pot destroyed
in Chapter 1, coming back to bite.

So we need a second number, one that answers: **"how far, typically, do the values sit from
their mean?"** That number is what this chapter builds. Mean = *where is the data centered?*
Spread = *how much should I trust that center?*

## 2. First attempt: just measure the distances

The natural move: for each value, compute how far it is from the mean. These are the
**deviations**:

$$d_i = x_i - \bar{x}$$

For Dataset A (mean 10):

| $x_i$ | deviation $x_i - \bar{x}$ |
|---|---|
| 0 | −10 |
| 5 | −5 |
| 25 | +15 |

The sign carries meaning: negative = below the mean, positive = above.

Now the obvious plan — take the *mean of the deviations* to get "typical distance":

$$\frac{(-10) + (-5) + (+15)}{3} = \frac{0}{3} = 0$$

Zero. Try it on any dataset — always zero. This is not a coincidence, and you already know
why: **you proved it** in Chapter 1, exercise 6. The mean is the balance point; deviations
above exactly cancel deviations below, *by construction of the mean itself*. Our measuring
tool self-destructs.

## 3. Killing the cancellation

The problem is the signs. −10 and +15 are both *distances*, but they eat each other.
Two honest fixes:

**Fix 1 — strip the signs (absolute value):** treat −10 as 10. This works, and the result
has a name (mean absolute deviation, MAD). It is used in the real world. But it has a flaw
we'll be able to *see* only later: the absolute value has a sharp corner at zero, and sharp
corners break calculus. Since everything in ML runs on calculus (gradient descent is coming),
statisticians took the other road.

**Fix 2 — square the deviations:** (−10)² = 100, (+15)² = 225. Squaring kills the sign
(negative × negative = positive) **and** is perfectly smooth for calculus. Bonus property,
neither good nor bad, just true: squaring punishes big deviations disproportionately —
a deviation of 15 contributes 225 while three deviations of 5 contribute only 75 combined.
The squared measure *cares more about outliers*. Remember this; it explains half of ML loss
function design.

So the recipe: deviations → square each → then do the most natural thing with a list of
numbers... take their **mean**. Pool and share, exactly Chapter 1.

## 4. Variance: the formula, then every symbol

$$\sigma^2 = \frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})^2$$

| Symbol | Name | What it means, in our story |
|---|---|---|
| $x_i$ | the i-th value | same as Chapter 1 |
| $\bar{x}$ | x-bar | the mean — computed FIRST, then held fixed while we measure against it |
| $x_i - \bar{x}$ | deviation | how far value i sits from the mean, with direction (sign) |
| $(\;\cdot\;)^2$ | squaring | kills the sign so distances can't cancel; smooth for later calculus |
| $\sum_{i=1}^{n}$ | sigma | pool all the squared deviations into one pot |
| $\frac{1}{n}$ | one n-th | share the pot equally — the *mean* of the squared deviations |
| $\sigma^2$ | "sigma squared" | the answer: **variance**. σ is the Greek s, for *spread*. Why it's written as a square — §5 explains |

Read aloud as a sentence: *"For each value, measure its distance from the mean, square it,
pool all the squares, share equally. The result is the variance."*

Variance is literally **a mean** — the mean of squared deviations. One new idea (deviations),
one trick (squaring), and then machinery you fully own.

**Compute it for your datasets:**

Dataset A: $\frac{(-10)^2 + (-5)^2 + (15)^2}{3} = \frac{100 + 25 + 225}{3} = \frac{350}{3} \approx 116.67$

Dataset B: $\frac{0^2 + 0^2 + 0^2}{3} = 0$

The blind spot is cured: same means, but A screams "spread out!" while B reports "no spread
at all." Variance = 0 has an exact meaning: *every value equals the mean.*

## 5. The units problem, and the square root that fixes it

If the data is in rupees, deviations are in rupees — but *squared* deviations are in
**rupees²**, whatever that is. Variance lives in squared units; you cannot compare it to
the data directly. "Mean 10, variance 116.67" mixes rupees with rupees².

The repair: undo the squaring at the very end. Take the square root:

$$\sigma = \sqrt{\sigma^2} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})^2}$$

This is the **standard deviation** — "standard" as in *typical*: the typical distance of a
value from the mean, back in the original units. For Dataset A: σ = √116.67 ≈ 10.8. Sanity
check against the raw deviations (10, 5, 15): a typical distance of ~10.8 sits right among
them. It will always pass this smell test.

And now the notation confesses: we write variance as σ² because the square root — σ — is
the more human-readable quantity. Variance is the standard deviation's square, defined
first, named second.

**Where you'll meet this pair forever:** the normal distribution is parameterized by (μ, σ);
batch normalization divides by σ; weight initialization schemes choose σ; "the loss
plateaued but variance across seeds is huge" is an everyday ML sentence. This chapter is
load-bearing for the entire program.

## 6. One honest flag: n versus n−1

In the wild you will see the same formula with $\frac{1}{n-1}$ instead of $\frac{1}{n}$
(your future libraries: `numpy.var(x)` uses n, `pandas` uses n−1 by default — a classic
gotcha). The short story: dividing by n is correct when your data is the *whole population*;
n−1 compensates for a subtle bias that appears when your data is merely a *sample* and the
mean itself was estimated from that same sample. The full proof needs expectation algebra
we haven't built — it gets its own chapter later, with the proof done properly. Until then
we divide by n and we *know we owe a debt*. Flag it, don't fear it.

## 7. On paper — do these now (no calculator, no computer)

Photos go to `exercises/vol-02/ch02/`, naming law applies.

**Easy**
1. Compute mean, variance, and standard deviation of: 2, 4, 6, 8. Show the deviation table
   (value, deviation, squared deviation) as in §2.
2. Without computing anything: dataset C = 7, 7, 7, 7, 7. State its variance and standard
   deviation, and justify in one sentence.

**Medium**
3. Datasets P = 1, 5, 9 and Q = 4, 5, 6. Predict which has larger variance *before*
   computing, then verify both. State the means first — what do you notice?
4. A dataset has mean 20 and variance 0. What is the value of every single element? How many
   elements are there — can you know? Explain both answers.
5. Take Dataset A (0, 5, 25) and add 100 to every value. Compute the new mean and new
   variance. Which changed, which didn't, and *why* — answer in deviation language.

**Hard**
6. Now take Dataset A and *multiply* every value by 2. Predict the new variance before
   computing (§3's disproportionate-punishment remark is the hint), then verify. State the
   general rule for what multiplying data by a constant c does to variance and to standard
   deviation.
7. Prove, algebraically, that $\frac{1}{n}\sum(x_i - \bar{x})^2 = \left(\frac{1}{n}\sum x_i^2\right) - \bar{x}^2$
   — in words: *"the mean of the squares minus the square of the mean."* Expand the square
   $(x_i - \bar{x})^2$ inside the sum, split the sum into three sums, and use the two facts
   you already own: $\sum x_i = n\bar{x}$, and $\bar{x}$ is a constant that can be pulled out
   of a sum. Then verify the shortcut numerically on Dataset A. (This identity is how real
   systems compute variance in one pass over the data — you will use it in your code's
   test block.)

## 8. Into the computer

Rules: pure Python. **Forbidden:** `sum()`, `len()`, `statistics`, `numpy`, `math`.
**Required:** import and reuse your own `mean()` — you built it, it's gated, it's now a
library *you* own. (First taste of why modules exist.)

Build in `code/stats/`:

```
def variance(values):
    # reuse mean(); one loop over values; guard clause consistent with mean()'s.

def std_dev(values):
    # square root of variance. math.sqrt is forbidden — but the ** operator is
    # pure Python and allowed: x ** 0.5
```

Steps:
1. Write both functions. Think: what should `variance([5])` return, and is a single value
   "spread"? Decide and defend at the debrief.
2. Test block (`if __name__ == "__main__":` with asserts) checking against your §7 paper
   answers — including Datasets A and B, and the shortcut identity from exercise 7 as a
   cross-check.
3. Commit (recipe applies — read it aloud) and push.

**Stretch (optional, real from-scratch honor):** `x ** 0.5` still leans on Python's
machinery. Newton's method finds √a with nothing but arithmetic: start with a guess g,
repeatedly replace g with (g + a/g) / 2, watch it converge in a handful of steps. If you
attempt it, write `sqrt_newton(a)` and assert it matches `a ** 0.5` to 6 decimal places.
This exact idea — *iteratively improving a guess* — is gradient descent's grandfather.

**Gate questions for the debrief** (answer without the book):
- Why can't we use the plain mean of deviations? Whose theorem is that — i.e., which result
  *you proved* makes it fail?
- Why squaring instead of absolute value? Two reasons.
- Why does standard deviation exist at all, if we already have variance?
- What does variance = 0 tell you, exactly?
- Adding a constant to all data: what happens to mean and to variance, and why?

---
*Next: Chapter 3 — from one variable to two: covariance and correlation (does x rising mean
y rises?), built from the same deviations.*
