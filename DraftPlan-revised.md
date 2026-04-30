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
**Time Slot:** Period 1 — 8:30 to 9:30 (60 minutes)
**Year Level:** Year 8

This is the opening lesson of an eight-lesson unit in which Year 8 students will design and develop an interactive digital game using Scratch (scratch.mit.edu). The unit employs a Scaffolded Guided Inquiry framework — specifically the "Base + Mod" strategy — in which all students first co-create a standardised Base Game under direct teacher instruction (Lessons 1–4), then independently extend it through tiered modification challenges (Lessons 5–8). This lesson is grounded in **constructivist theory**: students actively construct understanding by observing a complex digital artefact, identifying its components through guided questioning, and building new technical vocabulary onto their prior experience of games and digital tools. Lesson 1 establishes every prerequisite for this journey: cognitive (what is the game?), technical (what is the tool?), and procedural (how do we manage our work?).

The lesson is structured in alignment with the **Madeline Hunter Instructional Model** across eight explicit steps — Anticipatory Set, Objective and Purpose, Input, Modeling, Checking for Understanding, Guided Practice, Independent Practice, and Closure — mapped onto a three-part Introduction, Body, and Conclusion framework.

---

## Intended Learning Outcomes / Objectives

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

## Students' Prior Knowledge

Students are expected to bring the following knowledge and skills to this lesson:
- **Basic ICT proficiency:** ability to log in to a school account, open and navigate a web browser to a specified URL, and operate a mouse or trackpad competently.
- **General file management awareness:** understanding that digital work must be saved to prevent data loss — analogous to saving a Word document; experience with the concept of file formats (.docx, .pdf) helps contextualise the .sb3 format.
- **Implicit event-driven logic from everyday life:** awareness that a button press or input triggers an action (e.g., pressing play starts a video) — this everyday intuition is the bridge to the [When Green Flag Clicked] concept.
- **Foundational familiarity with computer games as rule-based systems:** students understand that a game has components (characters, a goal, a score) even without prior coding experience — no prior Scratch or programming experience is assumed or required.

---

## Materials / Resources Required

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

## Learning Experiences and Timing

### INTRODUCTION (10 minutes)

#### **Anticipatory Set** — Part 1 (5 minutes)
The teacher opens the "Catch the Crystal" demo link on the projector in full-screen mode before students enter, allowing the game to play silently as the class settles. This spectacle of the finished product — including the bomb drops and speed-up mechanics — serves as the Anticipatory Set, connecting students' prior experience of playing digital games to today's design and coding context.

The teacher initiates a structured oral decomposition activity, posing the following focus questions to the class in groups (not to individuals), applying wait time after each question:
- "Look at everything that is moving on screen. Can you name the separate, independent things you can see?"
- "What is the exact rule that makes the score go up — what has to happen?"
- "If you had to build this game from absolutely nothing, what would be the very first piece you would create?"

As students respond, the teacher records their suggestions on the whiteboard in three labelled columns, progressively narrowing the discussion through guided questioning until the class reaches agreement on the three Base Game components: **Bat** (player-controlled sprite), **Crystal** (falling sprite), **Score** (variable/counter). The teacher then explicitly sets the lesson's scope: "Today, we are only building these three pieces. Everything else you saw — the bomb, the speed-up — those are challenges we will choose from later. For now, simple and solid."

This activity operationalises the computational thinking strategy of **Decomposition** — the ability to observe a complex digital system and strip away non-essential features to identify the core functional architecture.

#### **Objective and Purpose** — Part 2 (5 minutes)
The teacher takes the roll quietly while the pre-prepared WALT/WILF slide is displayed on the projector. This lesson is grounded in constructivist theory: students actively construct understanding by observing a complex system, identifying its components, and building upon prior knowledge of digital tools and games.

The teacher reads the learning goals aloud using student-friendly language:
- **WALT:** "We are learning to: break a digital game into its key parts, set up our Scratch workspace, and save our work correctly."
- **WILF:** "What I am looking for: you can name at least three separate parts of a game, find the right blocks in Scratch, and have your project saved and named by the end of today."

---

### BODY (40 minutes)

#### **Input** — Part 1 (8 minutes)
Following the introduction, the teacher directs students to open Chrome and navigate to scratch.mit.edu and log in (or create an account). The Scratch interface is displayed on the projector. Using a physical pointer, the teacher identifies and names the three primary zones:

