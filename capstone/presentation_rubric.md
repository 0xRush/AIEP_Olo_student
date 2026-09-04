# Capstone Rubric — Demo and Q&A (8 of the 50%)

Ten minutes: five demoing, three answering questions, two changing over.

<div dir="rtl" align="right">

# معيار تقييم العرض والأسئلة (٨ من ٥٠٪)

عشر دقائق: خمس للعرض، وثلاث للأسئلة، ودقيقتان للتبديل.

</div>

---

## Weights

| Criterion | Points |
|---|---|
| 1. The live demo | 3 |
| 2. **Q&A** | 4 |
| 3. Communication | 1 |
| **Total** | **8** |

**The Q&A is worth more than the demo.** A polished demo can be rehearsed by anyone. Answering "why did
you drop that column?" cannot.

---

## What the demo must show

Told to students a week in advance, and marked against exactly this:

1. The problem, in one sentence, and why it is worth solving.
2. The data, and **one honest thing that was wrong with it**.
3. **The system running live**, given something it has never seen.
4. The result against the baseline.
5. **One failure case**, shown deliberately.

Point 5 is not a trap. A student who shows where their system breaks is demonstrating that they
understand it — and markers should reward that, visibly, so the rest of the cohort sees it rewarded.

<div dir="rtl" align="right">

## ما يجب أن يُظهره العرض

المسألة في جملة وسبب أهميتها · البيانات و**عيب واحد صادق فيها** · **النظام يعمل حيًّا** على شيء لم يره
قط · النتيجة مقارنةً بخط الأساس · **حالة فشل واحدة** يعرضها عمدًا.

والنقطة الأخيرة ليست فخًّا: من يعرض موضع انكسار نظامه يُثبت أنه يفهمه، وعلى المُقيّم أن يكافئ ذلك علنًا
حتى ترى بقية الدفعة أنه يُكافأ.

</div>

---

## 1. The live demo (3)

| Band | Descriptor |
|---|---|
| **Excellent** | The system runs live on genuinely new input. The five points are covered in five minutes without rushing. A failure case is shown deliberately and explained. The demo makes the value obvious to someone who has not read the report. |
| **Good** | The system runs live. Most points covered. The failure case is mentioned rather than shown. |
| **Pass** | The system runs, but on pre-prepared input, or with a rehearsed path that avoids anything risky. Some points missed. |
| **Fail** | No live demo — screenshots or a recording. The system does not start. Time badly overrun. |

**Automatic cap at Pass** if the input was not new. Start your server before your slot, not during it.

---

## 2. Q&A (4) ⭐

Three minutes. Two or three questions. Ask things **only the builder can answer**.

### The question bank

- "Why this metric and not accuracy?"
- "What happens if I send your endpoint an empty file?"
- "Why did you drop that column?"
- "You have 400 training rows and a neural network. Defend that."
- "What is the worst way this fails in production?"
- "Your baseline is 0.62 and your model is 0.71. Is that worth deploying?"
- "Where in your pipeline could data have leaked, and how do you know it did not?"
- "What would you do first if you had another week?"
- "If your data doubled, what would you change?"

| Band | Descriptor |
|---|---|
| **Excellent** | Answers immediately and specifically, including "I do not know" where that is the honest answer — followed by how they would find out. Distinguishes what they measured from what they assume. Engages with a challenge to their result rather than defending it reflexively. |
| **Good** | Answers correctly with some hesitation. Understands their own system. Occasionally over-claims. |
| **Pass** | Answers the easy questions; vague on the harder ones. Can describe what the code does but not why. |
| **Fail** | Cannot explain choices in their own submission. Answers contradict the report or the code. Attributes decisions to a tutorial or a tool without understanding. |

**This is the integrity check.** A student who built the system answers instantly. A student who did not,
cannot — and no plagiarism scan approaches this for reliability. Where the answers make it clear the
work is not theirs, follow the academic-integrity process in
[`../docs/Assessment_Guide.md`](../docs/Assessment_Guide.md).

**"I do not know, but here is how I would find out" is a strong answer, not a weak one.** Mark it that
way, and make sure the room sees you do it.

---

## 3. Communication (1)

| Band | Descriptor |
|---|---|
| **Excellent** | A non-specialist follows the whole thing. No unexplained jargon. Slides support rather than compete. Finishes inside five minutes. |
| **Good** | Clear and well-paced with minor lapses into jargon. |
| **Pass** | Followable but disorganised, or over time, or dense with unexplained terminology. |
| **Fail** | Cannot be followed. Significantly over time. |

Language is the student's choice — Arabic or English, neither preferred.

---

## Running the session

- **Timekeep strictly.** With 25 students this is over four hours. Publish the running order and the
  break times in advance; hold to them.
- **Two markers per student where possible**, scoring independently and reconciling afterwards.
- **Score during the changeover**, not at the end of the day. Twenty-five demos blur together.
- **Have a fallback.** If a student's machine dies, give them the next slot rather than a zero — and
  score what you can from the repository.
- **Ask everyone at least one hard question.** A student who only gets easy questions has been marked on
  less evidence than their peers, which is unfair in both directions.
- **Close the cohort out** with three things that went well across all projects, three recurring
  mistakes, and the employability notes handed over.

<div dir="rtl" align="right">

## إدارة الجلسة

التزم بالوقت بصرامة وانشر الترتيب والاستراحات مسبقًا · مُقيّمان لكل طالب إن أمكن، يُقيّمان مستقلًّين ثم
يتّفقان · سجّل الدرجات أثناء التبديل لا في آخر اليوم · إن تعطّل جهاز طالب فامنحه الدور التالي ولا تصفّره ·
اطرح سؤالًا صعبًا واحدًا على الأقل على الجميع، فمن لم يُسأل إلا الأسهل قُيّم على دليل أقلّ من زملائه ·
واختم بثلاثة نجاحات عامة وثلاثة أخطاء متكرّرة وتسليم ملاحظات قابلية التوظيف.

</div>
