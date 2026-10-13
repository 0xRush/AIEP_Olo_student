# Week 5 — NLP Foundations

Language is the messiest data you will meet. This week goes from counting words to running a large language model
on your own laptop — and every step on the way is a mechanism you have computed by hand.

<div dir="rtl" align="right">

# الأسبوع الخامس — أساسيات معالجة اللغة الطبيعية

اللغة أكثر البيانات فوضى مما ستقابله. يبدأ هذا الأسبوع من عدّ الكلمات وينتهي بتشغيل
نموذج لغة كبير على حاسوبك — وكل خطوة في الطريق آلية حسبتها بيدك.

</div>

---

## What you'll be able to do by the end of the week

- Turn raw text into numbers with TF-IDF and with embeddings, measure similarity with cosine, and say
  when each representation wins.
- Compute an RNN step by hand, measure why its memory fades, and train a GRU with padding handled
  correctly.
- Build a causal, dilated convolutional network for sequences and compute exactly how far back it sees.
- Compute attention by hand on three short vectors, then assemble a transformer block and check every
  shape as it passes through.
- Run a small LLM on your own laptop: read its next-token probabilities, write the sampling that turns
  them into text, and use it to classify text with no training at all.
- Compare six kinds of model on the same data — accuracy **and** cost — and defend the one you would ship.

<div dir="rtl" align="right">

## ما ستقدر عليه بنهاية الأسبوع

- أن تُحوّل نصًا خامًا إلى أرقام بـTF-IDF وبالتضمينات، وتقيس التشابه بجيب التمام، وتقول متى يتفوّق كل تمثيل.
- أن تحسب خطوة RNN يدويًا، وتقيس لماذا تبهت ذاكرتها، وتُدرّب GRU مع معالجة الحشو صحيحًا.
- أن تبني شبكة التفافية سببية متّسعة للمتتاليات وتحسب بالضبط إلى أيّ مدى ترى إلى الوراء.
- أن تحسب الانتباه يدويًا على ثلاثة متّجهات قصيرة، ثم تُركّب كتلة محوّل وتتحقّق من كل شكل يمرّ فيها.
- أن تُشغّل نموذج لغة كبيرًا صغيرًا على حاسوبك: تقرأ احتمالات رمزه التالي، وتكتب أخذ العيّنات الذي يحوّلها إلى
  نص، وتستعمله لتصنيف النص دون أي تدريب.
- أن تقارن ستة أنواع من النماذج على البيانات نفسها — الدقّة **والكلفة** — وتدافع عن الذي كنت لتنشره.

</div>

---

## The days

| Day | Theory | Lab |
|---|---|---|
| **D1** | The NLP pipeline · TF-IDF · embeddings and cosine similarity · what Arabic breaks | **From text to vectors** — TF-IDF and sentence embeddings on the week's split; the leaderboard starts |
| **D2** | RNNs · vanishing gradients through time · LSTM and GRU gates · padding | **RNNs, LSTMs and GRUs** — one step by hand, the gradient measured, a GRU on the reviews |
| **D3** | Temporal convolutional networks · causal and dilated convolution · the receptive field | **TCNs** — compute a receptive field, prove a block is causal, a TCN on the reviews |
| **D4** | Attention · positional encoding · multi-head self-attention · the transformer block · the causal mask | **Attention and the transformer block** — by hand, then assembled, then a memory task the RNN could not reliably pass |
| **D5** | LLMs · next-token pretraining · chat templates · sampling · prompting · hallucination | **Working with an LLM** — a 0.5 B model on CPU, zero-shot on the week's data, and the verdict |

Every lab adds a row to **one leaderboard** on **one train/test split**, so by Friday six generations of
NLP are compared on the same 2,400 reviews.

**First-run downloads:** D1 `all-MiniLM-L6-v2` (~90 MB), D5 `Qwen2.5-0.5B-Instruct` (~1 GB). Download
them before class if the Wi-Fi is weak.

**Assignment 5** (TF-IDF vs BERT) is issued on D5 and due W6D3. **Capstone
M1** (data + baseline) is due on D4.

<div dir="rtl" align="right">

## الأيام

| اليوم | النظري | المعمل |
|---|---|---|
| **١** | خط معالجة اللغة · TF-IDF · التضمينات وجيب التمام · ما تكسره العربية | **من النص إلى المتّجهات** — TF-IDF وتضمينات الجمل على تقسيم الأسبوع؛ وتبدأ اللوحة |
| **٢** | الشبكات المتكرّرة · تلاشي التدرّج عبر الزمن · بوّابات LSTM وGRU · الحشو | **RNN وLSTM وGRU** — خطوة يدويًا، والتدرّج مقيسًا، وGRU على المراجعات |
| **٣** | الشبكات الالتفافية الزمنية · الالتفاف السببي والمتّسع · مجال الاستقبال | **TCN** — احسب مجال استقبال، وبرهن أن الكتلة سببية، وTCN على المراجعات |
| **٤** | الانتباه · ترميز الموضع · الانتباه الذاتي متعدّد الرؤوس · كتلة المحوّل · القناع السببي | **الانتباه وكتلة المحوّل** — يدويًا، ثم مُركَّبًا، ثم مهمة ذاكرة لم تجتزها RNN باطّراد |
| **٥** | نماذج اللغة الكبيرة · التدريب المسبق على الرمز التالي · قوالب المحادثة · أخذ العيّنات · الموجِّهات · الهلوسة | **العمل مع نموذج لغة كبير** — نموذج بنصف مليار معامل على المعالج، دون أمثلة على بيانات الأسبوع، والحكم |

كل معمل يضيف صفًا إلى **لوحة نتائج واحدة** على **تقسيم واحد** للتدريب والاختبار، فتُقارَن يوم الجمعة ستة أجيال
من معالجة اللغة على المراجعات نفسها، ٢٬٤٠٠ مراجعة.

**تنزيلات أول تشغيل:** في اليوم الأول `all-MiniLM-L6-v2` (نحو ٩٠ ميغابايت)، وفي اليوم الخامس
`Qwen2.5-0.5B-Instruct` (نحو ١ غيغابايت). نزّلها قبل الحصّة إن كانت الشبكة ضعيفة.

**التكليف الخامس** يُطرح في اليوم الخامس ويُسلَّم في الأسبوع السادس اليوم الثالث.
و**المرحلة الأولى من مشروع التخرّج** تُسلَّم في اليوم الرابع.

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
