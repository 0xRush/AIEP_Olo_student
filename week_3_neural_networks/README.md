# Week 3 — Deep Learning & Neural Networks

The week you build a neural network from nothing but NumPy, and then find out whether it was worth it.

<div dir="rtl" align="right">

# الأسبوع الثالث — التعلّم العميق والشبكات العصبية

الأسبوع الذي تبني فيه شبكة عصبية من NumPy وحدها، ثم تكتشف هل كان الأمر يستحق.

</div>

---

## What you'll be able to do by the end of the week

- Fit a decision tree, a random forest and a gradient-boosted model on tabular data, and read a feature
  importance chart without over-claiming what it proves.
- Compute a forward pass through a two-layer network by hand, and get the same numbers from your own
  NumPy code.
- Explain what backpropagation is by having measured a gradient numerically, not by reciting the chain
  rule.
- Rebuild the same network in PyTorch and say exactly which part the library replaced.
- Diagnose a training run from its loss curve: too high a learning rate, overfitting, a dead layer.

<div dir="rtl" align="right">

## ما ستقدر عليه بنهاية الأسبوع

- أن تُدرّب شجرة قرار وغابة عشوائية ونموذج تعزيز اشتقاقي على بيانات جدولية، وأن تقرأ مخطّط أهمية
  الخصائص دون أن تُحمّله أكثر مما يحتمل.
- أن تحسب المرور الأمامي في شبكة ذات طبقتين بيدك، وأن تحصل على الأرقام نفسها من شيفرتك بـ NumPy.
- أن تشرح ما هو الانتشار الخلفي بعد أن قِست الاشتقاق عدديًا بنفسك، لا بترديد قاعدة السلسلة.
- أن تُعيد بناء الشبكة نفسها بـ PyTorch وتُحدّد بالضبط أي جزء تولّت عنه المكتبة.
- أن تُشخّص تدريبًا من منحنى الخسارة: معدّل تعلّم مرتفع، أو فرط مطابقة، أو طبقة ميتة.

</div>

---

## The days

| Day | Theory | Lab |
|---|---|---|
| **D1** | Decision trees · how one tree overfits · random forests · gradient boosting · feature importance and its limits | **Trees & ensembles** — beat the week-1 linear baseline, and record the score the neural net has to beat |
| **D2** | Why deep networks win on some data and lose on tabular · perceptron → MLP · activations · a forward pass by hand | **Forward pass in NumPy** — build it by hand, match the slide's numbers exactly |
| **D3** | Loss functions (MSE, Cross-Entropy) · backpropagation, computed numerically | **Backprop from scratch** — add the backward pass and watch it learn |
| **D4** | PyTorch: tensors, autograd, `Dataset`/`DataLoader`, the training loop | **Same network in PyTorch** — same result, a tenth of the code |
| **D5** | Optimisers (SGD, momentum, Adam, RMSprop) · dropout · batch normalisation · early stopping | **Tuning an MLP** — an experiment grid, and a final architecture you can justify |

**Assignment 3** (neural network classification challenge) is issued on D3 and due W4D2.
**Assignment 2** is due on D5. **The capstone brief is released on D5.**

<div dir="rtl" align="right">

## الأيام

| اليوم | النظري | المعمل |
|---|---|---|
| **١** | أشجار القرار · فرط مطابقة الشجرة الواحدة · الغابات العشوائية · التعزيز الاشتقاقي · أهمية الخصائص وحدودها | **الأشجار والتجميعات** — تجاوز خط الأساس الخطي، وسجّل الرقم الذي على الشبكة تجاوزه |
| **٢** | لماذا تفوز الشبكات العميقة أحيانًا وتخسر على البيانات الجدولية · من العصبون إلى الشبكة · دوال التنشيط · المرور الأمامي يدويًا | **المرور الأمامي بـ NumPy** — ابنِه بيدك وطابِق أرقام الشريحة |
| **٣** | دوال الخسارة · الانتشار الخلفي محسوبًا عدديًا | **الانتشار الخلفي من الصفر** — أضِف المرور الخلفي وراقب التعلّم |
| **٤** | PyTorch: التنسورات وautograd وDataLoader وحلقة التدريب | **الشبكة نفسها بـ PyTorch** — النتيجة نفسها بعُشر الشيفرة |
| **٥** | المُحسِّنات · Dropout · التطبيع الدُفعي · الإيقاف المبكر | **ضبط الشبكة** — شبكة تجارب ومعمارية نهائية تستطيع تبريرها |

**التكليف الثالث** يُطرح في اليوم الثالث، و**الثاني** يُسلَّم في اليوم الخامس، و**كرّاسة مشروع التخرّج
تُنشر في اليوم الخامس**.

</div>

---

## Why the week opens with trees

Trees and ensembles are not in the programme document. They are here, on day one of the deep-learning
week, for a reason: they are the strongest thing you can point at a table of numbers, they are what a
junior interview will ask you about, and they give this week an honest baseline.

By Thursday you will have a neural network. On Sunday you will have a gradient-boosted model. If the
network does not beat it on this data, you will know — and knowing that is worth more than a week of
being told deep learning is better.

<div dir="rtl" align="right">

## لماذا يبدأ الأسبوع بالأشجار

النماذج الشجرية غير موجودة في وثيقة البرنامج، ووجودها في أول يوم من أسبوع التعلّم العميق مقصود: هي أقوى
ما تُوجّهه إلى جدول أرقام، وهي ما تسأل عنه مقابلات الوظائف الأولى، وهي التي تمنح هذا الأسبوع خط أساس
صادقًا. بنهاية الأسبوع ستملك شبكة عصبية، وستملك نموذج تعزيز اشتقاقي. وإن لم تتجاوز الشبكة النموذج
الشجري على هذه البيانات فستعرف ذلك بنفسك — ومعرفة هذا أنفع من أسبوع من الكلام عن تفوّق التعلّم العميق.

</div>

---

## A warning about D2 and D3

These two days are the only place in the bootcamp where calculus appears, and it appears once, as
arithmetic: *if I nudge this weight by 0.01, how much does the loss move?* If you have been avoiding the
maths, these are the two days to attend awake. Everything in weeks 4 to 6 is this loop with more
parameters.

<div dir="rtl" align="right">

## تنبيه بشأن اليومين الثاني والثالث

هذان اليومان هما الموضع الوحيد في المعسكر الذي يظهر فيه التفاضل، ويظهر مرّة واحدة وبصيغة حسابية: «إن
زدت هذا الوزن بمقدار ٠٫٠١، فكم تتحرّك الخسارة؟». إن كنت تتحاشى الرياضيات فهذان يومان تحضرهما بتركيز:
كل ما في الأسابيع من الرابع إلى السادس هو هذه الحلقة نفسها بمعاملات أكثر.

</div>
