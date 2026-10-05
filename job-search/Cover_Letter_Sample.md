# Cover Letter - voice guide and reference sample

Updated 2026-09-26. The older 2025 City of Toronto letter has been retired as a
model: it was long, front-loaded with "my qualifications align perfectly", and
spent a paragraph on hobbies. The letter he writes now is shorter, plainer and
more direct, and that is the voice to use. Never reuse any sample verbatim -
write each letter from scratch for the specific employer and posting.

## Structure

Rendered by aaz_docs.py `build_cover_letter` - same Comfortaa letterhead as the
resume, then date, recipient block (first line bold), bold "Re: <job title>",
salutation, body, "Sincerely,", name. One page. Four or five body paragraphs.

1. **Why this job, in two sentences.** Name the role. If there is a real
   connection - he worked there before, the posting names a tool he has used -
   say it plainly in the first two lines.
2. **The posting's main requirement, answered with what he actually did.**
   Quote the requirement in the posting's own words, then answer it with
   specifics from Resume_Content.md, including the outcome.
3. **The second requirement, usually the people side.** Who he worked with and
   what he had to get agreed, not a claim about being a team player.
4. **The honest gap.** One paragraph naming the thing he does not have, framed
   as what he would be building on. This is a fixed convention of his letters -
   do not drop it, do not soften it into a strength, and do not invent a gap
   that isn't real. Follow it with why the underlying skill carries across.
5. **Two-line close.** Ask for the conversation, thank them.

## Voice rules

- Short declarative sentences. He writes the way he talks.
- "That was the job." Blunt sentences are in character.
- Concrete over abstract: tools, datasets, who he presented to, what changed.
- No "I believe my qualifications align", no "passionate", no "proven track
  record", no "perfectly". No paragraph about hobbies or awards.
- Em dashes and contractions are fine.
- Never claim experience that is not in Resume_Content.md, and never overstate
  a partial match - flag it in paragraph 4 instead.

## Reference sample - Metrolinx, Rail Simulation Specialist (2026-09-26)

Dear Hiring Manager,

I would like to apply for the Rail Simulation Specialist position. I worked at Metrolinx in Service Design through 2023 and into 2024, running the rail simulations this role is built around, so this would be a return rather than a first introduction.

The posting asks for rail network analysis, simulation model development and operational analysis against historical data and scenario models. That was the job. I ran OpenTrack simulations of GO rail services to test how infrastructure constraints and speed restrictions changed run times and schedule reliability - you change something physical on the network, and you want to know what it does to the service before anyone commits to it. I set up a command line workflow so slow orders could be pre-simulated in batches, which cut turnaround on scenario requests from days to hours. I also wrote a Python tool that read large JSON operations files and produced summaries of speed profiles and run-time variance, which was used to monitor how the railway was actually performing against what the model said it should.

The posting also asks for working with stakeholders and communicating results out of OpenTrack. At Metrolinx that meant schedulers, operations staff and engineers, and presenting the evidence behind service design decisions rather than just handing over an output file. Since January 2024 I have been an Assistant Planner with the City of Toronto, where I run assigned studies from scoping through to recommendations on my own, write the briefing notes, and present findings to planners, engineers and managers across divisions who do not necessarily agree with each other.

One thing I would be building on rather than bringing fully formed: my simulation work has been in OpenTrack rather than Rail Traffic Controller, and it has been commuter rail - the GO network specifically - rather than across the range of network types the posting mentions. The underlying discipline of building a defensible model and knowing where it stops being trustworthy carries across, and OpenTrack is the tool listed as the asset, but I would rather say that plainly now than have it surface later.

I would welcome the chance to talk about the role. Thank you for considering my application.

Sincerely,
Abdullah Al Zahid
