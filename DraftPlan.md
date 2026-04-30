# Learning Experience Plan (LEP)
## Lesson 1 of 8 — Game Deconstruction and Scratch Environment Setup

---

# PART ONE: Full Lesson Narrative (Human-Readable)

---

## Lesson Overview

**Learning Area:** Digital Technology
**Lesson Number:** 1 of 8
**Lesson Focus:** Game Deconstruction and Scratch Environment Setup
**Date:** 30/04/2026
**Term:** 2
**Time Slot:** Period 1 — 8:30 to 9:20 (50 minutes)
**Year Level:** Year 8

This is the opening lesson of an eight-lesson unit in which Year 8 students will design and develop an interactive digital game using Scratch (scratch.mit.edu). The unit employs a Scaffolded Guided Inquiry framework — specifically the "Base + Mod" strategy — in which all students first co-create a standardised Base Game under direct teacher instruction (Lessons 1–4), then independently extend it through tiered modification challenges (Lessons 5–8). Lesson 1 establishes every prerequisite for this journey: cognitive (what is the game?), technical (what is the tool?), and procedural (how do we manage our work?).

The lesson is structured around three logical segments that directly correspond to the Insights module directives: (1) Hook and Deconstruction (~10 min), (2) Workspace Initialisation (~30 min), and (3) Digital Asset Management (~10 min).

---

## Learning Outcomes

### SCSA Curriculum Alignment
This lesson addresses the following Year 8 SCSA Digital Technologies Content Descriptions:
- **WA8DIGDI1:** Design the user experience (UX) of a digital system.
- **WA8DIGDTID1:** Investigate a problem for a given need or opportunity.
- **WA8DIGDTPM1:** Plan, develop and communicate, using project management processes, considering time, resources and costs to achieve solutions.
- **WA8DIGDTDE1:** Design processes and solutions considering a range of technologies and techniques, using appropriate technical terms.

