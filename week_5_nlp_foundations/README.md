# Week 5 — NLP Foundations

Language is the messiest data you will meet. This week goes from counting words to the architecture that
powers every large language model — and every step is a mechanism you have computed by hand.

<div dir="rtl" align="right">

# الأسبوع الخامس — أساسيات معالجة اللغة الطبيعية

اللغة أكثر البيانات فوضى مما ستقابله. يبدأ هذا الأسبوع من عدّ الكلمات وينتهي بالمعمارية التي تقوم عليها
كل النماذج اللغوية الضخمة — وكل خطوة فيه آلية حسبتها بيدك.

</div>

---

## What you'll be able to do by the end of the week

- Turn raw text into numbers with TF-IDF, and say precisely what that representation throws away.
- Explain what an embedding is, measure similarity with cosine, and demonstrate one bias the embedding
  inherited from its training data.
- Compute attention by hand on three short vectors — three dot products, a softmax, one weighted sum —
  and then find the same numbers in a library.
- Assemble a transformer block and check every shape as it passes through.
- Fine-tune BERT on a real classification task and compare it honestly against a TF-IDF baseline,
  including the cost.

<div dir="rtl" align="right">

## ما ستقدر عليه بنهاية الأسبوع

- أن تُحوّل نصًا خامًا إلى أرقام بـ TF-IDF، وأن تُحدّد بدقة ما يُهدره هذا التمثيل.
- أن تشرح ما هو التمثيل المتّجهي، وأن تقيس التشابه بجيب التمام، وأن تُظهر تحيّزًا واحدًا ورثه التمثيل من
  بيانات تدريبه.
- أن تحسب آلية الانتباه بيدك على ثلاثة متّجهات قصيرة — ثلاثة جداءات نقطية وsoftmax ومجموع موزون — ثم
  تجد الأرقام نفسها في مكتبة.
- أن تُركّب كتلة محوّل وتتحقّق من كل شكل يمرّ فيها.
- أن تضبط BERT على مهمة تصنيف حقيقية وتقارنه بأمانة بخط أساس TF-IDF، مع حساب التكلفة.

</div>

---

## The days

| Day | Theory | Lab |
|---|---|---|
| **D1** | The NLP pipeline: tokenisation, normalisation, stopwords, stemming vs lemmatisation · TF-IDF · what Arabic breaks | **Classical text classification** — TF-IDF + logistic regression; inspect the most predictive terms |
| **D2** | Word and sentence embeddings · the embedding space · cosine similarity · what embeddings inherit | **Exploring embedding space** — similarity, nearest neighbours, a PCA view, and one bias you can show |
| **D3** | Why sequences are hard · RNN/LSTM and exactly where they break · attention as the fix, by hand | **Attention by hand** — three vectors, three dot products, one weighted sum |
| **D4** | The Transformer: positional encoding · multi-head self-attention · encoder / decoder | **Build a transformer block** — assemble it from yesterday's attention, check every shape |
| **D5** | How BERT and GPT are pretrained · Hugging Face pipelines · a survey of applied NLP tasks | **Fine-tuning BERT** — one epoch on CPU, compared against D1's baseline |

**Assignment 5** (TF-IDF vs BERT) is issued on D5 and due W6D3. **Capstone M1** (data + baseline) is due
on D4.

<div dir="rtl" align="right">

## الأيام

| اليوم | النظري | المعمل |
|---|---|---|
| **١** | خط معالجة اللغة: التقطيع والتطبيع وكلمات الوقف والتجذيع مقابل التأصيل · TF-IDF · ما تكسره العربية | **التصنيف النصي الكلاسيكي** — TF-IDF مع الانحدار اللوجستي |
| **٢** | التمثيلات المتّجهية للكلمات والجمل · فضاء التمثيل · جيب التمام · ما ترثه التمثيلات | **استكشاف فضاء التمثيل** — التشابه والجيران والتحيّز |
| **٣** | لماذا التسلسلات صعبة · حدود RNN وLSTM · الانتباه كحلّ، يدويًا | **الانتباه يدويًا** — ثلاثة متّجهات ومجموع موزون |
| **٤** | المحوّل: الترميز الموضعي · الانتباه الذاتي متعدّد الرؤوس · المُرمِّز والمُفكِّك | **بناء كتلة محوّل** — ركّبها وتحقّق من كل شكل |
| **٥** | كيف يُدرَّب BERT وGPT · Hugging Face · مسح لتطبيقات اللغة | **ضبط BERT** — دورة واحدة على المعالج، مقارنةً بخط الأساس |

**التكليف الخامس** يُطرح في اليوم الخامس، و**المرحلة الأولى من مشروع التخرّج** تُسلَّم في اليوم الرابع.

</div>

---

## What is not here, and why

The programme document was revised, and two things were removed. Do not go looking for them:

- **Bag-of-Words and n-grams.** TF-IDF alone carries the classical representation, and it carries it
  better — it already contains the counting idea, plus the weighting that makes counting useful.
- **Word2Vec, GloVe and FastText.** Embeddings are taught with the sentence-transformer models you would
  actually reach for today. The *concepts* — embedding space, cosine similarity, semantic arithmetic —
  are all still on D2, and they are what transfers.

If you have read an older syllabus, this is the difference.

<div dir="rtl" align="right">

## ما ليس موجودًا هنا ولماذا

عُدِّلت وثيقة البرنامج فحُذف شيئان: **حزمة الكلمات وn-grams** — إذ يكفي TF-IDF وحده لتمثيل الطريقة
الكلاسيكية بل ويؤدّيها أفضل، لأنه يحتوي فكرة العدّ أصلًا مع الوزن الذي يجعل العدّ مفيدًا. و**Word2Vec
وGloVe وFastText** — إذ تُدرَّس التمثيلات بالنماذج التي تستخدمها فعلًا اليوم، أما المفاهيم — فضاء
التمثيل وجيب التمام والحساب الدلالي — فكلها باقية في اليوم الثاني، وهي ما ينتقل معك.

</div>

---

## A note on Arabic

Most NLP tooling was built for English and quietly assumes it. Arabic breaks the assumptions in specific
ways: the letters join, diacritics are usually absent, the same word appears with and without
prefixes, and normalisation choices (أ / ا / إ, ة / ه, ى / ي) change your vocabulary size before you
have trained anything.

D1 covers this properly rather than as a footnote, because a graduate of this bootcamp in this region
will be asked to process Arabic text.

<div dir="rtl" align="right">

## ملاحظة عن العربية

بُنيت معظم أدوات معالجة اللغة للإنجليزية وتفترضها ضمنًا. والعربية تكسر تلك الافتراضات بطرق محدّدة:
الحروف متّصلة، والتشكيل غائب عادةً، والكلمة نفسها تظهر بالسوابق وبدونها، وخيارات التطبيع (أ/ا/إ، ة/ه،
ى/ي) تُغيّر حجم المعجم قبل أن تُدرّب أي شيء. ويُعالج اليوم الأول هذا الأمر معالجةً كاملة لا كهامش، لأن
من يتخرّج من هذا المعسكر في هذه المنطقة سيُطلب منه معالجة نص عربي.

</div>
