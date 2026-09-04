# Week 8 — Capstone Sprint

Five weeks of project work land here. There is one short session on day one and none after it — the rest
of the week is your project, with the instructor and TA in the room.

<div dir="rtl" align="right">

# الأسبوع الثامن — أسبوع مشروع التخرّج

خمسة أسابيع من العمل على المشروع تتجمّع هنا. هناك جلسة قصيرة واحدة في اليوم الأول ولا شيء بعدها — وبقيّة
الأسبوع لمشروعك، والمدرّب والمساعد في القاعة معك.

</div>

---

## Why this week is light

Every other week is five taught days. This one is not, and that is a deliberate design decision rather
than a gap in the schedule.

Your capstone brief was released at the end of week 3. You have been building it for five weeks alongside
new content every single day. What you need now is time, review, and someone to tell you that your repo
has no README — not another lecture.

A taught session on Wednesday of this week would not be attended in spirit even if it were attended in
person.

<div dir="rtl" align="right">

## لماذا هذا الأسبوع مخفَّف

كل أسبوع آخر خمسة أيام تدريسية، وهذا الأسبوع ليس كذلك، وهذا قرار تصميمي لا ثغرة في الجدول. صدرت كرّاسة
مشروعك في نهاية الأسبوع الثالث، وأنت تبنيه منذ خمسة أسابيع مع محتوى جديد كل يوم. وما تحتاجه الآن هو الوقت
والمراجعة ومن يقول لك إن مستودعك بلا ملف README — لا محاضرة أخرى.

</div>

---

## The days

| Day | Session | What you do |
|---|---|---|
| **D1** | **~60 min** — what a model artifact really is (weights **and** fitted preprocessing) · versioning and reproducibility · inference on data the model has never seen · Streamlit / FastAPI for a demo · repo hygiene | **Get your capstone serving.** Export the artifact, load it in a fresh process, predict on unseen files, put an interface in front of it |
| **D2** | — | **Capstone clinic 1.** Instructor-led review, one project at a time, in front of the room |
| **D3** | — | **Capstone clinic 2** plus a technical-report writing workshop: what a hiring manager actually reads |
| **D4** | — | **Dress rehearsal.** Full 10-minute run-through each, integration fixes, **no new features** |
| **D5** | — | **Demo day.** 10-minute live demo + Q&A each. **Capstone final due** |

<div dir="rtl" align="right">

## الأيام

| اليوم | الجلسة | ما تفعله |
|---|---|---|
| **١** | **نحو ٦٠ دقيقة** — ما هو أثر النموذج فعلًا (الأوزان **ومعالجة البيانات المُدرَّبة**) · الإصدارات وقابلية إعادة الإنتاج · التنبؤ على بيانات لم يرها النموذج · Streamlit وFastAPI · نظافة المستودع | **اجعل مشروعك يعمل كخدمة** |
| **٢** | — | **عيادة المشروع ١** — مراجعة أمام القاعة، مشروعًا مشروعًا |
| **٣** | — | **عيادة المشروع ٢** وورشة كتابة التقرير الفني |
| **٤** | — | **التجربة النهائية** — عرض كامل عشر دقائق، وإصلاحات تكامل، و**لا مزايا جديدة** |
| **٥** | — | **يوم العرض** — عرض حيّ عشر دقائق وأسئلة. **تسليم المشروع النهائي** |

</div>

---

## D1 is the session the revised programme dropped

The programme document's revision removed model serving along with the old module 6. Capstone requirement
4 still asks for a model that predicts on unseen data through an interface, so the content survives — as
one short session, on the day you actually need it.

It is short because you have already met most of it: you saved a fitted `Pipeline` with `joblib` on W2D5,
and you reloaded a model and reproduced its score on W3D5 and W4D5. D1 assembles those habits into
something a stranger can run.

<div dir="rtl" align="right">

## اليوم الأول هو الجلسة التي حذفتها الوثيقة المُعدَّلة

