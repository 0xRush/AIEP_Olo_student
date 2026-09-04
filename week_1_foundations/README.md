# Week 1 — ML Foundations: Supervised & Unsupervised

The week you stop guessing what machine learning is and build one.

<div dir="rtl" align="right">

# الأسبوع الأول — أساسيات تعلّم الآلة: المُوجَّه وغير المُوجَّه

الأسبوع الذي تتوقّف فيه عن تخمين ما هو تعلّم الآلة وتبني نموذجًا فعليًا.

</div>

---

## What you'll be able to do by the end of the week

- Say precisely what AI, machine learning, and deep learning are and how they nest — and, more
  usefully, when a problem needs machine learning at all and when a few `if` statements are better.
- Explain why gradient descent works, having implemented it yourself on five numbers.
- Fit both kinds of supervised model — a regression and a classification — and read what their
  coefficients do and do not tell you.
- Report a score honestly: with a baseline beside it, on data the model has never seen, using the
  metric that matches the question rather than the one that looks best.
- Find structure in data that has no labels at all, and defend the number of clusters you chose.

<div dir="rtl" align="right">

## ما ستقدر عليه بنهاية الأسبوع

- أن تُحدّد بدقة ما هو الذكاء الاصطناعي وتعلّم الآلة والتعلّم العميق وعلاقتها ببعض — والأهم: متى تحتاج
  المسألة إلى تعلّم آلة أصلًا ومتى تكون بضعة شروط `if` أفضل.
- أن تشرح لماذا يعمل طريقة النزول التدريجي، بعد أن نفّذته بنفسك على خمسة أرقام.
- أن تُدرّب نوعي النماذج المُوجَّهة — انحدارًا وتصنيفًا — وتقرأ ما تقوله معاملاتها وما لا تقوله.
- أن تُعلن نتيجة بأمانة: بخط أساس بجانبها، على بيانات لم يرها النموذج، وبالمقياس الذي يناسب السؤال لا
  الذي يبدو أجمل.
- أن تجد بنيةً في بيانات بلا تسميات، وتُدافع عن عدد العناقيد الذي اخترته.

</div>

---

## The days

| Day | Theory | Lab |
|---|---|---|
| **D1** | AI / ML / DL · when learning from data beats writing rules · the ML lifecycle · environment and repo setup (Miniconda + uv) | **Setup & your first model** — the full five steps on real housing data. Produces `baseline.json` |
| **D2** | Linear regression: the line, the cost function, gradient descent — worked by hand on five points | **Gradient descent from scratch** — implement it in NumPy, watch the loss fall, then match `LinearRegression` |
| **D3** | Logistic regression · the sigmoid · decision boundaries · binary → multiclass | **Classification** — fit it, plot the boundary, read the coefficients |
| **D4** | Train / validation / test · confusion matrix · precision, recall, F1 · ROC-AUC · thresholds · class imbalance | **Evaluating honestly** — build the confusion matrix by hand, then move the threshold and watch the trade-off |
| **D5** | Unsupervised learning · K-Means · PCA · what "distance" means once columns have different units | **Clustering & PCA** — segment a real dataset with no labels and defend your choice of *k* |

**Assignment 1** (regression + classification) is issued on D4 and due W2D5.

<div dir="rtl" align="right">

## الأيام

| اليوم | النظري | المعمل |
|---|---|---|
| **١** | الذكاء الاصطناعي وتعلّم الآلة والتعلّم العميق · متى يتفوّق التعلّم من البيانات على كتابة القواعد · دورة حياة المشروع · تهيئة البيئة | **التهيئة وأول نموذج** — الخطوات الخمس كاملة على بيانات إسكان حقيقية |
| **٢** | الانحدار الخطي: الخط ودالة التكلفة وطريقة النزول التدريجي — محلولًا يدويًا على خمس نقاط | **طريقة النزول التدريجي من الصفر** — نفّذه بـ NumPy وطابِق نتيجة المكتبة |
| **٣** | الانحدار اللوجستي · الدالة السيغمويدية · حدود القرار · من ثنائي إلى متعدّد الفئات | **التصنيف** — درّب، وارسم الحدّ، واقرأ المعاملات |
| **٤** | التدريب والتحقّق والاختبار · مصفوفة الالتباس · الدقة والاستدعاء وF1 · العتبة · اختلال توازن الفئات | **التقييم بأمانة** — ابنِ المصفوفة بيدك ثم حرّك العتبة وراقب المقايضة |
| **٥** | التعلّم غير المُوجَّه · K-Means · تحليل المكوّنات الرئيسية · ماذا تعني «المسافة» حين تختلف وحدات الأعمدة | **التجميع وتقليل الأبعاد** — جزّئ بيانات بلا تسميات ودافِع عن عدد العناقيد |

**التكليف الأول** يُطرح في اليوم الرابع ويُسلَّم في الأسبوع الثاني اليوم الخامس.

</div>

---

## Before you start

Python and Git are assumed — they were entry requirements, and no session teaches them. If you are
rusty on comprehensions, dictionaries, or `git rebase`, refresh over the weekend rather than in class.

Set up once, on D1. Miniconda gives you the interpreter, **uv** installs the packages:

```bash
conda env create -f environment.yml
conda activate aiep
uv pip install -r requirements.lock
uv pip install -e shared/
```

Or one command: `make setup`.

**pandas and NumPy are taught properly in week 2**, which is where the programme puts them. This week's
labs hand you the data through `get_dataset(...)`, and D1's setup segment covers the handful of calls
you need until then. If you are impatient, week 2 day 1 is where it lands — not in a tutorial you find
on your own tonight.

<div dir="rtl" align="right">

## قبل أن تبدأ

بايثون وGit مفترضان مسبقًا — فقد كانا شرطي قبول ولا تُدرّسهما أي جلسة. وإن كنت غير متمكّن من
comprehensions أو القواميس أو `git rebase` فراجعها في عطلة نهاية الأسبوع لا داخل القاعة.

جهّز البيئة مرة واحدة في اليوم الأول بالأوامر أعلاه: Miniconda يعطيك المُفسّر، وأداة **uv** تُثبّت
الحِزم. **وpandas وNumPy تُدرَّسان في الأسبوع الثاني**، وهو موضعهما في البرنامج؛ ومعامل هذا الأسبوع
تُسلّمك البيانات جاهزة عبر `get_dataset(...)`.

</div>

---

## The habit this week is really about

**Never fit a model to data you have not looked at, and never report a score without a baseline
beside it.**

Both are trivial to state and almost universally skipped. Every embarrassing result in this field —
the fraud detector that was 99% accurate because 99% of transactions are legitimate, the model that
scored perfectly because the answer was hiding in a column — comes from skipping one of these two.

Get them into your hands this week and they will carry you through the capstone.

<div dir="rtl" align="right">

## العادة التي يدور حولها هذا الأسبوع فعلًا

**لا تُدرّب نموذجًا على بيانات لم تنظر إليها، ولا تُعلن نتيجة بلا خط أساس بجانبها.**

القاعدتان بسيطتان في القول ويتخطّاهما الجميع تقريبًا. وكل نتيجة محرجة في هذا المجال — كاشف الاحتيال
الذي بلغت دقته ٩٩٪ لأن ٩٩٪ من المعاملات سليمة أصلًا، والنموذج الذي جاء مثاليًا لأن الإجابة كانت مختبئة
في أحد الأعمدة — سببها تخطّي إحداهما.

رسّخهما هذا الأسبوع وستحملانك حتى مشروع التخرّج.

</div>
