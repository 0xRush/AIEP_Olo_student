# Capstone Report — Template

Copy this into your repo as `report.md`, fill it in, export to PDF, and commit both.

2,500–3,500 words. English or Arabic — neither is preferred. Delete these instructions as you go.

The word budgets below are guidance, not rules. But note where they are largest: sections 4 and 7 are
where marks are actually won, because they are the only ones somebody who did not do the work cannot
write.

<div dir="rtl" align="right">

# تقرير مشروع التخرّج — القالب

انسخ هذا الملف إلى مستودعك باسم `report.md`، واملأه، وصدّره إلى PDF، وارفع الاثنين.

من ٢٥٠٠ إلى ٣٥٠٠ كلمة، بالعربية أو الإنجليزية دون تفضيل لإحداهما. احذف هذه التعليمات أثناء الكتابة.

وأعداد الكلمات أدناه إرشادية. لكن لاحظ أين هي الأكبر: القسمان الرابع والسابع هما موضع الدرجات فعلًا،
لأنهما القسمان الوحيدان اللذان لا يستطيع كتابتهما من لم يقم بالعمل.

</div>

---

## Title

**A specific one.** "Predicting Delivery Delays for Riyadh Grocery Orders" — not "Machine Learning
Project".

Your name · cohort · date · repository URL.

---

## 1. The problem (~250 words)

- What are you predicting or retrieving, in one sentence a non-specialist understands.
- **Who would use the output, and for what decision?** If you cannot answer this, the project has no
  ground under it.
- Why does it matter — what happens today without it, and what changes with it.
- What would count as good enough to be useful? Give a number, and say where it came from.

> Write this section last. You will only know what the project was really about after you have built it.

---

## 2. The data (~400 words)

- Where it came from: the source, the licence, the date you pulled it.
- How you obtained it — API, scrape, download, manual labelling. **Include enough that someone could
  repeat it.**
- Shape: rows, columns, and what one row represents.
- The target: what it is, how it is distributed, and whether it is balanced.
- **What was wrong with it.** Every dataset has something. Missing values with a cause, a truncated
  range, duplicates, inconsistent categories, a sampling bias, a leaking column. Name at least one and
  say what it cost you.
- What you did about each problem, and what that decision traded away.

> A figure belongs here: the target distribution, or a missingness map.

---

## 3. Exploration (~300 words)

Not every chart you made. **The two or three that changed a decision**, and what each one changed.

For each: what it shows, what you concluded, and what you did differently as a result.

> If a chart changed nothing, leave it out. Decoration costs you space you need in section 4.

---

## 4. Method — what you built and what you rejected (~700 words) ⭐

**The most important section in the report.**

- The pipeline, end to end: ingest → clean → features → train → evaluate → persist. A diagram is worth
  three paragraphs here.
- The features you engineered and why each one should carry signal.
- The model you chose, and **why that one** — its fit to the data volume, the problem type, and the
  interpretability you needed.
- **What you tried and rejected.** At least one alternative, with the evidence:

  > "I tried a random forest first and it scored 0.68 against the logistic regression's 0.71, while
  > being far harder to explain to the person who would use it. I kept the simpler model."

  This paragraph is worth more than any accuracy number in your report.
- How you avoided leakage, and how you know — not that you were careful, but what you checked.
- Anything that did not work at all and why you think that was.

> Markers ask: could a competent colleague rebuild this from the report alone? Write for that reader.

---

## 5. Results (~450 words)

- **Your baseline, and its score.** Say what it was — the mean, the majority class, the most popular
  item. It should be dumb on purpose.
- Your model's score on the same held-out data, with the same metric.
- **The metric, and why that one.** If your classes are imbalanced and you report accuracy, this section
  fails regardless of the number.
- A results table: baseline versus your model, and any intermediate versions worth showing.
- Learning curves or a confusion matrix, labelled.
- What the number means **in the units of the problem**: "on average we are 12 minutes out on a delivery
  estimate" tells a reader something that "MAE 0.34" does not.

