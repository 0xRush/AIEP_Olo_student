# Week 4 — CNNs & Model Fine-Tuning

Images have spatial structure that a dense network throws away. This is the week you stop throwing it
away — and the week you learn to stand on someone else's trained model instead of starting from zero.

<div dir="rtl" align="right">

# الأسبوع الرابع — الشبكات الالتفافية وضبط النماذج

الصور تحمل بنيةً مكانية تُهدرها الشبكة الكثيفة. هذا هو الأسبوع الذي تتوقّف فيه عن إهدارها — والأسبوع
الذي تتعلّم فيه أن تقف على نموذج دُرِّب مسبقًا بدل أن تبدأ من الصفر.

</div>

---

## What you'll be able to do by the end of the week

- Compute a 2-D convolution by hand on a small grid, and predict the output size of any conv layer given
  its stride and padding — then check it by counting.
- Build and train a CNN in PyTorch, and say in one sentence why it needs far fewer parameters than a
  dense network on the same image.
- Run an object detector, read its output honestly, and **evaluate** it: IoU, non-max suppression, and
  mAP@0.5 against ground truth.
- Measure what augmentation actually bought you, instead of assuming it helped.
- Fine-tune a pretrained model on 400 images and beat what training from scratch could ever reach.

<div dir="rtl" align="right">

## ما ستقدر عليه بنهاية الأسبوع

- أن تحسب الالتفاف ثنائي الأبعاد بيدك على شبكة صغيرة، وأن تتنبّأ بحجم خرج أي طبقة التفافية بمعرفة
  الخطوة والحاشية — ثم تتحقّق بالعدّ.
- أن تبني شبكة التفافية وتُدرّبها بـ PyTorch، وأن تشرح في سطر لماذا تحتاج معاملات أقل بكثير من الشبكة
  الكثيفة على الصورة نفسها.
- أن تُشغّل كاشف كائنات وتقرأ خرجه بأمانة، وأن **تُقيّمه**: تداخل الصناديق وكبت غير الأقصى وmAP.
- أن تقيس ما أضافته زيادة البيانات فعلًا، لا أن تفترض أنها أفادت.
- أن تضبط نموذجًا مُدرَّبًا مسبقًا على ٤٠٠ صورة وتتجاوز ما يمكن أن يبلغه التدريب من الصفر أصلًا.

</div>

---

## The days

| Day | Theory | Lab |
|---|---|---|
| **D1** | Why a flattened image loses information · convolution by hand · stride · padding · output size by counting, then as a formula | **Convolution by hand** — implement it in NumPy, match the slide, then run it on a real photo and watch edges appear |
| **D2** | Pooling · channels · assembling a CNN · parameter counts · ReLU vs sigmoid in depth · the architecture lineage to ConvNeXt (~30 min) | **CNN on MNIST** — build it, train it, hit the target. Stretch: visualise the filters |
| **D3** | What a detector outputs · **IoU by hand** · non-max suppression · YOLO's one-pass idea · segmentation conceptually | **Detection with YOLO** — run it, sweep the threshold, and score it against ground truth |
| **D4** | The small-dataset problem · augmentation as free data · which augmentations are valid for which task | **Augmentation A/B** — same model, with and without; measure the gap |
| **D5** | Transfer learning · pretrained `torchvision` models · freeze/unfreeze · LR scheduling · why fine-tuning uses a small LR | **Fine-tuning ResNet-18** — 400 images, 5 classes; fine-tune vs scratch, both curves on one figure |

**Assignment 3** is due on D2. **Assignment 4** (MNIST CNN) is issued on D2 and due D5.
**Capstone proposal** is due on D4.

<div dir="rtl" align="right">

## الأيام

