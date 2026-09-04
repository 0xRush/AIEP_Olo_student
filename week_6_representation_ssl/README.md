# Week 6 — Representation Learning & Self-Supervised Models

In the real world, labels are the expensive part. This is the week you stop needing them.

<div dir="rtl" align="right">

# الأسبوع السادس — تعلّم التمثيلات والنماذج ذاتية الإشراف

في العالم الحقيقي، التسميات هي الجزء المكلف. هذا هو الأسبوع الذي تتوقّف فيه عن الحاجة إليها.

</div>

---

## What you'll be able to do by the end of the week

- Explain what a Vision Transformer does to an image, and say when you would choose it over a CNN and
  when you would not.
- Train an autoencoder and read its bottleneck as a representation rather than as a compression trick.
- Explain what a masked autoencoder learns that a classifier never does, and demonstrate it by deleting
  most of an image and getting it back.
- Evaluate a representation you cannot look at, using a linear probe — and know why that is the honest
  test.
- Search images with a sentence and sentences with an image, and explain what shared embedding space
  means.

<div dir="rtl" align="right">

## ما ستقدر عليه بنهاية الأسبوع

- أن تشرح ما يفعله محوّل الرؤية بالصورة، ومتى تختاره على الشبكة الالتفافية ومتى لا تختاره.
- أن تُدرّب مُرمِّزًا تلقائيًا وتقرأ عنق الزجاجة فيه كتمثيلٍ لا كحيلة ضغط.
- أن تشرح ما يتعلّمه المُرمِّز التلقائي المُقنَّع ولا يتعلّمه المُصنِّف، وأن تُثبته بحذف معظم الصورة
  واستعادتها.
- أن تُقيّم تمثيلًا لا تستطيع النظر إليه، بالفحص الخطي — وأن تعرف لماذا هو الاختبار الصادق.
- أن تبحث عن صور بجملة وعن جمل بصورة، وأن تشرح معنى فضاء التمثيل المشترك.

</div>

---

## The days

| Day | Theory | Lab |
|---|---|---|
| **D1** | Vision Transformer: image → patches → tokens · why the attention that read sentences reads images · ViT vs CNN, and when each wins | **ViT inference + attention maps** — run a pretrained ViT and see what its heads look at |
| **D2** | The label-scarcity problem · what self-supervised learning is · autoencoders | **Autoencoder on images** — train one, inspect the reconstructions and the bottleneck |
| **D3** | Masked autoencoders (MAE) · pretext tasks · why filling a gap teaches more than labelling | **MAE reconstruction** — mask patches and find out how much you can delete |
| **D4** | DINO and self-distillation · **linear probing** · how to evaluate a representation | **Linear probe on DINOv2** — freeze the backbone, fit a linear layer, compare against W4D5 |
| **D5** | Embeddings as the product · retrieval as the use case · CLIP and cross-modal retrieval | **Cross-modal search with CLIP** — search images with text, and find where it fails |

**Assignment 5** is due on D3. **Assignment 6** (fine-tuning on top of DINO) is issued on D4 and due
W7D2. **Capstone M2** (model + artifact) is due on D5.

<div dir="rtl" align="right">

## الأيام

| اليوم | النظري | المعمل |
|---|---|---|
| **١** | محوّل الرؤية: من الصورة إلى الرِقَع إلى الرموز · لماذا يقرأ الانتباه الصور · ViT مقابل الشبكة الالتفافية | **تشغيل ViT وخرائط الانتباه** |
| **٢** | مشكلة قِلّة التسميات · ما هو التعلّم ذاتي الإشراف · المُرمِّزات التلقائية | **مُرمِّز تلقائي على الصور** |
| **٣** | المُرمِّزات التلقائية المُقنَّعة · المهام الذريعة · لماذا يُعلّم سدّ الفراغ أكثر من التسمية | **إعادة البناء بـ MAE** |
| **٤** | DINO والتقطير الذاتي · **الفحص الخطي** · كيف تُقيّم تمثيلًا | **فحص خطي على DINOv2** |
| **٥** | التمثيلات كمنتَج · الاسترجاع كحالة استخدام · CLIP والاسترجاع متعدّد الوسائط | **البحث متعدّد الوسائط بـ CLIP** |

**التكليف الخامس** يُسلَّم في اليوم الثالث، و**السادس** يُطرح في اليوم الرابع، و**المرحلة الثانية من
مشروع التخرّج** تُسلَّم في اليوم الخامس.

</div>

---

## Why this week exists

Every model you have trained so far needed a labelled example for everything it learned. Week 4 fine-tuned
a backbone that someone else had trained on 1.2 million **hand-labelled** ImageNet photographs.

That is the expensive assumption, and it is the one that breaks first on a real project. You will have
40,000 images and 400 labels, because labelling is slow and someone has to pay for it.

This week is the answer: learn the structure of the data from the data itself, then spend your few labels
on a small layer at the very end. It is also where the last five years of the field actually went — DINO,
MAE and CLIP are not curiosities, they are what the backbones you download are now trained with.

<div dir="rtl" align="right">

## لماذا يوجد هذا الأسبوع

كل نموذج دربته حتى الآن احتاج مثالًا مُسمّى لكل ما تعلّمه، وحتى الأسبوع الرابع ضبط نموذجًا دُرِّب على
١٫٢ مليون صورة **مُسمّاة يدويًا**. وهذا هو الافتراض المكلف، وهو أول ما ينكسر في مشروع حقيقي: ستملك
٤٠٠٠٠ صورة و٤٠٠ تسمية، لأن التسمية بطيئة ومكلفة.

وهذا الأسبوع هو الجواب: تعلّم بنية البيانات من البيانات نفسها، ثم اصرف تسمياتك القليلة على طبقة صغيرة في
النهاية. وهو أيضًا حيث ذهب المجال فعلًا في السنوات الخمس الأخيرة: DINO وMAE وCLIP ليست طرائف، بل هي ما
تُدرَّب به النماذج التي تُنزّلها اليوم.

</div>

---

## This week is new

The programme document was revised and this module replaced the previous one entirely. If you are looking
for augmentation, transfer learning or model serving, they moved:

- **Augmentation and transfer learning** → week 4, days 4 and 5.
- **Model artifacts and serving** → week 8, day 1, where the capstone needs them.

<div dir="rtl" align="right">

## هذا الأسبوع جديد

عُدِّلت وثيقة البرنامج فاستبدلت هذه الوحدة الوحدة السابقة بالكامل. إن كنت تبحث عن زيادة البيانات
والتعلّم بالنقل فقد انتقلا إلى الأسبوع الرابع (اليومان الرابع والخامس)، وحفظ النموذج ونشره انتقلا إلى
الأسبوع الثامن اليوم الأول حيث يحتاجهما مشروع التخرّج.

</div>

---

## Everything still runs on a CPU

You are not pretraining DINO. You are loading a backbone somebody else pretrained and putting a linear
layer on top of it — which is cheap, and which is also exactly what you would do at work.

The autoencoder and MAE labs train small models on small images on purpose. Where a step is slow, the
notebook says how slow before you run it.

<div dir="rtl" align="right">

## كل شيء يعمل على المعالج العادي

أنت لا تُدرّب DINO من الصفر، بل تُحمّل نموذجًا دُرِّب مسبقًا وتضع طبقة خطية فوقه — وهو رخيص، وهو أيضًا ما
ستفعله في العمل. ومعامل المُرمِّز التلقائي وMAE تُدرّب نماذج صغيرة على صور صغيرة عن قصد، وحيث تكون الخطوة
بطيئة يذكر الدفتر مقدار البطء قبل أن تُشغّلها.

</div>
