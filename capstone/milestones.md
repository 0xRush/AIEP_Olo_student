# Capstone Milestones

Five checkpoints between the brief and demo day. Each is a ten-minute conversation during a lab slot.

<div dir="rtl" align="right">

# مراحل مشروع التخرّج

خمس نقاط تفتيش بين صدور التكليف ويوم العرض، كل واحدة محادثة من عشر دقائق ضمن وقت المعمل.

</div>

---

## Why these exist

The failure mode is always the same: a student starts building in week 7 and ships nothing in week 8.
Every milestone is a chance to catch that while it is still fixable.

Milestones are graded **pass / needs-work** and carry no marks on their own. But **missing two of them
caps the capstone at 70%** — because by then the project is in real trouble and pretending otherwise
helps nobody.

<div dir="rtl" align="right">

## لماذا هذه المراحل

نمط الفشل واحد دائمًا: طالب يبدأ البناء في الأسبوع السابع فلا يُسلّم شيئًا في الثامن. وكل مرحلة فرصة
لاكتشاف ذلك وهو ما يزال قابلًا للإصلاح.

تُقيَّم المراحل بـ «مُجتاز / يحتاج عملًا» ولا تحمل درجات بذاتها، لكن **تفويت اثنتين منها يسقف درجة المشروع
عند ٧٠٪** — لأن المشروع حينها في ورطة حقيقية، والتظاهر بغير ذلك لا يفيد أحدًا.

</div>

---

## Proposal — W4D4

**One page. Bring it printed or on screen.**

| Must contain | Why |
|---|---|
| The problem, in one sentence | If you cannot state it in one sentence, it is not scoped |
| Who would use the result and for what decision | Stops "predict something" projects |
| **The data source, with a working sample pull** | The gate that prevents most week-7 disasters |
| Rows, columns, and one thing already wrong with the data | Proves you looked |
| The target metric, and why that one | Accuracy on imbalanced data is a rejection |
| The dumb baseline you will compare against | Forces you to have one |
| Project type — (a), (b), or (c) | Determines what your serving layer looks like |

**Rejected if:** there is no working sample pull · the dataset is `iris`, `titanic`, MNIST, or a clean
competition CSV · the scope is a research programme rather than a five-week project.

**A rejected proposal is not a failure** — it is the cheapest possible correction. Resubmit within three
days.

<div dir="rtl" align="right">

### المقترح — الأسبوع ٤ اليوم ٤

صفحة واحدة تحتوي: المسألة في جملة، ومن يستخدم النتيجة ولأي قرار، و**مصدر البيانات مع سحب عيّنة يعمل**،
وعدد الصفوف والأعمدة وعيب واحد معروف في البيانات، والمقياس المستهدف وسببه، وخط الأساس الغبي الذي ستقارن به،
ونوع المشروع.

**يُرفض إذا:** لم يوجد سحب عيّنة عامل، أو كانت البيانات من المجموعات الجاهزة النظيفة، أو كان النطاق برنامج
بحث لا مشروع خمسة أسابيع. والرفض ليس فشلًا بل أرخص تصحيح ممكن؛ أعد التسليم خلال ثلاثة أيام.

</div>

---

## M1 — Data and baseline — W5D4

**Show, do not describe.** Open the notebook and run it.

| Must show | The check |
|---|---|
| Data loaded from your source, reproducibly | Not a one-off manual download you cannot repeat |
| Cleaning done, with the decisions written down | The `cleaning_log` habit from W2D3 |
| EDA: at least three charts that changed a decision | Each with a sentence on what it changed |
| **A baseline score** | Mean, majority class, or most-popular. Deliberately dumb |
| The metric computed on a held-out split | Not on training data |

**Needs work if:** there is no baseline · the data is still raw · the split does not exist yet.

**No baseline means needs-work**, however good the data looks. The baseline is the thing that makes
every later number meaningful.

---

## M2 — Model and artifact — W6D5

**The check is specific and it is not about accuracy.**

| Must show | The check |
|---|---|
| A trained model beating the baseline | By any margin — beating it is the bar, not by how much |
| A saved artifact: weights **and** fitted preprocessing | W2D5's `joblib` habit, completed in W8D1 |
| **A load-and-predict script that runs in a fresh process** | You will be asked to restart and run it |
| A prediction on a row or file never used in training | Live, in front of the instructor |

**Needs work if:** the model only exists in a running kernel · the preprocessing is not saved with it ·
loading it requires manually re-running notebook cells.

A student with 0.94 accuracy who cannot load their model in a fresh process is **needs-work**. A student
with 0.71 who can is **pass**. Say this clearly when M1 is returned.

---

## M3 — Pipeline and serving — W7D4

**The last checkpoint. After this, you are on your own until demo day.**

| Must show | The check |
|---|---|
| One documented command that retrains from raw data | `make train` or equivalent, in the README |
| `/predict` responding | Live, from a running server |
| The endpoint handling a bad input without a stack trace | Send it something wrong on purpose |
| Repo structure: `src/`, `README.md`, `requirements.txt` | Not one giant notebook |
| The report started, with a section skeleton | An empty file is needs-work |

**Needs work if:** the pipeline cannot be re-run · the endpoint does not exist · the repo is a single
notebook.

**Anyone not at M3 leaves this session with a written, scoped-down plan for week 8, agreed with an
instructor.** A smaller thing that works demos far better than an ambitious thing that does not — and
being told this on Thursday of week 7 is a kindness, not a criticism.

---

## Final — W8D5

Demo day. Full requirements in [`project_brief.md`](project_brief.md).

**Submit before the session starts:**

- The repository URL (your fork, or a separate repo linked from it).
- The report as a PDF, committed to the repo.
- `AI_USAGE.md` if you used AI assistance beyond the always-fine category.

**Bring to the demo:**

- Your system running — server started before your slot, not during it.
- Something new to send it, that it has never seen.
- One failure case you chose to show.

---

## What "needs work" means

It is not a punishment and it is not a mark. It means: *this specific thing is not there yet, here is
what to do first, and here is when I will check again.*

Every needs-work comes with three written lines from the instructor:

```
Working:  <the thing that is genuinely fine>
At risk:  <the specific gap>
Do next:  <one concrete action for tomorrow morning>
```

Keep them. By week 8 they are the most accurate record of your project's history that exists.

<div dir="rtl" align="right">

## ماذا يعني «يحتاج عملًا»

ليست عقوبة ولا درجة، بل تعني: هذا الشيء تحديدًا غير جاهز، وهذا ما تفعله أولًا، وهذا موعد المراجعة التالية.

وكل تقييم «يحتاج عملًا» يأتي بثلاثة أسطر مكتوبة من المدرّب: ما الذي يعمل جيدًا، وما الفجوة تحديدًا، وما
الإجراء الملموس لصباح الغد. احتفظ بها — فهي بحلول الأسبوع الثامن أدقّ سجلّ موجود لتاريخ مشروعك.

</div>

---

## Instructor notes

- **Ten minutes each, timed.** With 25 students that is over four hours, so milestones run across the
  whole lab slot while the room works on that day's lab. Design the lab that day to tolerate it — the
  specs for W4D4, W5D4, W6D5, and W7D4 already account for this.
- **Make them run it.** A milestone check where the student describes their work instead of executing it
  is worthless. Every one of these can be verified in under two minutes by running something.
- **Write the three lines the same day.** Feedback delivered a week later has missed its window.
- **Flag two consecutive needs-work to programme leadership immediately**, not in week 8.
- Record everything in the cohort spreadsheet described in
  [`../docs/Assessment_Guide.md`](../docs/Assessment_Guide.md).
