# Week 2 — Data Engineering & Preprocessing

Clean, well-engineered data is the foundation of every successful model. This is the week the models
stop being the interesting part.

<div dir="rtl" align="right">

# الأسبوع الثاني — هندسة البيانات والمعالجة المسبقة

البيانات النظيفة المُهندَسة جيدًا هي أساس كل نموذج ناجح. هذا هو الأسبوع الذي تتوقّف فيه النماذج عن كونها
الجزء المثير.

</div>

---

## What you'll be able to do by the end of the week

- Take a raw table and turn it into a feature table, using the handful of pandas operations that cover
  most real work — and know why `.apply()` is usually the wrong reflex.
- Produce a chart that changes a decision, and say in one sentence which decision it changed.
- Handle missing values because you know *why* they are missing, not because a tutorial said to impute
  with the median.
- Engineer a feature and measure the lift it actually contributed, separately from the others.
- Cross-validate properly, and recognise data leakage — the reason most impressive-looking student
  results are fake.

<div dir="rtl" align="right">

## ما ستقدر عليه بنهاية الأسبوع

- أن تُحوّل جدولًا خامًا إلى جدول خصائص بعمليات pandas القليلة التي تُغطّي معظم العمل الحقيقي — وأن تعرف
  لماذا يكون `.apply()` رِدّة فعل خاطئة في الغالب.
- أن تُنتج رسمًا يُغيّر قرارًا، وأن تكتب في سطر واحد أي قرار غيّره.
- أن تعالج القيم المفقودة لأنك تعرف **سبب** فقدانها، لا لأن درسًا على الإنترنت قال «استخدم الوسيط».
- أن تُهندس خاصية وتقيس مقدار ما أضافته وحدها لا مجتمعةً مع غيرها.
- أن تُطبّق التحقّق المتقاطع بشكل صحيح، وأن تكشف تسريب البيانات — وهو سبب أن معظم النتائج الطلابية
  المُبهرة نتائج زائفة.

</div>

---

## The days

| Day | Theory | Lab |
|---|---|---|
| **D1** | pandas as the ML data layer · NumPy arrays, shape, broadcasting · vectorisation instead of loops | **Data toolkit** — load, filter, group, merge; build the feature table the rest of the week uses |
| **D2** | Distributions · outliers · correlation is not causation · what a chart must answer | **EDA & visualisation** — five charts, each of which changes a modelling decision |
| **D3** | Missing data and why it is missing · imputation · categorical encoding (label, one-hot, target) | **Cleaning a messy dataset** — three imputation strategies, each measured |
| **D4** | Feature engineering · scaling and normalisation (Min-Max, Standard, Robust) | **Feature engineering** — engineer five features, measure the lift of each |
| **D5** | Overfitting · bias–variance · L1/L2/ElasticNet · K-Fold and Stratified K-Fold · **data leakage** · `Pipeline` | **Pipelines, regularisation & CV** — then break it on purpose with a leaking feature |

**Assignment 1** is due on D5. **Assignment 2** (data wrangling + cross-validation) is issued on D5 and
due W3D5.

<div dir="rtl" align="right">

## الأيام

| اليوم | النظري | المعمل |
|---|---|---|
| **١** | pandas كطبقة بيانات · NumPy والأشكال والبثّ · الحساب المُتجَهي بدل الحلقات | **صندوق أدوات البيانات** — بناء جدول الخصائص الذي يعتمد عليه الأسبوع |
| **٢** | التوزيعات · القيم الشاذّة · الارتباط ليس سببية · ما يجب أن يجيب عنه الرسم | **الاستكشاف والتصوير** — خمسة رسوم، كل واحد يُغيّر قرارًا |
| **٣** | القيم المفقودة وسبب فقدانها · الإكمال · ترميز المتغيّرات الفئوية | **تنظيف بيانات فوضوية** — ثلاث استراتيجيات إكمال مقيسة |
| **٤** | هندسة الخصائص · القياس والتوحيد | **هندسة الخصائص** — خمس خصائص وقياس إضافة كل واحدة |
| **٥** | فرط المطابقة · المقايضة بين التحيّز والتشتّت · التنظيم · التحقّق المتقاطع · **تسريب البيانات** | **خطوط المعالجة والتنظيم والتحقّق المتقاطع** — ثم اكسرها بعمود يُسرّب الهدف |

**التكليف الأول** يُسلَّم في اليوم الخامس، و**الثاني** يُطرح في اليوم الخامس ويُسلَّم في الأسبوع الثالث.

</div>

---

## The one sentence that matters this week

**A score you cannot reproduce on data the model has never seen is not a result.**

Everything this week — the splitting, the pipeline, the leakage hunt — exists to protect that sentence.
It is also the single most common reason a capstone falls apart in week 8: the model was excellent right
up until it met a file it had not been fitted on.

<div dir="rtl" align="right">

## الجملة الوحيدة المهمة هذا الأسبوع

**النتيجة التي لا تستطيع إعادة إنتاجها على بيانات لم يرها النموذج ليست نتيجة.**

كل ما في هذا الأسبوع — التقسيم وخط المعالجة والبحث عن التسريب — موجود لحماية هذه الجملة. وهي أيضًا أكثر
سبب يُفشِل مشروع التخرّج في الأسبوع الثامن: النموذج كان ممتازًا إلى أن قابل ملفًا لم يُدرَّب عليه.

</div>

---

## A warning about D5

D5 covers regularisation, cross-validation, leakage and `Pipeline` in one session. It is the densest day
of the week by design — the four ideas are one idea wearing four hats, and splitting them across two
days makes each one look smaller than it is. Come having done D3 and D4.

<div dir="rtl" align="right">

## تنبيه بشأن اليوم الخامس

اليوم الخامس يجمع التنظيم والتحقّق المتقاطع والتسريب و`Pipeline` في جلسة واحدة، وهو أكثف يوم في الأسبوع
عن قصد: الأفكار الأربع فكرة واحدة بأربعة أقنعة. تعال وقد أنجزت اليومين الثالث والرابع.

</div>
