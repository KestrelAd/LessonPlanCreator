# SCSA Connection Document
## Lesson 1 of 8 — Game Deconstruction and Scratch Environment Setup
**Target Year Level:** Year 8 | **Curriculum Framework:** SCSA Digital Technologies

---

## 1. Overview of the Mapping Process

This document records the alignment between the core user insights (Insights/Insights.md) and the relevant SCSA Year 8 Digital Technologies Content Descriptions and Achievement Standards. The purpose of Lesson 1 is to introduce students to the Scratch programming environment by first deconstructing a finished, complex digital game demo into its constituent parts, then configuring a personal workspace and establishing a digital project management habit. The central computational thinking concept is **Decomposition** — the deliberate strategy of breaking a complex digital system into smaller, discrete, manageable components.

---

## 2. Primary SCSA Alignments

### 2.1 WA8DIGDI1 — Design the user experience (UX) of a digital system
**SCSA Description:** Design the user experience (UX) of a digital system.

**Connection to Lesson 1 Insights:**
The hook activity at the beginning of Lesson 1 asks students to observe the fully featured "Catch the Crystal" demo game and perform oral reverse engineering — identifying what the player sees, what actions they can take, what triggers score changes, and what rules govern the game loop. This is precisely the kind of UX analysis that WA8DIGDI1 refers to: students are not designing yet, but they are performing the foundational cognitive act that precedes all UX design — decomposing an existing digital experience into its functional sub-systems. The oral decomposition exercise ("What are the separate moving things on screen?", "What must happen for the score to increase?") directly operationalises UX investigation at an age-appropriate level. By the end of the hook, students have identified three distinct UX components: the player-controlled sprite (Bat), the environmental falling object (Crystal), and the score feedback mechanism (Score variable). This maps squarely onto the UX decomposition skill required by WA8DIGDI1.

**Strength of alignment:** Very high — the activity is explicitly structured around analysing a UX system.

---

### 2.2 WA8DIGDTID1 — Investigate a problem for a given need or opportunity
**SCSA Description:** Investigate a problem for a given need or opportunity.

**Connection to Lesson 1 Insights:**
The "reverse engineering" and decomposition task constitutes an investigation. Students are presented with a design problem framed as a need: "We need to build this game." By watching the demo and identifying which elements are core (Bat, Crystal, Score) versus extended (bomb, speed-up), students are effectively scoping the problem space and distinguishing between essential requirements and optional enhancements. This mirrors the formal process of investigating and defining a design brief — the students are identifying what is needed before any implementation begins. The Insights explicitly frame Lesson 1 as the conceptual foundation for the entire eight-lesson project: without a clear understanding of what the base game requires, students cannot meaningfully engage with the later implementation lessons.

**Strength of alignment:** High — the lesson frames a real design investigation, even if the brief is teacher-specified rather than student-generated (appropriate for Year 8 early exposure).

---

### 2.3 WA8DIGDTPM1 — Plan, develop and communicate, using project management processes, considering time, resources and costs to achieve solutions
**SCSA Description:** Plan, develop and communicate, using project management processes, considering time, resources and costs to achieve solutions.

