# Capstone Rubric — Technical Work (30 of the 50%)

Grades the system itself: the data, the pipeline, the model, the artifact, the service, and the
evaluation. The report and the demo are graded separately by
[`report_rubric.md`](report_rubric.md) and [`presentation_rubric.md`](presentation_rubric.md).

<div dir="rtl" align="right">

# معيار تقييم مشروع التخرّج — العمل التقني (٣٠ من ٥٠٪)

يُقيّم النظام نفسه: البيانات وخط المعالجة والنموذج والأثر المحفوظ والخدمة والتقييم. أما التقرير والعرض
فيُقيَّمان بمعياريهما المستقلّين.

</div>

---

## Bands

| Band | Range | What it means |
|---|---|---|
| Excellent | 85–100 | Would be trusted with a real task on a junior team with light supervision |
| Good | 70–84 | Solid work; gaps in justification or engineering practice |
| Pass | 60–69 | Understands the fundamentals; execution is uneven |
| Fail | < 60 | Not yet employable in this field; the gaps are named in the feedback |

---

## Weights

| Criterion | Points |
|---|---|
| 1. Data and pipeline | 6 |
| 2. Modelling | 6 |
| 3. Evaluation honesty | 8 |
| 4. Artifact and serving | 6 |
| 5. Repository and engineering | 4 |
| **Total** | **30** |

**Criterion 3 carries the most weight deliberately.** Anyone can get a model to output a number. Knowing
whether the number means anything is what makes someone employable.

---

## 1. Data and pipeline (6)

| Band | Descriptor |
|---|---|
| **Excellent** | Real data from a source the student obtained themselves, with genuine problems in it. Every cleaning decision is deliberate and justified. The pipeline rebuilds from raw with one command and produces identical output. Feature choices are motivated by the domain, not by a tutorial. |
| **Good** | Real data, cleaned sensibly. The pipeline runs end to end with minor manual steps. Most decisions are justified. |
| **Pass** | The data is real but lightly processed. The pipeline works but is partly manual or partly notebook-bound. Cleaning is generic — dropped rows with no rationale. |
| **Fail** | A toy or pre-cleaned dataset. The pipeline cannot be re-run. Cleaning is absent or the data was used as-is. |

**Automatic cap at Pass:** the data is `iris`, `titanic`, MNIST, or a clean competition CSV, unless
approved in the proposal for a specific reason.

---

## 2. Modelling (6)

| Band | Descriptor |
|---|---|
| **Excellent** | The model choice fits the problem and the data volume, and is justified against **at least one alternative that was tried and rejected**. Hyperparameters were tuned on a validation set, never on test. The complexity is proportionate — the student did not reach for a neural network on 400 tabular rows, or a linear model on obviously non-linear data. |
| **Good** | A sensible model, properly trained, with some tuning. The justification is present but thin. |
| **Pass** | A model that works, chosen by default rather than by reasoning. Little or no tuning, or tuning done on the test set. |
| **Fail** | The model does not train, does not beat the baseline, or is grossly mismatched to the problem. |

**Note for markers:** a well-executed logistic regression with a clear rationale scores **above** an
unexplained deep network. Say this to students in week 3, not in week 8.

---

## 3. Evaluation honesty (8) ⭐

| Band | Descriptor |
|---|---|
| **Excellent** | A deliberately dumb baseline, beaten and reported. The metric fits the problem and the choice is defended. Error analysis on real failure cases identifies a **pattern**, not just examples. Limitations are specific and uncomfortable — the student names something that genuinely weakens their own result. Any leakage risk is discussed and ruled out with evidence. |
| **Good** | Baseline present and beaten. The metric is appropriate. Error analysis exists and is concrete. Limitations are real but generic. |
| **Pass** | A baseline exists, possibly a weak one. The metric is defensible but unexamined. Error analysis is a list of wrong predictions with no interpretation. Limitations are boilerplate ("more data would help"). |
| **Fail** | No baseline. The metric is wrong for the problem (accuracy on heavily imbalanced data). No error analysis. Limitations absent, or the result is presented as better than it is. |

**Hard rule:** a submission that reports an excellent score which turns out to rest on leakage or on
evaluating against training data scores **lower** than an honest weaker result. State this when the
brief is issued, and apply it.

**Marker prompt:** ask "what is the strongest argument that this result is wrong?" An Excellent
submission has already asked itself that question and answered it in the report.

---

## 4. Artifact and serving (6)

| Band | Descriptor |
|---|---|
| **Excellent** | The artifact contains weights, every fitted transformation, and metadata (classes, input shape, normalisation, metrics, versions, date). It loads in a fresh process through a single sanctioned `predict()` path — there is no second, drifting preprocessing implementation. The endpoint validates input, handles bad input with a clear error, returns a confidence, and reports low confidence rather than guessing on out-of-distribution input. |
| **Good** | The artifact loads cleanly and includes the preprocessing. The endpoint works and handles the obvious bad cases. |
| **Pass** | The artifact loads but is missing metadata or requires manual setup. The endpoint responds to valid input and breaks on invalid input. |
| **Fail** | No persisted artifact, or it cannot be loaded without re-running the notebook. No serving layer. |

**Verified live, not from the code.** On demo day: restart, load, send something new. Two minutes.

---

## 5. Repository and engineering (4)

| Band | Descriptor |
|---|---|
| **Excellent** | A stranger can clone it, follow the README, and run the demo without asking a question. Code lives in `src/` modules with clear names. `requirements.txt` is accurate. No secrets anywhere in the history. Commits span five weeks and their messages describe what changed. |
| **Good** | Clone-and-run works with a small stumble. Reasonable structure, accurate requirements, no secrets. |
| **Pass** | It runs with effort and some guessing. Structure is mostly one notebook. Requirements are incomplete. |
| **Fail** | Cannot be run from a clean clone. Secrets committed. One commit on the last day. |

**Check the git history for secrets, not just the working tree.** A key deleted in a later commit is
still in the repository.

---

## Marking procedure

1. **Clone it fresh** into an empty directory. Follow the README, nothing else. Note where you get stuck.
2. **Run the training command.** Does it rebuild the model?
3. **Load the artifact in a fresh Python process.** Predict on something new.
4. **Start the service.** Send it valid input, invalid input, and out-of-distribution input.
5. **Read the evaluation section** of the report and the code that produced it. Look specifically for
   leakage and for evaluation on training data.
6. Only then read the rest of the code.
7. Score each criterion, and write two sentences per criterion — what earned the band, and what would
   have moved it up one.

---

## Feedback

For each student, alongside the scores:

**The employability note.** Two paragraphs, honest:

- What they can already do that an employer would value.
- The **one** gap to close first, and how.
- Which role type fits them best on this evidence — data analyst, ML engineer, AI/LLM engineer, data
  engineer — and why.

Several students will use this verbatim to decide what to learn next. It is the single most valuable
artefact this course produces. Write it accordingly.

<div dir="rtl" align="right">

## التغذية الراجعة

مع الدرجات، اكتب لكل طالب **ملاحظة قابلية التوظيف**: فقرتان صادقتان عمّا يُتقنه فعلًا مما يقدّره سوق
العمل، والفجوة **الواحدة** التي يجب سدّها أولًا وكيف، ونوع الدور الأنسب له بحسب هذا الدليل وسببه.

سيستخدم عدد من الطلاب هذه الملاحظة حرفيًا ليقرّروا ما يتعلّمونه بعد المعسكر، وهي أثمن ما يُنتجه هذا
المقرّر. فاكتبها بما يليق بذلك.

</div>