---

## 6. Error analysis (~400 words)

- Find the cases your system gets wrong. Look at them individually.
- **What do they have in common?** A pattern, not a list. "It fails on orders placed after 9pm and on
  the two least common categories" is analysis. Ten screenshots of wrong predictions is not.
- Is the failure the model's, the data's, or the problem's? These need different responses.
- Does it fail in a way that matters more for some users than others? Say so — this is where fairness
  becomes concrete rather than abstract.

---

## 7. Limitations (~300 words) ⭐

**Be uncomfortable here.** The best sentence available to you in this whole report begins:

> "The main reason this result might be wrong is…"

Cover:

- What your data cannot support. Sample size, coverage gaps, a time period that is not representative.
- What your evaluation does not prove. You tested on data from the same source and the same period as
  training — real deployment is not that.
- Where it would fail in production and you would not immediately notice.
- What you would need in order to trust it with a real decision.

> "More data would help" is boilerplate and scores nothing. Name **which** data, and **what** it would fix.

---

## 8. Next steps (~200 words)

Two or three concrete things, prioritised, that follow from section 7 rather than from a wish list.
For each: what it would cost and what it would buy.

---

## 9. How to run it (~150 words)

Setup, the retrain command, how to start the service, and how to send it a request. This can be a
pointer to the README if the README is genuinely complete — but check that it is, from a clean clone.

---

## References

Anything you drew on: papers, documentation, datasets, blog posts. Consistent format; the specific
citation style does not matter.

---

## Appendix (does not count towards the word limit)

- Full results tables.
- Additional figures.
- `AI_USAGE.md` contents, if you used AI assistance beyond documentation and debugging.

---

<div dir="rtl" align="right">

## بنية التقرير — ملخّص

١. المسألة (~٢٥٠ كلمة) — ماذا تتنبّأ به، ومن يستخدم النتيجة ولأي قرار، ولماذا تهم، وما «الجيّد بما يكفي».

٢. البيانات (~٤٠٠) — المصدر والرخصة وطريقة الحصول والشكل والهدف، و**ما كان معطوبًا فيها** وماذا فعلت.

٣. الاستكشاف (~٣٠٠) — الرسمان أو الثلاثة التي **غيّرت قرارًا**، وما غيّرته.

٤. المنهج — ما بنيته وما رفضته (~٧٠٠) ⭐ — خط المعالجة والخصائص واختيار النموذج و**بديل واحد على الأقل
جرّبته ورفضته مع الدليل**، وكيف تجنّبت التسرّب وكيف تأكّدت.

٥. النتائج (~٤٥٠) — **خط الأساس ونتيجته**، ونتيجتك على البيانات نفسها، والمقياس وسبب اختياره، وماذا يعني
الرقم بوحدات المسألة.

٦. تحليل الأخطاء (~٤٠٠) — **نمطٌ** لا قائمة. وهل الخلل من النموذج أم البيانات أم المسألة؟ ومن يتضرّر أكثر؟

٧. الحدود (~٣٠٠) ⭐ — كن غير مرتاح هنا. وأفضل جملة يمكنك كتابتها تبدأ بـ «أرجح سبب لكون هذه النتيجة
خاطئة هو…». وعبارة «مزيد من البيانات سيساعد» لا تُكسب شيئًا؛ حدّد **أي** بيانات و**ماذا** ستُصلح.

٨. الخطوات القادمة (~٢٠٠) — شيئان أو ثلاثة ملموسة مرتّبة بالأولوية، تنبع من القسم السابع.

٩. كيفية التشغيل (~١٥٠) — الإعداد وأمر إعادة التدريب وتشغيل الخدمة وإرسال طلب.

ثم المراجع والملاحق (لا تُحتسب ضمن عدد الكلمات).

</div>
