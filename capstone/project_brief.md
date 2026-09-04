# Capstone Project — Brief

**Released:** Week 3, Day 5 · **Due:** Week 8, Day 5 (demo day) · **Worth:** 50% of the programme

<div dir="rtl" align="right">

# مشروع التخرّج — التكليف

**يصدر:** الأسبوع الثالث اليوم الرابع · **يُسلَّم:** الأسبوع الثامن اليوم الرابع (يوم العرض) · **الوزن:** ٥٠٪

</div>

---

## What you are building

An AI system that **someone else can run**, on data **you** found, solving a problem **you** chose,
with a written account of how you got there and where it falls short.

Not a notebook. Not a Kaggle score. A working thing with a repository, an artifact, an endpoint, and a
report.

You have five weeks and roughly 40 hours. Scope accordingly — a small system that genuinely works beats
an ambitious one that does not.

<div dir="rtl" align="right">

## ما الذي تبنيه

نظام ذكاء اصطناعي **يستطيع غيرك تشغيله**، على بيانات **أنت** وجدتها، لحلّ مسألة **أنت** اخترتها، مع
تقرير مكتوب يشرح كيف وصلت وأين يقصّر نظامك.

ليس دفترًا، ولا نتيجة في مسابقة. بل شيء يعمل، له مستودع وأثر محفوظ ونقطة نهاية وتقرير.

أمامك خمسة أسابيع وقرابة ٤٠ ساعة. فاضبط الحجم على ذلك — فالنظام الصغير الذي يعمل فعلًا خير من الطموح
الذي لا يعمل.

</div>

---

## The eight requirements

Every one of these is checked. A project missing any of them cannot pass, regardless of how good the
rest is.

### 1. Real, messy data

**Not acceptable:** `iris`, `titanic`, MNIST, or a clean Kaggle competition CSV.

**Acceptable:** a public API you pull yourself · a corpus you scrape or collect · an open government
dataset (start at `data.gov.sa`) · two or more sources you merge · data you label yourself.

Your proposal must include a **working sample pull** — a script or cell that actually returns rows. "There
must be an API for this" is not a data source.

Your data must have at least one real problem in it, and your report must name it. Every dataset does.

### 2. A pipeline you designed

Ingest → clean → features or representation → train → evaluate → persist.

**Reproducible from raw data with one documented command.** `make train`, `python src/train.py`,
whatever — but one command, documented in the README, that rebuilds the model from scratch.

### 3. A persisted model artifact

The learned weights **and** every fitted transformation: the scaler, the encoder, the vectoriser, the
class-name mapping, the normalisation constants.

Loadable in a fresh process. **A notebook that only works top to bottom in one session does not meet
this requirement.** You will be asked to restart and load it.

### 4. Serving on unseen data

A FastAPI `/predict` endpoint or a Streamlit app that accepts input the model has never seen and
returns a prediction with a confidence.

Demoed live on demo day, with something new. Not a screenshot.

### 5. Honest evaluation

- A **baseline** you beat — and a deliberately dumb one, not a weak model.
- The **right metric for your problem**, chosen and justified. Accuracy on imbalanced data is not it.
- **Error analysis** on real failures: find the cases it gets wrong, look at them, and say what they
  have in common.
- **Stated limitations.**

A submission reporting a great score without noticing an obvious leak scores **worse** than an honest
weaker result. This is not a formality; it is how this is graded.

### 6. A clean GitHub repository

- A README that lets a stranger set it up and run the demo.
- Code in `src/` modules, not one 900-cell notebook. Notebooks are fine for exploration; the pipeline is
  not a notebook.
- `requirements.txt` reflecting what you actually import.
- **No secrets.** Check the git history, not just the current files.
- Meaningful commit history across five weeks. A single commit on the last day is itself a finding.

### 7. A technical report

2,500–3,500 words, English or Arabic. Structure in [`report_template.md`](report_template.md). It must
cover:

- The problem and why it matters.
- The data, where it came from, and what was wrong with it.
- **What you tried and rejected, and why.** Marks live here.
- What you built and how it works.
- Results against the baseline.
- Error analysis.
- **Limitations** — marks live here too.
- What you would do next.

### 8. A live demo and Q&A

Ten minutes: five demoing, three answering questions, two changing over.

**The Q&A is graded.** You will be asked things only the person who built it can answer.

---

## Choose one project type

You may propose something outside these three; it needs approval.

### (a) A predictive service on tabular data

Predict a number or a category from structured data, served behind an endpoint.

*Examples:* delivery-time estimation from logistics data · property valuation from listings you
scraped · demand forecasting from public retail or energy data · equipment-failure prediction from
sensor readings.

*Hard part:* the data is never clean, and the baseline is often better than you expect.

### (b) A computer-vision service

Classify, detect, or segment images, served behind an endpoint.

*Examples:* quality inspection on a product-photo set you assemble · document type classification ·
plant disease from leaf images · Arabic handwriting or sign classification.

*Hard part:* you will not have enough labelled images. That is what week 4 day 5 and week 6 were for.

### (c) An NLP system — semantic search, RAG, or a recommender

*Examples:* a RAG assistant over a document collection that matters to you (regulations, university
handbooks, technical manuals) · semantic search over a corpus you assembled · a content-based
recommender for a catalogue you scraped.

*Hard part:* evaluation. "It seems to work" is not a result, and week 7 day 4 exists because of this.

---

<div dir="rtl" align="right">