| اليوم | النظري | المعمل |
|---|---|---|
| **١** | لماذا تفقد الصورة المُسطّحة معلوماتها · الالتفاف يدويًا · الخطوة · الحاشية · حجم الخرج بالعدّ ثم بالمعادلة | **الالتفاف يدويًا** — نفّذه بـ NumPy وطابِق الشريحة ثم شغّله على صورة حقيقية |
| **٢** | التجميع · القنوات · تركيب الشبكة · عدد المعاملات · سلسلة المعماريات حتى ConvNeXt | **شبكة التفافية على MNIST** — ابنِها ودرّبها وحقّق الهدف |
| **٣** | ما يُخرجه الكاشف · **تداخل الصناديق يدويًا** · كبت غير الأقصى · فكرة YOLO · التقطيع مفاهيميًا | **الكشف بـ YOLO** — شغّله واكتسح العتبة وقيّمه مقابل المرجع |
| **٤** | مشكلة البيانات القليلة · زيادة البيانات · أي تحويل يصلح لأي مهمة | **مقارنة زيادة البيانات** — النموذج نفسه بها وبدونها |
| **٥** | التعلّم بالنقل · النماذج المُدرَّبة مسبقًا · التجميد وفكّه · جدولة معدّل التعلّم | **ضبط ResNet-18** — ٤٠٠ صورة وخمس فئات: الضبط مقابل التدريب من الصفر |

**التكليف الثالث** يُسلَّم في اليوم الثاني، و**الرابع** يُطرح في اليوم الثاني ويُسلَّم في الخامس.
**مقترح مشروع التخرّج** يُسلَّم في اليوم الرابع.

</div>

---

## D3 is a lab, not a slide

Object detection is often taught as a diagram of YOLO's architecture and a promise that it is fast. That
teaches nothing you can use.

On D3 you run a real detector on the same twenty photographs you convolved by hand on D1, and then you
**evaluate** it: compute IoU by hand and in code, sweep the confidence threshold and watch precision
trade against recall, switch non-max suppression off and see duplicate boxes stack up on one car, and
finally score the whole run as mAP@0.5 against hand-annotated ground truth.

Two of the twenty photos are deliberately hard. Naming *which* failure mode each one is — occlusion,
unusual angle — is part of the deliverable.

<div dir="rtl" align="right">

## اليوم الثالث معمل لا شريحة

يُدرَّس كشف الكائنات غالبًا كرسم لمعمارية YOLO ووعدٍ بأنها سريعة، وهذا لا يُعلّم شيئًا قابلًا للاستخدام.

في اليوم الثالث تُشغّل كاشفًا حقيقيًا على العشرين صورة نفسها التي طبّقت عليها الالتفاف بيدك في اليوم
الأول، ثم **تُقيّمه**: تحسب تداخل الصناديق بيدك وبالشيفرة، وتكتسح عتبة الثقة وتراقب مقايضة الدقة
والاستدعاء، وتُطفئ كبت غير الأقصى فترى الصناديق المكرّرة تتكدّس على سيارة واحدة، ثم تُقيّم التشغيل كله
بمقياس mAP مقابل مرجع مُعلَّم يدويًا. وصورتان من العشرين صعبتان عمدًا، وتحديد **نوع** الفشل في كل منهما
جزء من التسليم.

</div>

---

## Everything here runs on a laptop CPU

No lab this week needs a GPU. MNIST trains in minutes, and D5 fine-tunes 400 images with a frozen
backbone, which is cheap by design.

The one exception is D3's **stretch** section — fine-tuning a detector head — which is slow on CPU. That
notebook ships a Google Colab path and says so at the top of the section. Everything before the stretch
is CPU-only.

<div dir="rtl" align="right">

## كل ما في هذا الأسبوع يعمل على معالج حاسب محمول

لا يحتاج أي معمل هذا الأسبوع إلى معالج رسومات. الاستثناء الوحيد هو القسم الإضافي في اليوم الثالث — ضبط
رأس الكاشف — وهو بطيء على المعالج العادي، ويحتوي الدفتر مسارًا بديلًا على Google Colab مذكورًا في أول
القسم.

</div>