**Connection to Lesson 1 Insights:**
The final segment of Lesson 1 (Digital Asset Management) is directly sourced from the Insights Module C and addresses project management at the level of digital workflow hygiene. Students are required to: (a) name their Scratch project according to an agreed convention (FirstName's Game), (b) save to the cloud via Scratch's "Save now" function, and (c) download a local .sb3 backup. These three actions establish the file management discipline that will be critical across all eight lessons — students who fail to save correctly in Lesson 1 risk losing all subsequent work. This aligns with WA8DIGDTPM1 in that students are learning to manage a digital project resource (their Scratch file) with explicit consideration of data preservation and workflow continuity — core components of professional project management practice.

**Strength of alignment:** High — the connection is direct and practical; this is not a superficial alignment.

---

### 2.4 WA8DIGDTDE1 — Design processes and solutions considering a range of technologies and techniques, using appropriate technical terms
**SCSA Description:** Design processes and solutions considering a range of technologies and techniques, using appropriate technical terms.

**Connection to Lesson 1 Insights:**
The Scratch interface orientation activity (Body Part 1) introduces students to the formal technical vocabulary of the Scratch environment: Stage, Sprite List, Code Blocks Area, Events, and the [When Green Flag Clicked] trigger block. Learning to name these components accurately and use them correctly is the foundational prerequisite for all subsequent design and implementation work. The Insights' Module F explicitly mandates that "standard computational thinking terminology" must be used throughout — terms like "infinite loop," "event trigger," and "iteration" appear in later lessons, and Lesson 1 builds the vocabulary infrastructure. The icebreaker coding activity (dragging the [When Green Flag Clicked] block) further introduces the concept of event-driven programming as a design technique with a specific technical name. This aligns with WA8DIGDTDE1's requirement to work with technologies and techniques using appropriate technical terms.

**Strength of alignment:** High — the terminology-building component of this lesson is deliberately structured and aligns with what the curriculum describes.

---

## 3. Secondary SCSA Alignments (Supporting Context)

### 3.1 WA8DIGDTID2 — Develop a design brief for a given need or opportunity
**Partial alignment:** Although students do not write a design brief in Lesson 1, the decomposition activity implicitly begins to populate the conceptual requirements that a design brief would contain. Students who correctly identify the Base Game components (Bat + Crystal + Score) are, in cognitive terms, defining the minimum viable product specification. This lays the groundwork for the formal design constraint and modding decision that students will face in Lessons 5–8.

### 3.2 General Capability — Digital Literacy
The entire Lesson 1 is foundational digital literacy development: students learn to navigate a new digital tool (Scratch), adopt file management conventions, and begin to understand a block-based programming paradigm. These are core digital literacy competencies articulated in the SCSA General Capabilities framework and are implicitly developed throughout all activities.

### 3.3 General Capability — Critical and Creative Thinking
The oral decomposition activity ("If you could only keep one element, which one could the game not exist without?") directly exercises critical thinking by asking students to evaluate the necessity and interdependence of system components — a higher-order cognitive skill well above simple recall.

---

## 4. Summary Correspondence Table

| SCSA Code | Description | Lesson 1 Activity | Alignment Strength |
|---|---|---|---|
| WA8DIGDI1 | Design the UX of a digital system | Oral decomposition of the demo game into Bat / Crystal / Score | Very High |
| WA8DIGDTID1 | Investigate a problem for a given opportunity | Identifying base game requirements from the demo | High |
| WA8DIGDTPM1 | Project management processes | Project naming convention and dual save (cloud + local) | High |
| WA8DIGDTDE1 | Design with appropriate technical terms | Scratch interface vocabulary; [When Green Flag Clicked] | High |
| WA8DIGDTID2 | Develop a design brief | Implicit: identification of minimum viable product components | Partial / Supporting |
| Digital Literacy (GC) | Digital literacy capability | Full Scratch environment setup; file management workflow | Supporting |
| Critical & Creative Thinking (GC) | Critical evaluation skills | Hook questions requiring component necessity reasoning | Supporting |

---

## 5. Pedagogical Rationale for the Mapping

The selection of these SCSA codes reflects the Insights' explicit pedagogical philosophy: Lesson 1 operates in the **Teacher-Led / Explicit Teaching** phase (Lessons 1–4), which means the curriculum connections must be grounded in teacher-directed investigation and vocabulary building rather than student-generated design. The SCSA codes chosen (WA8DIGDI1, WA8DIGDTID1, WA8DIGDTPM1, WA8DIGDTDE1) all involve structured analysis, investigation, and process application — skills that benefit from explicit modelling and guided practice. They are not the more open-ended design and evaluation codes (WA8DIGDTEV1, WA8DIGDTDE1 in its fullest sense) that will become relevant in Lessons 5–8 when students enter the Student-Centred / Maker Workshop phase.

This alignment ensures that Lesson 1's activities are curriculum-authentic without overreaching into skills that students have not yet had the scaffolding to develop.