## المتطلّبات الثمانية

كلها تُفحَص، والمشروع الذي ينقصه أحدها لا يجتاز مهما كان بقيّته جيدًا.

**١. بيانات حقيقية وفوضوية** — لا iris ولا titanic ولا MNIST ولا ملف مسابقة نظيف. بل واجهة برمجية تسحب
منها بنفسك، أو مُدوّنة تجمعها، أو بيانات حكومية مفتوحة (ابدأ من `data.gov.sa`)، أو مصادر تدمجها، أو
بيانات تُسمّيها بنفسك. ويجب أن يتضمّن مقترحك **سحب عيّنة يعمل فعلًا**.

**٢. خط معالجة صمّمته أنت** — من الاستيراد إلى الحفظ، ويُعاد بناؤه من البيانات الخام **بأمر واحد موثّق**.

**٣. أثر محفوظ للنموذج** — الأوزان **وكل** تحويل مُدرَّب معها، قابل للتحميل في عملية جديدة. والدفتر الذي
يعمل في جلسة واحدة فقط **لا يفي بهذا المتطلّب**.

**٤. تشغيل على بيانات لم يرها** — نقطة نهاية `/predict` أو تطبيق Streamlit، يُعرض حيًّا يوم العرض.

**٥. تقييم أمين** — خط أساس تتفوّق عليه، ومقياس مناسب مُبرَّر، وتحليل للأخطاء الحقيقية، وحدود معلنة.
والتسليم الذي يعلن نتيجة ممتازة دون ملاحظة تسرّب واضح يُقيَّم **أسوأ** من نتيجة أضعف وأمينة.

**٦. مستودع نظيف** — README يكفي غريبًا لتشغيله، وشيفرة في `src/` لا في دفتر واحد ضخم، و`requirements.txt`
صادق، **ولا أسرار** (افحص تاريخ git لا الملفات الحالية فقط)، وسجلّ التزامات ممتدّ على خمسة أسابيع.

**٧. تقرير تقني** — من ٢٥٠٠ إلى ٣٥٠٠ كلمة، عربي أو إنجليزي، وفق القالب. و**ما جرّبته ورفضته** و**الحدود**
هما موضع الدرجات.

**٨. عرض حيّ وأسئلة** — عشر دقائق، والأسئلة **مُقيَّمة**.

## اختر نوعًا واحدًا

**(أ)** خدمة تنبّؤية على بيانات جدولية · **(ب)** خدمة رؤية حاسوبية · **(ج)** نظام لغوي: بحث دلالي أو RAG
أو توصية. ويمكنك اقتراح غيرها بموافقة مسبقة.

</div>

---

## Milestones — do not skip these

| Milestone | Due | What you must show |
|---|---|---|
| **Proposal** | W4D4 | Problem, data source **with a working sample pull**, target metric, why it matters |
| **M1 — Data + baseline** | W5D4 | Cleaned data, EDA, a deliberately dumb baseline score |
| **M2 — Model + artifact** | W6D5 | A model beating the baseline, saved artifact, load-and-predict script |
| **M3 — Pipeline + serving** | W7D4 | One-command retrain, `/predict` responding, repo structured |
| **Final** | W8D5 | Demo + repo + report |

Milestones are graded pass / needs-work and carry no marks on their own — but **missing two of them caps
the capstone at 70%**.

They exist because the failure mode is always identical: a student who starts building in week 7 ships
nothing in week 8. Catching that in week 5 is the entire point.

Details in [`milestones.md`](milestones.md).

---

## How it is graded

| Component | Weight | Rubric |
|---|---|---|
| Technical work | 30 | [`rubric.md`](rubric.md) |
| Report | 12 | [`report_rubric.md`](report_rubric.md) |
| Demo and Q&A | 8 | [`presentation_rubric.md`](presentation_rubric.md) |

---

## Using AI assistants

You will use them. The rule is about **understanding**, not tooling.

**Fine, no declaration needed:** documentation, tutorials, asking an assistant to explain a concept or
debug an error message, reviewing your own code.

**Fine, declare it** in an `AI_USAGE.md`: generated code you read, understood, adapted, and can explain;
assisted writing where the analysis is yours.

**Not allowed:** submitting code or writing you cannot explain. That is the actual line, and demo-day
Q&A is where it gets checked.

Full policy in [`../docs/Assessment_Guide.md`](../docs/Assessment_Guide.md).

<div dir="rtl" align="right">

## استخدام مساعدات الذكاء الاصطناعي

القاعدة عن **الفهم** لا عن الأداة. فالوثائق والشروح وتصحيح رسائل الخطأ ومراجعة شيفرتك مسموحة بلا إعلان.
والشيفرة المُولَّدة التي قرأتها وفهمتها وكيّفتها وتستطيع شرحها مسموحة **مع إعلانها** في ملف `AI_USAGE.md`.
أما تسليم شيفرة أو نصّ لا تستطيع شرحه فغير مسموح — وهذا هو الحدّ الفعلي، ويُفحص في أسئلة يوم العرض.

</div>

---

## Where to start

1. Read [`project_ideas.md`](project_ideas.md) — twelve concrete briefs with data sources and a note on
   what makes each hard.
2. Pick something you actually care about. Five weeks is a long time with a boring dataset.
3. **Pull the data before you propose it.** This single step prevents most week-7 disasters.
4. Copy [`starter_repo/`](starter_repo/) as your project skeleton.
5. Write the proposal.