### Specific Learning Goals (WALT — We Are Learning To)
By the end of this lesson, students will be able to:
- Identify at least three independent components of a digital game (Bat sprite, Crystal sprite, Score variable) by applying the computational thinking strategy of Decomposition.
- Navigate the three primary zones of the Scratch interface — Stage, Sprite List, and Code Blocks Area — and locate the Events block category.
- Configure a new Scratch project by deleting the default Cat sprite, adding the Bat sprite and Blue Sky backdrop, and placing the [When Green Flag Clicked] event block in the script area.
- Apply digital asset management protocols by naming the project using the agreed class convention (FirstName's Game) and saving it to cloud storage or as a local .sb3 file.

### Success Criteria (WILF — What I am Looking For)
Students demonstrate success when they:
- Can name at least three separate, functionally distinct parts of the demo game.
- Have a correctly configured Scratch project with Bat sprite, Blue Sky backdrop, and the green flag block visible in the script area.
- Have a project named according to convention and saved via at least one method before the lesson ends.

---

## Assessment Plan

### Formative Assessment (Assessment FOR Learning)
No diagnostic or summative assessment is planned for this first lesson. All assessment is formative:
1. **Structured teacher observation** during the guided workspace setup phase: the teacher circulates and visually confirms each student has completed all four mandatory workspace actions (delete Cat, add Bat, add Blue Sky backdrop, place [When Green Flag Clicked] block).
2. **Oral group questioning** during the hook activity: the teacher poses decomposition questions to small groups, listening for computational vocabulary (sprite, variable, trigger, rule) to gauge prior conceptual connections.
3. **Backup Worksheet** (Assessment FOR Learning tool for fast finishers): students label the three Scratch interface zones on a printed diagram and write one sentence describing each zone's function. The teacher collects completed worksheets at the exit as a record of initial interface comprehension.

### What Will Be Monitored and How
- **What:** Whether students correctly identify at least three discrete game components (Bat, Crystal, Score) during the oral decomposition activity. → **How:** Targeted oral questioning in groups during the hook segment; teacher listens for computational vocabulary and notes any students unable to identify more than one component.
- **What:** Whether each student has located the Events drawer and placed the [When Green Flag Clicked] block correctly. → **How:** Physical circulation during Body Parts 2 and 3; teacher visually inspects each screen.
- **What:** Whether all students have named and saved their project. → **How:** Final visual scan of all screens during the conclusion; teacher verbally prompts any student whose project is unnamed or unsaved.

---

## Prior Knowledge

Students are expected to bring the following knowledge and skills to this lesson:
- **Basic ICT proficiency:** ability to log in to a school account, open and navigate a web browser to a specified URL, and operate a mouse or trackpad competently.
- **General file management awareness:** understanding that digital work must be saved to prevent data loss — analogous to saving a Word document; experience with the concept of file formats (.docx, .pdf) helps contextualise the .sb3 format.
- **Implicit event-driven logic from everyday life:** awareness that a button press or input triggers an action (e.g., pressing play starts a video) — this everyday intuition is the bridge to the [When Green Flag Clicked] concept.
- **Foundational familiarity with computer games as rule-based systems:** students understand that a game has components (characters, a goal, a score) even without prior coding experience — no prior Scratch or programming experience is assumed or required.

---

## Preparation and Resources

**Teacher preparation (prior to lesson):**
- Pre-registered Scratch accounts for each student, or a procedure for account creation with school email ready to distribute.
- Pre-prepared WALT/WILF slide to display at lesson start.
- Bookmarked link to the fully featured "Catch the Crystal" Scratch demo (with bomb and speed-up features) ready to open on the teacher display.
- Printed Backup Worksheets (one per student): single-sided A4 diagram of the Scratch interface with five arrows and blank boxes for zone name and one-sentence description.
- Whiteboard and markers cleared and ready.

**Physical and digital resources:**
- Student devices (school-issued laptops or tablets) with internet access and Chrome browser.
- Projector connected to teacher display device.
- Pre-prepared WALT/WILF slide displayed on the projector screen at lesson start.
- Teacher-prepared demo link: the fully featured "Catch the Crystal" Scratch project (including bomb and speed-up features) for display only.
- Scratch accounts (pre-registered with school email, or students register on arrival).
- Backup Worksheet: printed single-sided A4 sheet showing a labelled screenshot of the Scratch interface with five arrows and blank boxes for zone name and one-sentence description (one per student).
- Whiteboard and markers for recording decomposition components.

---

## Teaching Sequence

### INTRODUCTION (10 minutes)

#### Part 1 — Welcome, Roll and Goal Sharing (5 minutes)
The teacher greets students at the door and directs them to their assigned seats. While students settle, the teacher takes the roll quietly. Simultaneously, the pre-prepared WALT/WILF slide is displayed on the projector screen. The teacher reads the learning goals aloud, using student-friendly language:
- **WALT:** "We are learning to: break a digital game into its key parts, set up our Scratch workspace, and save our work correctly."
- **WILF:** "What I am looking for: you can name at least three separate parts of a game, find the right blocks in Scratch, and have your project saved and named by the end of today."

#### Part 2 — Hook: Demo Game and Oral Decomposition (5 minutes)
This segment is the conceptual engine of the entire lesson. The teacher opens the "Catch the Crystal" demo link on the projector in full-screen mode and plays the complete game — including bomb drops and speed-up mechanic — for approximately 60 seconds without verbal commentary. Students are allowed to react naturally; the spectacle of the finished product is the hook.

Once initial reactions subside, the teacher initiates a structured oral decomposition activity, posing the following focus questions to the class in groups (not to individuals), applying wait time after each question:
- "Look at everything that is moving on screen. Can you name the separate, independent things you can see?"
- "What is the rule that makes you score a point? What has to happen for that rule to fire?"
- "If you had to build this game from absolutely nothing, what would be the very first piece you would create?"

As students respond, the teacher records their suggestions on the whiteboard in three labelled columns, progressively narrowing the discussion through guided questioning until the class reaches agreement on the three Base Game components: **Bat** (player-controlled sprite), **Crystal** (falling sprite), **Score** (variable/counter). The teacher then explicitly sets the lesson's scope: "Today, we are only building these three pieces. Everything else you saw — the bomb, the speed-up — those are challenges we will choose from later. For now, simple and solid."

This activity operationalises the computational thinking strategy of **Decomposition** — the ability to observe a complex digital system and strip away non-essential features to identify the core functional architecture — which is the primary learning intention for this lesson.

---

### BODY (30 minutes)

#### Part 1 — Instructional Input: Scratch Interface Orientation (5 minutes)
Following the hook, the teacher directs students to open Chrome and navigate to scratch.mit.edu and log in (or create an account). The Scratch interface is displayed on the projector. Using a physical pointer, the teacher identifies and names the three primary zones:

1. **The Stage** — "The screen your player will watch. This is where your finished game actually runs."
2. **The Sprite List** — "Your cast of characters. Every moving thing in your game — the Bat, the Crystal — lives here as a 'sprite'."
3. **The Code Blocks Area** — "Your instruction toolbox. You build your game's brain by dragging and snapping coloured blocks together here."

The zone definitions are deliberately student-friendly (Register B), prioritising comprehension over technical precision at this initial exposure. EAL/D and visual learner support is provided by using the projector pointer to physically highlight each zone as it is named. The teacher strictly respects the lesson's content boundary: no mention is made of X/Y coordinates, loops, or any block categories beyond the Events drawer.

#### Part 2 — Guided Practice: Workspace Configuration — Mandatory Steps 1 to 3 (10 minutes)
This is the core hands-on phase of the lesson. The teacher employs explicit instruction with an "I do → We do" Gradual Release of Responsibility pattern: each step is demonstrated on the projector first, then students replicate it on their own device. Steps are issued one at a time to manage cognitive load and prevent students from racing ahead.

**Step 1 — Delete the default Cat sprite:**
Teacher demonstrates, then instructs: "Right-click directly on the Cat icon in the Sprite List at the bottom right of your screen. A small menu will appear. Select 'Delete'. Your stage should now be completely empty." The teacher circulates to confirm all students have an empty stage before proceeding.

**Step 2 — Add the Bat sprite:**
Teacher demonstrates, then instructs: "See the blue circle with a small cat face at the bottom right of the Sprite List? Click it. In the library that opens, type 'Bat' into the search box. Click the Bat thumbnail to add it. You should see a Bat appear on your Stage." The teacher circulates to confirm Bat is visible.

**Step 3 — Add the Blue Sky backdrop:**
Teacher demonstrates, then instructs: "Look at the very bottom right of the screen — there is a small landscape icon next to the word 'Stage'. Click it. In the backdrop library, search for 'Blue Sky' and click it. Your stage background should now be blue." The teacher circulates to confirm the backdrop is applied.

Common errors intercepted during circulation: students adding a backdrop via the "Paint" option (redirect to the library search tab); students unable to find Bat (confirm correct spelling); students accidentally deleting the wrong element (undo with Ctrl+Z). If a student's device fails to load Scratch, the teacher pairs them temporarily with a neighbour rather than halting the entire class.

#### Part 3 — Icebreaker Coding: Event Trigger and [When Green Flag Clicked] (7 minutes)
With the workspace configured, the teacher draws the class's attention back to the projector for a brief instructional input on the concept of event-driven programming, framed in accessible terms:
"Every program needs an on-switch — something that says: start right now. Without it, your code just sits there and nothing ever happens. In Scratch, that on-switch is a special block called [When Green Flag Clicked]. It lives in the yellow Events drawer."

The teacher demonstrates on the projector: clicking the yellow Events category in the Code Blocks Area, then dragging the [When Green Flag Clicked] block onto the empty script area. Students are then asked to mirror this action independently: "Find the yellow Events category — it is the one that looks like a lightning bolt. Drag the [When Green Flag Clicked] block out onto your blank script area. That block is your game's ignition switch."

The teacher circulates to confirm all students have the block placed. A firm scope boundary is explicitly communicated to prevent premature experimentation: the block has no code beneath it yet, and this is correct. Students should not add further blocks today. For fast finishers who reach this point early, a verbal extension prompt is offered: "Look at the other colours in the Code Blocks Area. Can you figure out what category each colour might belong to just from its colour?" This extends thinking without breaching the lesson's code boundary.

#### Part 4 — Independent Consolidation and Backup Worksheet (8 minutes)
Students who have successfully completed all four mandatory workspace actions receive the Backup Worksheet. The teacher reads the task instructions aloud: "On your worksheet you will see a Scratch screenshot with five arrows pointing to different areas. For each arrow: write the name of that area, and write one sentence explaining what it does. Here is an example — arrow number one points to the Stage. You would write: Stage — the area where the game runs and is displayed to the player. Use that same format for all five."

During this phase, the teacher circulates to provide direct 1:1 support to students still completing the setup steps. Cooperative learning is permitted: students who have completed the worksheet may offer quiet verbal assistance to a neighbour who is still setting up, but may not touch the neighbour's keyboard. Students who complete the worksheet rapidly may explore the remaining block categories visually (without dragging blocks), predicting what each colour represents — this foreshadows later content without exposing it.

---

### CONCLUSION (10 minutes)

#### Part 1 — Digital Asset Management: Naming and Saving (5 minutes)
The teacher signals the class to pause their Scratch work and direct attention to the projector. The teacher demonstrates the naming convention: "Click the project title at the very top of the screen — it currently says 'Untitled'. Replace it with your first name followed by the word 'Game'. For example: Alex's Game."

The teacher then demonstrates both saving methods:
- **Method 1 (cloud):** "Click 'File' in the top menu bar, then click 'Save now'. Scratch will save your project to your account online."
- **Method 2 (local backup):** "Click 'File' again, then 'Save to your computer'. This downloads a .sb3 file to your Downloads folder. Keep this as your backup."

The teacher conducts a final visual scan of all student screens to confirm every project is named and saved. This constitutes the lesson's exit requirement: no student is dismissed until their project is named and saved.

#### Part 2 — Lesson Recap and Vocabulary Review (5 minutes)
The teacher poses three brief recap questions to small groups, using wait time (not to individuals):
- "We broke the game into parts today. What is the name for that thinking skill?"
- "What are the three zones of the Scratch screen? Can your group name all three?"
- "What is the very first block that every Scratch program must begin with?"

The teacher briefly acknowledges the class's progress: the three components identified today — Bat, Crystal, Score — are the exact building blocks that the next lesson will begin to activate. Students are dismissed in an orderly manner once all screens show a named, saved project. Students who completed the Backup Worksheet place it on the teacher's desk as they leave.

---

# PART TWO: Key Name to Content Mapping

The following section maps each JSON key name (x01–x61) to its corresponding content for this lesson plan.

| Key | Field Description | Content |
|---|---|---|
| x01 | Learning Area | Digital Technology |
| x02 | Lesson Number | 1 |
| x03 | Lesson Focus | Game Deconstruction and Scratch Environment Setup |
| x04 | Date | 30/04/2026 |
| x05 | Term | 2 |
| x06 | Time Period | Period 1 - 8:30 to 9:20 |
| x07 | Year Level | Year 8 |
| x08 | Learning Area Outcomes (SCSA Codes) | WA8DIGDI1: Design the UX of a digital system. WA8DIGDTID1: Investigate a problem for a given need or opportunity. WA8DIGDTPM1: Project management processes. WA8DIGDTDE1: Design with appropriate technical terms. |
| x09 | Specific Learning Goals (array) | [Identify three Base Game components via Decomposition; Navigate three Scratch zones; Configure workspace with Bat/Blue Sky/green flag block; Apply naming and saving conventions] |
| x10 | Diagnostic Assessment Type | (empty — no diagnostic assessment this lesson) |
| x11 | Diagnostic Assessment Type (duplicate label) | (empty) |
| x12 | Diagnostic Assessment Methods | (empty) |
| x13 | Formative Assessment Type | Formative |
| x14 | Formative Assessment Type (duplicate label) | Formative |
| x15 | Formative Assessment Methods (array) | [Structured teacher observation of workspace completion; Oral group questioning during hook; Backup Worksheet labelling task for fast finishers] |
| x16 | Summative Assessment Type | (empty — no summative assessment this lesson) |
| x17 | Summative Assessment Type (duplicate label) | (empty) |
| x18 | Summative Assessment Methods | (empty) |
| x19 | What to Monitor (array) | [Correct identification of Bat/Crystal/Score during oral decomposition; Events drawer located and green flag block placed; Project named and saved before lesson end] |
| x20 | How to Monitor (array) | [Oral group questioning during hook; Physical screen circulation during Body Parts 2 and 3; Final visual scan during conclusion] |
| x21 | Students' Prior Knowledge (array) | [Basic ICT/browser proficiency; File management awareness; Implicit event-driven logic from everyday experience; General game-as-rule-system familiarity; No prior Scratch experience assumed] |
| x22 | Preparation and Resources (array) | [Student devices with internet; Projector; WALT/WILF slide; Demo game link; Scratch accounts; Backup Worksheets; Whiteboard and markers] |
| x23 | Introduction Part 1 — Time | 5min |
| x24 | Introduction Part 1 — Actions (array) | [Greet at door; Take roll while displaying WALT/WILF slide; Read WALT aloud; Read WILF aloud] |
| x25 | Introduction Part 1 — Notes | Keep roll quiet and efficient. |
| x26 | Introduction Part 2 — Time | 5min |
| x27 | Introduction Part 2 — Strategy | Display demo game full-screen; guided oral decomposition with three focus questions; record Bat/Crystal/Score on whiteboard; set scope boundary. |
| x28 | Introduction Part 2 — Focus Questions | Three hook decomposition questions (What moves independently? What triggers scoring? What is the first element to build?) |
| x29 | Introduction Part 3 — Time | (empty) |
| x30 | Introduction Part 3 — Strategy | (empty) |
| x31 | Introduction Part 3 — Notes | (empty) |
| x32 | Body Part 1 — Time | 5min |
| x33 | Body Part 1 — Strategy | Students open Scratch; teacher labels three zones on projector with student-friendly definitions (Stage = game screen; Sprite List = cast of characters; Code Blocks Area = toolbox). |
| x34 | Body Part 1 — Notes | EAL/D support via projector pointer. Strict content boundary: no coordinates or loops introduced. |
| x35 | Body Part 2 — Time | 10min |
| x36 | Body Part 2 — Strategy | Explicit I-do/We-do: Step 1 delete Cat; Step 2 add Bat; Step 3 add Blue Sky backdrop. One step at a time; teacher circulates after each. |
| x37 | Body Part 2 — Notes | Common errors and corrections listed. Device failure contingency: pair with neighbour. |
| x38 | Body Part 3 — Time | 7min |
| x39 | Body Part 3 — Strategy | Concept: event trigger as on-switch. Teacher demos Events drawer + green flag block; students replicate independently. Teacher circulates to confirm. |
| x40 | Body Part 3 — Notes | Scope boundary: no further blocks today. Extension verbal prompt for fast finishers. |
| x41 | Body Part 4 — Time | 8min |
| x42 | Body Part 4 — Strategy | Distribute Backup Worksheet to students who have completed setup. Read task instructions aloud. Teacher circulates to support lagging students. Cooperative help permitted (verbal only). |
| x43 | Body Part 4 — Notes | Differentiation: 1:1 support for lagging students; visual exploration extension for fast finishers. |
| x44–x52 | Body Parts 5–7 | (empty — not used in this lesson) |
| x53 | Conclusion Part 1 — Time | 5min |
| x54 | Conclusion Part 1 — Actions (array) | [Signal class to pause; Demo project naming; Demo cloud save; Demo local .sb3 save; Final visual scan] |
| x55 | Conclusion Part 1 — Notes | Exit requirement: all students must have a named, saved project before dismissal. Worksheets collected at door. |
| x56 | Conclusion Part 2 — Time | 5min |
| x57 | Conclusion Part 2 — Strategy | Three group recap questions (Decomposition term; three zone names; first block name). Acknowledge progress; orderly dismissal. |
| x58 | Conclusion Part 2 — Notes | Assessment FOR Learning: oral responses gauge retention of core vocabulary for Lesson 2 planning. |
| x59 | Conclusion Part 3 — Time | (empty) |
| x60 | Conclusion Part 3 — Strategy | (empty) |
| x61 | Conclusion Part 3 — Notes | (empty) |