1. **The Stage** — "The screen your player will watch. This is where your finished game actually runs."
2. **The Sprite List** — "Your cast of characters. Every moving thing in your game — the Bat, the Crystal — lives here as a 'sprite'."
3. **The Code Blocks Area** — "Your instruction toolbox. You build your game's brain by dragging and snapping coloured blocks together here."

The zone definitions are deliberately student-friendly, prioritising comprehension over technical precision at this initial exposure. EAL/D and visual learner support is provided by using the projector pointer to physically highlight each zone as it is named. The teacher strictly respects the lesson's content boundary: no mention is made of X/Y coordinates, loops, or any block categories beyond the Events drawer.

#### **Modeling** — Part 2 (8 minutes)
With students watching the projector only (not yet touching their own devices), the teacher demonstrates all four mandatory workspace setup steps in sequence:

**Step 1 — Delete the default Cat sprite:**
Teacher demonstrates: "Right-click directly on the Cat icon in the Sprite List at the bottom right. A small menu will appear. Select 'Delete'. Your stage should now be completely empty."

**Step 2 — Add the Bat sprite:**
Teacher demonstrates: "See the blue circle with a small cat face at the bottom right of the Sprite List? Click it. In the library that opens, type 'Bat' into the search box. Click the Bat thumbnail to add it. You should see a Bat appear on your Stage."

**Step 3 — Add the Blue Sky backdrop:**
Teacher demonstrates: "Look at the very bottom right of the screen — there is a small landscape icon next to the word 'Stage'. Click it. In the backdrop library, search for 'Blue Sky' and click it. Your stage background should now be blue."

**Step 4 — Place the [When Green Flag Clicked] block:**
Teacher demonstrates: "Find the yellow Events category — it is the one that looks like a lightning bolt. Drag the [When Green Flag Clicked] block from the palette onto the empty script area. That block is your game's ignition switch."

Students observe the complete demonstration before touching their own devices. This full Modeling phase ensures all students have a clear mental model of the entire process before attempting it themselves.

#### **Checking for Understanding** — Part 3 (5 minutes)
Before releasing students to hands-on practice, the teacher poses the following questions to small groups (not to individuals), applying wait time and using Think-Pair-Share:
- "Point to where on the Scratch screen you would find the Events drawer. What colour is it?"
- "If I asked you to delete the Cat sprite right now, what would you click first?"
- "What is the name of the block that starts your program when you click the green flag?"

The teacher scans the room for hesitation or confusion. If more than one-third of the class cannot answer confidently, the teacher repeats the relevant step of the Modeling demonstration before proceeding. This gate check ensures that Guided Practice begins only when students are ready, preventing reinforcement of misconceptions.

#### **Guided Practice** — Part 4 (12 minutes)
Students now replicate all four workspace setup steps on their own devices. The teacher employs the "We do" phase of the Gradual Release of Responsibility pattern: each step is issued one at a time to manage cognitive load and prevent students from racing ahead.

**Step 1 — Delete the Cat sprite:**
Students execute the deletion step. The teacher circulates to confirm all students have an empty stage before proceeding.

**Step 2 — Add the Bat sprite:**
Students locate and add the Bat sprite from the library. The teacher circulates to confirm Bat is visible on all student stages.

**Step 3 — Add the Blue Sky backdrop:**
Students locate and apply the Blue Sky backdrop. The teacher circulates to confirm the backdrop is applied.

**Step 4 — Place the [When Green Flag Clicked] block:**
Students locate the yellow Events category and drag the green flag block onto their script area. The teacher circulates to visually confirm all students have the block placed.

Common errors intercepted during circulation: students adding a backdrop via the "Paint" option (redirect to the library search tab); students unable to find Bat (confirm correct spelling); students accidentally deleting the wrong element (undo with Ctrl+Z). If a student's device fails to load Scratch, the teacher pairs them temporarily with a neighbour rather than halting the entire class.

Differentiation: students experiencing difficulty receive direct 1:1 support; students who complete all four steps early may visually explore the remaining block categories (without dragging any blocks) and predict what each colour represents.

#### **Independent Practice** — Part 5 (7 minutes)
Students who have successfully completed all four mandatory workspace actions receive the Backup Worksheet. The teacher reads the task instructions aloud: "On your worksheet you will see a Scratch screenshot with five arrows pointing to different areas. For each arrow: write the name of that area, and write one sentence explaining what it does. Here is an example — arrow number one points to the Stage. You would write: Stage — the area where the game runs and is displayed to the player. Use that same format for all five."