حذف تعديل وثيقة البرنامج نشر النموذج مع الوحدة السادسة القديمة، لكن المتطلّب الرابع لمشروع التخرّج لا يزال
يطلب نموذجًا يتنبّأ على بيانات جديدة عبر واجهة، فبقي المحتوى — جلسةً قصيرة واحدة في اليوم الذي تحتاجه فيه
فعلًا. وهي قصيرة لأنك قابلت معظمها: حفظت `Pipeline` مُدرَّبًا في الأسبوع الثاني، وأعدت تحميل نموذج وأعدت
إنتاج نتيجته في الأسبوعين الثالث والرابع. واليوم الأول يجمع هذه العادات في شيء يستطيع غريبٌ تشغيله.

</div>

---

## What "done" means for the capstone

From [`../capstone/project_brief.md`](../capstone/project_brief.md), and it has not changed since week 3:

1. A real dataset you can defend, with a working data pull.
2. Cleaned data and EDA that changed at least one modelling decision.
3. A trained model that **beats a stated baseline**, with a saved artifact.
4. Predictions on data the model has never seen, through an interface.
5. A repository a stranger can clone and run, and a technical report.

Rubrics: [`../capstone/rubric.md`](../capstone/rubric.md) ·
[`../capstone/report_rubric.md`](../capstone/report_rubric.md) ·
[`../capstone/presentation_rubric.md`](../capstone/presentation_rubric.md).

<div dir="rtl" align="right">

## ما يعني «مُنجَز» في مشروع التخرّج

بيانات حقيقية تستطيع الدفاع عنها مع سحب بيانات يعمل · بيانات منظّفة واستكشاف غيّر قرارًا واحدًا على الأقل ·
نموذج مُدرَّب **يتجاوز خط أساس معلَن** مع أثر محفوظ · تنبؤات على بيانات لم يرها النموذج عبر واجهة ·
مستودع يستطيع غريبٌ استنساخه وتشغيله، وتقرير فني.

</div>

---

## D4 is a feature freeze

On Thursday you rehearse. You do not add anything.

Every cohort has a student who starts a new model on the day before demo day, breaks the thing that
worked, and demos nothing. The rehearsal exists to prevent that, and the freeze is not a suggestion.

If something is broken on D4, fix it. If something is missing on D4, it is missing.

<div dir="rtl" align="right">

## اليوم الرابع تجميد للمزايا

في اليوم الرابع تتدرّب على العرض ولا تُضيف شيئًا. في كل دفعة طالبٌ يبدأ نموذجًا جديدًا في اليوم السابق ليوم
العرض فيكسر ما كان يعمل ولا يعرض شيئًا. والتجربة النهائية موجودة لمنع ذلك، والتجميد ليس اقتراحًا: إن كان
شيء معطوبًا في اليوم الرابع فأصلحه، وإن كان ناقصًا فهو ناقص.

</div>

---

## Demo day format

10 minutes each, timed:

- **1 min** — the problem and who has it.
- **2 min** — the data, and one thing about it that surprised you.
- **2 min** — your approach, and the baseline you beat.
- **3 min** — **the live demo.** Working software, on your own machine, on data it has not seen.
- **2 min** — what you would do next, and Q&A.

A slide deck is optional. A working demo is not. Screenshots of a thing that used to work score as a
thing that does not work.

<div dir="rtl" align="right">

## صيغة يوم العرض

عشر دقائق لكل طالب بتوقيت: دقيقة للمشكلة ومن يعاني منها · دقيقتان للبيانات وشيء واحد فيها أدهشك · دقيقتان
للمنهج وخط الأساس الذي تجاوزته · **ثلاث دقائق للعرض الحيّ** على جهازك وعلى بيانات لم يرها النموذج · دقيقتان
لما ستفعله لاحقًا وللأسئلة. الشرائح اختيارية، والعرض الحيّ ليس اختياريًا؛ ولقطات شاشة لشيء كان يعمل تُحسب
شيئًا لا يعمل.

</div>
