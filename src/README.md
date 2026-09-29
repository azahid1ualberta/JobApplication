# Generator

The PDFs under `applications/` are produced from these files. If the container
is ever lost again, this directory is enough to rebuild every document that has
a `content*.py` here.

    pip install reportlab fonttools pymupdf
    python fetch_fonts.py          # once, downloads and instances the typefaces
    python generate14.py           # writes the 117317 PDFs

| File | What it holds |
|---|---|
| `pdfbuilder3.py` | The renderer. Tagged-line content in, one-page PDF out. |
| `content3.py` | Shared blocks: contact details, the City / Metrolinx / Mott / UofA experience, skills, education. |
| `content13.py` | Timetabling Specialist, 117073 (closed 7 Sept 2026). |
| `content14.py` | Rail Simulation Specialist, 117317. |
| `generate14.py` | Builds 117317. Copy it for a new job. |
| `fetch_fonts.py` | Downloads Comfortaa, Nunito and Style Script, and cuts the static weights. |

## Adding a job

Write a `content<N>.py` that imports the shared blocks from `content3`, define a
`RESUME_<jobid>` and a `COVER_<jobid>`, then copy `generate14.py` and point it at
the new module. Keep both documents to one page — `generate14.py` shows the size
and spacing settings that achieve that.