During this phase, the teacher continues circulating to provide direct 1:1 support to students still completing the setup steps. Cooperative learning is permitted: students who have completed the worksheet may offer quiet verbal assistance to a neighbour who is still setting up, but may not touch the neighbour's keyboard.

---

### CONCLUSION (10 minutes)

#### Part 1 — Digital Asset Management: Naming and Saving (5 minutes)
The teacher signals the class to pause their Scratch work and direct attention to the projector. The teacher demonstrates the naming convention: "Click the project title at the very top of the screen — it currently says 'Untitled'. Replace it with your first name followed by the word 'Game'. For example: Alex's Game."

The teacher then demonstrates both saving methods:
- **Method 1 (cloud):** "Click 'File' in the top menu bar, then click 'Save now'. Scratch will save your project to your account online."
- **Method 2 (local backup):** "Click 'File' again, then 'Save to your computer'. This downloads a .sb3 file to your Downloads folder. Keep this as your backup."

The teacher conducts a final visual scan of all student screens to confirm every project is named and saved. This constitutes the lesson's exit requirement: no student is dismissed until their project is named and saved.

#### **Closure** — Part 2 (5 minutes)
The teacher poses three brief recap questions to small groups, using wait time:
- "We broke the game into parts today. What is the name for that thinking skill?"
- "What are the three zones of the Scratch screen? Can your group name all three?"
- "What is the very first block that every Scratch program must begin with?"

The teacher briefly acknowledges the class's progress: the three components identified today — Bat, Crystal, Score — are the exact building blocks that the next lesson will begin to activate. Students are dismissed in an orderly manner once all screens show a named, saved project. Students who completed the Backup Worksheet place it on the teacher's desk as they leave.

---

## Strategies to Evaluate Student Learning

### Formative Assessment (Assessment FOR Learning)
No diagnostic or summative assessment is planned for this first lesson. All assessment is formative:
1. **Structured teacher observation** during the Guided Practice phase: the teacher circulates and visually confirms each student has completed all four mandatory workspace actions (delete Cat, add Bat, add Blue Sky backdrop, place [When Green Flag Clicked] block).
2. **Oral group questioning** during the Checking for Understanding phase: the teacher poses decomposition and interface questions to small groups, listening for computational vocabulary to gauge readiness before Guided Practice begins.
3. **Backup Worksheet** (Assessment FOR Learning tool for fast finishers): students label the three Scratch interface zones on a printed diagram and write one sentence describing each zone's function. The teacher collects completed worksheets at the exit as a record of initial interface comprehension.

---

# PART TWO: Key Name to Content Mapping

The following section maps each JSON key name (x01–x61) to its corresponding content for this revised lesson plan.

