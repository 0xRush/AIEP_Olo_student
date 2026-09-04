# AIEP — Olo Academy AI Engineering Bootcamp

Labs, datasets, and the capstone brief for the 8-week AI Engineering Bootcamp.

<div dir="rtl" align="right">

# معسكر هندسة الذكاء الاصطناعي — أكاديمية علو

معامل المعسكر وبياناته ومشروع التخرّج، على مدى ثمانية أسابيع.

</div>

---

## Day one — do this once

1. **Fork this repository** on GitHub. Your fork is where all your work lives for the whole
   bootcamp: labs, assignments, and the capstone.
2. Clone your fork and connect it back to the course repo:
   ```bash
   git clone https://github.com/<your-username>/AIEP_Olo_student.git
   cd AIEP_Olo_student
   git remote add upstream https://github.com/0xRush/AIEP_Olo_student.git
   ```
3. Build the environment:
   ```bash
   conda env create -f environment.yml
   conda activate aiep
   uv pip install -r requirements.lock
   uv pip install -e shared/
   ```
   Miniconda gives you the interpreter; `uv` installs the packages, and `requirements.lock` pins
   every version so your environment matches everyone else's.
   No conda? `uv venv && uv pip install -r requirements.lock && uv pip install -e shared/`
   No laptop? Everything runs on Google Colab — see below.

<div dir="rtl" align="right">

## اليوم الأول — نفّذ هذا مرة واحدة

١. **أنشئ نسخة (Fork) من هذا المستودع** على GitHub. نسختك هي مكان كل عملك طوال المعسكر: المعامل
   والتكاليف ومشروع التخرّج.
٢. استنسخ نسختك واربطها بمستودع المعسكر (انظر الأوامر أعلاه).
٣. جهّز البيئة بالأوامر أعلاه: Miniconda يعطيك مُفسّر بايثون، وأداة `uv` تُثبّت الحِزم، وملف
   `requirements.lock` يُثبّت كل النسخ فتكون بيئتك مطابقة لبيئة زملائك. وإن لم يكن conda لديك فاستخدم
   `uv venv`، أو اعمل على Google Colab.

</div>

---

## Every day

```bash
git pull upstream master    # morning: today's lab, and yesterday's solution
# … work …
git add . && git commit -m "W3D2 lab" && git push
```

Commit every day. Your eight weeks of commit history is part of what the capstone is graded
on — and it is what you show an employer.

<div dir="rtl" align="right">

## كل يوم

اسحب التحديثات صباحًا بأمر `git pull upstream master` لتحصل على معمل اليوم وحلّ الأمس، ثم اعمل،
ثم ارفع عملك مساءً بـ `git add` و`git commit` و`git push`.

التزم بالرفع يوميًا؛ فسجلّ التزاماتك عبر ثمانية أسابيع جزء من تقييم مشروع التخرّج، وهو ما تعرضه
على جهة التوظيف.

</div>

---

## Three versions of every lab

| File | Use it when |
|---|---|
| `*_blank.ipynb` | **Start here.** The real lab. Hints tell you what to do and where to look — not what to type |
| `*_guided.ipynb` | You have been stuck on one task for more than ten minutes. Most of the code is here; fill in the `# TODO` lines |
| `*_solution.ipynb` | Released at the end of each day. Read it, compare it to what you wrote |

Using the guided version is **not** cheating. Sitting stuck in silence is the only mistake.

**Never edit `*_solution.ipynb`** — it gets overwritten every time you pull.

<div dir="rtl" align="right">

## ثلاث نسخ لكل معمل

`*_blank.ipynb` هو المعمل الحقيقي وابدأ منه؛ والإرشادات فيه تخبرك بما تفعله وأين تبحث لا بما تكتبه
حرفيًا. و`*_guided.ipynb` للحالة التي تتوقّف فيها أكثر من عشر دقائق عند مهمة واحدة، وفيه معظم الشيفرة
وعليك إكمال أسطر `# TODO`. و`*_solution.ipynb` يُنشر في نهاية كل يوم فاقرأه وقارنه بما كتبت.

استخدام النسخة الموجَّهة **ليس غشًّا**، والخطأ الوحيد أن تبقى متوقّفًا بصمت.
ولا تُعدّل ملف الحل أبدًا، فهو يُستبدل مع كل عملية سحب.

</div>

---

## Data

You never need to find or move a data file. Every notebook calls:

```python
DATA = get_dataset("<name>")
```

which looks in the local cache, then in your Colab session, then downloads it — and if all
of that fails, it asks you to upload the file and tells you exactly which one.

<div dir="rtl" align="right">

## البيانات

لن تحتاج أبدًا للبحث عن ملف بيانات أو نقله. فكل دفتر يستدعي `get_dataset` التي تبحث في الذاكرة
المحلية ثم في جلسة Colab ثم تُنزّل الملف، وإن فشل كل ذلك طلبت منك رفعه وأخبرتك باسمه بالضبط.

</div>

---

## Google Colab

Open any notebook at:

```
https://colab.research.google.com/github/0xRush/AIEP_Olo_student/blob/master/<path-to-notebook>
```

The setup cell installs everything the lab needs. Colab does **not** save back to GitHub
automatically — use *File → Save a copy in GitHub* to push to your fork.

<div dir="rtl" align="right">

## Google Colab

افتح أي دفتر عبر الرابط أعلاه، وستُثبّت خلية الإعداد كل ما يحتاجه المعمل. ولا يحفظ Colab إلى GitHub
تلقائيًا، فاستخدم *File ← Save a copy in GitHub* لرفع عملك إلى نسختك.

</div>

---

## Submitting

Everything goes in your fork:

```
assignments/A1_first_model/A1.ipynb  +  report.pdf
capstone/
```

Push, then paste the commit URL into the LMS before the deadline. Your commit timestamp is
the submission time.

<div dir="rtl" align="right">

## التسليم

كل شيء في نسختك من المستودع، ضمن مجلّدَي `assignments/` و`capstone/`. ارفع عملك ثم ضع رابط
الالتزام (commit) في المنصة قبل الموعد النهائي؛ ووقت الالتزام هو وقت التسليم المعتمد.

</div>

---

## Something broken?

| Problem | Fix |
|---|---|
| `ModuleNotFoundError: aiep` | Re-run `pip install -e shared/`, then check *Kernel → Change kernel → Python (aiep)* |
| `git pull` conflicts | You edited a `_solution.ipynb`. `git checkout --theirs <file>` and work in `_blank` instead |
| A dataset won't download | Re-run the cell; if it still fails it will offer you an upload prompt |
| Anything else | Ask in the cohort channel. Paste the full error, not a screenshot of part of it |
