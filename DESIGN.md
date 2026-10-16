---
name: UniGrade Campus Index
description: An academic index that makes grade targets and the next useful action clear.
colors:
  chalk: "#f3f4ef"
  paper: "#fcfcf8"
  paper-hover: "#eff4f0"
  rule: "#cddbd3"
  ink: "#102f2f"
  ink-secondary: "#385a56"
  ink-muted: "#496b65"
  rail: "#103538"
  goal: "#103e42"
  teal: "#116b67"
  teal-hover: "#0d514f"
  teal-tint: "#dceee8"
  mint-action: "#d5f3df"
  deadline: "#925517"
  deadline-tint: "#fff0cf"
  danger: "#a73730"
  danger-tint: "#fae9e4"
  focus: "#d39927"
typography:
  display:
    fontFamily: "DM Mono, monospace"
    fontSize: "clamp(66px, 7vw, 104px)"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-6px"
  headline:
    fontFamily: "Prompt, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    fontSize: "clamp(30px, 3vw, 42px)"
    fontWeight: 800
    lineHeight: 1.25
    letterSpacing: "-1.5px"
  title:
    fontFamily: "Prompt, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    fontSize: "19px"
    fontWeight: 700
    lineHeight: 1.3
  body:
    fontFamily: "Prompt, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    fontSize: "14px"
    fontWeight: 400
  label:
    fontFamily: "DM Mono, monospace"
    fontSize: "12px"
    fontWeight: 700
rounded:
  sm: "6px"
  md: "8px"
  lg: "9px"
  xl: "12px"
spacing:
  xs: "8px"
  sm: "12px"
  md: "16px"
  lg: "24px"
  xl: "38px"
components:
  button-primary:
    backgroundColor: "{colors.teal}"
    textColor: "{colors.paper}"
    rounded: "7px"
    padding: "12px 17px"
  button-primary-hover:
    backgroundColor: "{colors.teal-hover}"
  button-goal:
    backgroundColor: "{colors.mint-action}"
    textColor: "{colors.goal}"
    rounded: "7px"
    padding: "10px 15px"
  card:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
  nav-active:
    backgroundColor: "{colors.teal}"
    textColor: "{colors.paper}"
    rounded: "5px"
---

# Design System: UniGrade Campus Index

## Overview

**Creative North Star: "Campus Index"**

UniGrade reads like a concise academic record. A stable dark rail and pale work surface frame the student's grade target; numbered rows and thin rules make courses easy to scan. Thai Prompt carries explanations and actions, while DM Mono distinguishes quantities, codes, and GPA figures.

**Key Characteristics:**
- The goal is the strongest visual panel; course and deadline information follows in indexed rows.
- Flat, lightly ruled surfaces keep a dense workspace legible.
- Teal marks actions and active location; warm color marks deadlines and attention.

## Colors

Deep blue-green gives navigation and the goal panel a stable frame. Chalk and paper separate the workspace from its panels.

### Primary
- **Campus Teal:** Active navigation, links, primary actions, and focus within fields.
- **Goal Blue-Green:** The prominent grade target panel; pale mint keeps its action distinct.

### Neutral
- **Chalk:** Page ground.
- **Paper:** Cards, top bar, and modal surfaces.
- **Academic Ink:** Main Thai text; secondary and muted ink carry supporting facts.
- **Rule Green:** Borders and row dividers.

### Supporting
- **Deadline Ochre:** Upcoming dates and time-sensitive information, paired with its light tint when a surface is needed.
- **Danger Red:** Destructive and error states, paired with its light tint.
- **Focus Gold:** The visible keyboard focus outline.

**The Sparse Signal Rule.** Reserve warm color for attention and status; ordinary progress and navigation use teal.

## Typography

**Display Font:** DM Mono (monospace fallback).  
**Body Font:** Prompt (system sans-serif fallback).

Prompt supports Thai reading at compact dashboard sizes. DM Mono gives GPA, scores, course numbers, and compact labels consistent digit widths.

### Hierarchy
- **Display:** Heavy monospaced goal GPA; the hero number scales with viewport width.
- **Headline:** Bold Prompt page title with tight tracking.
- **Title:** Bold Prompt section headings above ruled content.
- **Body:** Prompt at the base size for descriptions and course names.
- **Label:** Bold DM Mono for numerical indexes, data labels, and counters.

**The Measured Number Rule.** Use DM Mono for comparable figures and indexes, then return to Prompt for Thai names and explanatory copy.

## Layout

On desktop, a fixed 246px navigation rail sits beside a content area capped at 1350px with 38px side padding. The dashboard opens with a full-width goal panel, then a wider course index and narrower deadline panel. A 16px grid gap keeps the sections distinct. At 900px the rail becomes a bottom dock; at 650px the dashboard becomes one column, the goal metrics stack below the target, and the course score detail is omitted. Content padding reduces to 16px on small screens, with bottom space for the dock and safe area.

## Elevation & Depth

Campus Index is flat by default. Solid surfaces, thin borders, background tone, and the dark goal panel create hierarchy. Dashboard cards have no resting shadow. Legacy controls still use subtle hover or inset shadows where they communicate interaction; they are not a page-wide depth system.

**The Ruled Surface Rule.** Prefer a border or divider over a raised card when grouping academic information.

## Shapes

Panels are restrained rectangles with gently curved corners. The final token scale runs from 6px to 12px; dashboard panels use 9px, the top bar 8px, and the rail's active item 5px. Thin rules organize lists. Round grade chips and profile imagery remain small exceptions for compact status and identity.

## Components

### Buttons
- **Primary:** Solid teal, white text, 7px corners; hover darkens to the deeper teal.
- **Goal action:** Pale mint within the dark goal panel, with dark text and a light green border; hover turns white.
- **Outline:** Paper surface and a thin border; selected grade targets become teal.
- **Focus:** A 3px gold `:focus-visible` outline with 3px offset applies across controls.

### Cards and index rows
- **Panels:** Paper with a 1px rule border and 9px corners; dashboard panels have no shadow.
- **Course rows:** Number at left, Thai course name and credits in the middle, score and grade at right, plus an action arrow. Thin dividers and a pale hover fill carry the interaction.
- **Deadline rows:** Date in ochre, detail beside it, and the same thin dividers.
- **Target course cards:** Course and desired grade lead; a progress bar and numeric progress follow when a score target exists.

### Inputs
- **Score fields:** Bordered paper, DM Mono numerals, centered values, and an accent border/tint on focus.
- **Modal fields:** Bordered paper with restrained corners and an accent border on focus.

### Navigation

The desktop rail is deep blue-green with pale labels and icons. The active destination is a solid teal rectangle. At 900px and below, the same destinations form a fixed bottom dock with icons above compact labels.

## Do's and Don'ts

### Do:
- **Do** lead planning views with the target GPA and the remaining requirement.
- **Do** use thin rules, numbered rows, and tabular figures for comparable academic data.
- **Do** preserve Thai readability and the visible gold keyboard focus treatment.

### Don't:
- **Don't** turn every panel into a floating or glass surface.
- **Don't** use warm attention colors for ordinary navigation.
- **Don't** hide the primary planning action behind secondary statistics.
