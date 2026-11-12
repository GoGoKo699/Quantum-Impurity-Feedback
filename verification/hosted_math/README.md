# Checking the hosted mathematics

These scripts compare mathematical expressions in an exact Git revision with their actual rendering on GitHub. The check includes inline formulas, displays and table cells at widths of 1440 and 760 pixels. A local MathJax compilation supplies expected mathematical structure; the observed side comes from a fresh Chromium visit to each public, commit-pinned GitHub page.

The repository's read-only CI workflow runs on same-repository pull requests. It checks out the exact proposed head without persisted credentials, probes the overview first, and then captures every tracked Markdown page. Dependencies are Playwright 1.56.1 and MathJax 3.2.1. The job uses no additional secret or write permission.

## Run locally

Use Node.js 18 or later, Python 3.10 or later, Git, and a permitted Chromium runtime. Install the browser dependencies in a temporary directory outside this source tree. With `NODE_PATH` pointing to that directory's `node_modules`, run:

```bash
node verification/hosted_math/probe_hosted_math.cjs \
  --root /absolute/checkout --repository GoGoKo699/Quantum-Impurity-Feedback \
  --revision FULL_COMMIT_SHA --page README.md \
  --output /absolute/new-empty-probe-directory

node verification/hosted_math/capture_hosted_math.cjs \
  --root /absolute/checkout --repository GoGoKo699/Quantum-Impurity-Feedback \
  --revision FULL_COMMIT_SHA \
  --output /absolute/new-empty-capture-directory
```

Replace the placeholder paths and revision with actual values. The collector reads committed Git objects, not uncommitted working files. It saves the source inventory, expected structure, actual rendered MathML, HTML, screenshots and comparison reports. Each attempt requires a new empty output directory. The representative probe alone is not a complete review.

## Interpret the evidence

The automated comparison checks source identity, page and expression counts, symbols, structural relationships, labels, renderer errors and specified geometry conditions. Inspect the screenshots for readability and compare important equations with the source; a passing automated report does not establish visual quality or scientific correctness.

A failed capture can reflect a source-formatting defect, a transient network failure, missing runtime capability or an access restriction. Preserve the actual failure and address its cause. No access setting is changed by these scripts. Exact-source interrupted captures may be resumed through the collector's documented `--resume-from` option when their artifact, runtime and freshness checks pass.

CI artifacts are retained for 14 days. Their retention is a convenience for inspection, not permanent archival storage. Scientific reproduction commands and the distinct scopes of the numerical checks are in the [main verification guide](../README.md).
