# Volume 02 — Probability & Statistics
# Chapter 1: The Mean, From First Principles

> **Style note:** this chapter is the template for how every formula in this program is taught:
> intuition → each symbol named → each operation justified → by hand on paper → only then code.

---

## 1. Before any formula: the problem the mean solves

Five friends earn different amounts of money in a day: ₹100, ₹150, ₹80, ₹120, ₹50.

Question: *"If everyone had earned the same amount, with the group's total unchanged — what
would that amount be?"*

That imaginary "equal share" is the **mean**. It answers: *what single number best stands in
for all of these numbers?* That's the entire idea. Everything else is bookkeeping.

## 2. The two ingredients, justified one at a time

### Ingredient 1 — addition: pooling
To find the equal share, first pool everything into one pot:

100 + 150 + 80 + 120 + 50 = **500**

Why addition? Because the question said *"with the group's total unchanged"* — addition is
what computes a total. The pot now contains all the money with no memory of who brought what.
(Notice: information was destroyed here. Many different groups could produce the same pot of
500. This "forgetting" is why the mean alone can mislead — a thread we pull in later chapters.)

### Ingredient 2 — division: equal sharing
Now share the pot equally among the 5 friends. **Division IS equal sharing** — that is its
meaning. "500 ÷ 5" is the answer to: *"500 units split into 5 identical piles — how big is
each pile?"*

Why does dividing give the fair share? Because division is defined as the reverse of
multiplication: the fair share is the number **s** such that 5 piles of s rebuild the pot,
i.e.  5 × s = 500. The number that satisfies this is s = 100. Division is just the machine
that finds s. Check it in reverse — 5 × 100 = 500 ✓ — the total is unchanged, exactly as the
question demanded.

So: **mean = total ÷ count = 500 ÷ 5 = ₹100.**

Every mean you will ever compute — inside loss functions, gradient averaging, batch
normalization, attention weights — is exactly this: *pool, then share equally.*

## 3. Now, and only now: the notation

Mathematicians need to say "pool then share" for ANY list of numbers, not just our five
salaries. That requires naming things generally. Here is the standard formula, then every
symbol in it:

$$\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$$

| Symbol | Name | What it means, in our story |
|---|---|---|
| $x$ | the variable | the *kind* of thing measured (daily earnings) |
| $x_i$ | "x sub i" | the i-th person's number. $x_1$=100, $x_2$=150, … $x_5$=50. The subscript i is just a position label — a house number, not math |
| $n$ | the count | how many numbers there are (5) |
| $\sum$ | capital sigma, "sum" | a machine that means "add up". Nothing more |
| $i=1$ (below Σ) | start | begin adding at position 1 |
| $n$ (above Σ) | stop | stop after position n |
| $\sum_{i=1}^{n} x_i$ | the whole sum | "add $x_1 + x_2 + \dots + x_n$" — our pooling step, written compactly |
| $\frac{1}{n}$ | one n-th | the equal-sharing step. Multiplying by 1/n IS dividing by n — taking one share out of n equal shares |
| $\bar{x}$ | "x bar" | the answer; the bar over a variable is the standard costume for "mean of" |

Read the formula aloud, right to left, as a sentence:
*"Take each value ($x_i$), add them all up from the first to the n-th ($\sum_{i=1}^n$), then
split the total into n equal parts ($\frac{1}{n}$). Call the result x-bar."*

It is literally §2 in costume. If a formula ever feels alien, translate it back into the
story — every formula in this program has one.

### Why write $\frac{1}{n}\sum x_i$ instead of $\frac{\sum x_i}{n}$?
They are identical. The 1/n-in-front style survives because in bigger formulas (variance,
gradients, expectations) the "sharing factor" likes to sit out front where it can be seen
and manipulated. You'll meet both; never let the typography scare you.

## 4. On paper — do these now (no calculator, no computer)

**Easy**
1. Compute the mean of: 4, 8, 6, 2. Verify by the reverse-multiplication check (§2).
2. For that data, write out the formula with every symbol replaced by its actual number
   (i.e. expand the Σ fully).

**Medium**
3. Three friends have means of ₹90 over 4 days. A fourth friend joins with earnings that
   raise the group total by ₹200 over the same 4 days. What is the new mean *per person per
   day*? Think in pots, not formulas.
4. The mean of 6 numbers is 50. Five of them are 40, 45, 55, 60, 20. Find the sixth.
   (Hint: what must the pot contain?)

**Hard**
5. A store's mean daily sales over 30 days is ₹7,000. The owner realizes day 13 was recorded
   as ₹1,000 but was actually ₹10,000. Compute the corrected mean *without* re-adding 30
   numbers. Explain why your shortcut works, in pot language.
6. Prove, in words or algebra: if you subtract the mean from every value, the new values sum
   to exactly zero. (This is the "balance point" property — the mean is where the data
   see-saws level. It will return in variance, least squares, and gradient descent.)

## 5. Into the computer — your first from-scratch code of the program

Rules: pure Python. **Forbidden:** `sum()`, `len()`, `statistics`, `numpy` — you are building
these, so you may not call them. Build:

```
def mean(values):
    # your code: one loop, two running quantities.
    # Decide and justify: what should happen if values is empty?
```

Steps:
1. On the VM or laptop, create `code/stats/mean.py` with the function.
2. Test it yourself against your paper answers from §4 (a `if __name__ == "__main__":` block
   with a few checks is fine — real pytest arrives in Phase 3).
3. Commit (recipe applies) and push.

**Gate questions for the debrief** (answer without the book):
- Why does dividing the pot by n give the fair share? (reverse-multiplication argument)
- What does each of the five parts of $\frac{1}{n}\sum_{i=1}^{n}x_i$ do?
- What information does the mean destroy?
- Your empty-list decision — and why?

---
*Next: Chapter 2 — the mean's blind spot: spread, deviations, and why we square them
(variance & standard deviation, built the same way).*
