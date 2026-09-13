# Public Reader Experience Standard

This document defines how the public research experience should remain clear as the repository grows.

The goal is simple: **a reader should always know what question a page is answering, how deep they are in the research, and where to go next.**

## Core principle

The repository should reveal complexity gradually.

A first time reader should not encounter the complete theorem record before understanding the scientific question. A technical reader should still be able to reach every proof, equation, implementation, test, figure, and provenance record without searching folders.

## The six public layers

### Layer 1: README

Purpose: create curiosity and explain why the project exists.

The README should contain:

- the central research question;
- a short explanation in ordinary language;
- the main scientific reason the question matters;
- a compact description of what the project has built;
- clear paths to deeper material;
- the main scientific boundary.

The README should not contain:

- proposition by proposition summaries;
- long equations;
- exhaustive result tables;
- complete theorem histories;
- detailed proof certificates;
- large stacks of figures.

### Layer 2: Start Here

Purpose: explain the research logic in plain language.

This page should answer:

- what is the physical side of the problem;
- why the target must be independent;
- why measurement matters;
- why a model must be able to fail;
- why uncertainty must be included.

A reader should be able to finish this layer without mathematical preparation.

### Layer 3: Research Map

Purpose: show how the major scientific questions connect.

This page should organize the research by question rather than proposition number.

It may name the current theorem frontier, but it should not reproduce the full technical certificate.

### Layer 4: Formal architecture and theorem roadmap

Purpose: introduce definitions, equations, assumptions, and mathematical dependency.

Technical detail is appropriate here, but each section should still begin with the scientific question before presenting the formal object.

### Layer 5: Individual proposition pages

Purpose: provide the complete theorem level record.

A mature proposition page should make it easy to find:

- the question;
- assumptions;
- formal statement;
- proof;
- implementation when applicable;
- tests;
- figure when applicable;
- provenance;
- scientific boundary;
- dependencies and follow on results.

### Layer 6: Provenance, code, tests, and reproduction

Purpose: make technical claims auditable.

This layer may be dense because the reader has deliberately chosen to inspect the complete record.

## Page design rule

Every reader facing page should have one primary job.

If a page is trying to introduce the idea, explain the entire theorem history, show every figure, document the code, and provide citations at the same time, it is doing too much.

Move secondary material one layer deeper and link to it clearly.

## Writing rule

Public prose should be direct, natural, and readable.

Use short paragraphs, descriptive headings, ordinary punctuation, and concrete questions.

Do not use en dash or em dash punctuation. Avoid dash style compound prose on public website pages. Prefer commas, colons, parentheses, or separate sentences.

Technical notation can remain exact inside equations, source names, file paths, and code.

## Curiosity rule

A page should answer enough to reward the reader while leaving a clear next question.

Good transitions include:

- What physical system are we actually describing?
- Could the chosen description leave something important out?
- Is the target independent of the physical descriptor?
- Can the model fail?
- Does the conclusion survive uncertainty?
- What remains open?

The reader should feel invited to continue, not required to digest everything at once.

## Scientific boundary rule

Interesting presentation must not become stronger scientific wording.

The public pages must preserve these distinctions:

- a physical subsystem is not automatically a conscious subject;
- a latent variable is not automatically consciousness;
- rejection of one model does not prove the correct alternative;
- failure of one physical descriptor does not prove that no physical descriptor could be sufficient;
- operational quantum completeness does not automatically supply an experiential bridge;
- mathematical validity under assumptions does not establish those assumptions in nature;
- the final bridge from physical description to experience remains open.

## Navigation rule

Every layer should offer a clear route one level up and one level down.

A reader should never need to browse the repository tree to discover the intended next step.

The preferred public path is:

**README → Start Here → Research Map → Formal Architecture → Theorem Roadmap → Proposition → Provenance and Reproduction**

Alternative paths for visual readers, physicists, mathematicians, consciousness researchers, and software auditors should branch from the Research Map or Research Navigation page.

## Growth rule

New results should grow the technical record first.

The README, Start Here, and Research Map should change only when a new result materially changes the scientific story, current frontier, or major branch structure.

A new proposition number alone is not a reason to add another paragraph to the homepage.

## Repository promise

The repository should be rigorous enough for technical audit and readable enough that an interested person can understand why the research matters before deciding how deeply to enter the mathematics.