| Key | Field Description | Content |
|---|---|---|
| x01 | Learning Area | Digital Technology |
| x02 | Lesson Number | 1 |
| x03 | Lesson Focus | Game Deconstruction and Scratch Environment Setup |
| x04 | Date | 30/04/2026 |
| x05 | Term | 2 |
| x06 | Time Period | Period 1 - 8:30 to 9:30 |
| x07 | Year Level | Year 8 |
| x08 | Learning Area Outcomes (SCSA Codes) | WA8DIGDI1 / WA8DIGDTID1 / WA8DIGDTPM1 / WA8DIGDTDE1 |
| x09 | Specific Learning Goals (array) | [Identify three Base Game components via Decomposition; Navigate three Scratch zones; Configure workspace with Bat/Blue Sky/green flag block; Apply naming and saving conventions] |
| x10 | Diagnostic Assessment Type | (empty) |
| x11 | Diagnostic Assessment Type (duplicate) | (empty) |
| x12 | Diagnostic Assessment Methods | (empty) |
| x13 | Formative Assessment Type | Formative |
| x14 | Formative Assessment Type (duplicate) | Formative |
| x15 | Formative Assessment Methods (array) | [Teacher observation during Guided Practice; Oral group Q&A during Checking for Understanding; Backup Worksheet for fast finishers] |
| x16 | Summative Assessment Type | (empty) |
| x17 | Summative Assessment Type (duplicate) | (empty) |
| x18 | Summative Assessment Methods | (empty) |
| x19 | What to Monitor (array) | [Correct identification of Bat/Crystal/Score; Events drawer located and green flag block placed; Project named and saved] |
| x20 | How to Monitor (array) | [Oral group questioning during Anticipatory Set and CfU phases; Physical screen circulation during Guided Practice; Final visual scan during Conclusion] |
| x21 | Students' Prior Knowledge (array) | [Basic ICT/browser proficiency; File management awareness; Event-driven logic from everyday experience; Game-as-rule-system familiarity; No prior Scratch experience assumed] |
| x22 | Preparation and Resources (array) | [Student devices; Projector; WALT/WILF slide; Demo game link; Scratch accounts; Backup Worksheets; Whiteboard and markers] |
| x23 | Intro Part 1 — Time | 5min |
| x24 | Intro Part 1 — Actions (array) | [Open demo on projector; play silently as students settle; pose decomposition questions to groups; record Bat/Crystal/Score on whiteboard; set scope boundary] |
| x25 | Intro Part 1 — Notes | MH Step — Anticipatory Set. Do not deliver WALT until Part 2. |
| x26 | Intro Part 2 — Time | 5min |
| x27 | Intro Part 2 — Strategy | MH Step — Objective and Purpose. Roll while WALT/WILF slide displayed. Constructivism stated. WALT read aloud. WILF read aloud. |
| x28 | Intro Part 2 — Focus Questions | Decomposition focus questions (posed in Part 1 to groups): What moves independently? What triggers scoring? Which element could the game not exist without? |
| x29 | Intro Part 3 — Time | (empty) |
| x30 | Intro Part 3 — Strategy | (empty) |
| x31 | Intro Part 3 — Notes | (empty) |
| x32 | Body Part 1 — Time | 8min |
| x33 | Body Part 1 — Strategy | MH Step — Input. Students open Scratch; teacher labels 3 zones on projector. Zone definitions in student-friendly language. |
| x34 | Body Part 1 — Notes | EAL/D support via pointer. Content boundary: no coordinates or loops introduced. |
| x35 | Body Part 2 — Time | 8min |
| x36 | Body Part 2 — Strategy | MH Step — Modeling. Teacher demos all 4 steps on projector only; students observe, do not touch devices. Steps 1-4 demonstrated in full. |
| x37 | Body Part 2 — Notes | Students observe complete demo before touching own devices. Common errors list. Device failure contingency. |
| x38 | Body Part 3 — Time | 5min |
| x39 | Body Part 3 — Strategy | MH Step — Checking for Understanding. Three group questions on zones and steps. Scan for hesitation. Gate: only proceed if class is ready. |
| x40 | Body Part 3 — Notes | Gate check: if >1/3 of class cannot answer, repeat relevant Modeling step before proceeding to Guided Practice. |
| x41 | Body Part 4 — Time | 12min |
| x42 | Body Part 4 — Strategy | MH Step — Guided Practice. Students replicate all 4 steps one at a time with teacher circulating. I-do/We-do pattern. Teacher confirms after each step. |
| x43 | Body Part 4 — Notes | Differentiation: 1:1 support for lagging students; visual exploration for fast finishers. Cooperative verbal help permitted. |
| x44 | Body Part 5 — Time | 7min |
| x45 | Body Part 5 — Strategy | MH Step — Independent Practice. Backup Worksheet distributed. Task instructions read aloud with example. Teacher continues circulating. |
| x46 | Body Part 5 — Notes | Differentiation: continued 1:1 support for remaining setup; visual block exploration for fast finishers. |
| x47–x52 | Body Parts 6–7 | (empty — not used in this lesson) |
| x53 | Conclusion Part 1 — Time | 5min |
| x54 | Conclusion Part 1 — Actions (array) | [Signal class to pause; demo naming convention; demo cloud save; demo local .sb3 save; final visual scan] |
| x55 | Conclusion Part 1 — Notes | Exit requirement: all students must have a named, saved project before dismissal. Worksheets collected at door. |
| x56 | Conclusion Part 2 — Time | 5min |
| x57 | Conclusion Part 2 — Strategy | MH Step — Closure. Three group recap questions (Decomposition term; three zone names; first block name). Acknowledge progress; orderly dismissal. |
| x58 | Conclusion Part 2 — Notes | Assessment FOR Learning: oral responses gauge retention of Decomposition, Stage/Sprite/Events vocabulary, and [When Green Flag Clicked] — all foundational to Lesson 2. |
| x59 | Conclusion Part 3 — Time | (empty) |
| x60 | Conclusion Part 3 — Strategy | (empty) |
| x61 | Conclusion Part 3 — Notes | (empty) |
