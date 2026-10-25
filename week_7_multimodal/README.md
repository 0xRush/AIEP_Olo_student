# Week 7 — Vision, Language and Speech

Every model you have met is a transformer reading tokens. This week the tokens change. Images become
patches (D1), images sit in the same space as sentences and become tokens a language model can read
(D2), and speech goes both ways — sound into text (D3) and text into sound (D4).

<div dir="rtl" align="right">

# الأسبوع السابع — الرؤية واللغة والكلام

كل نموذج قابلته حتى الآن محوّلٌ يقرأ رموزًا. وفي هذا الأسبوع تتغيّر الرموز. تصير الصور رقعًا (اليوم ١)، وتجلس الصور
في الفضاء نفسه مع الجمل وتصير رموزًا يقرؤها نموذج لغوي (اليوم ٢)، ويسير الكلام في الاتجاهين — من الصوت إلى النص
(اليوم ٣) ومن النص إلى الصوت (اليوم ٤).

</div>

---

## What you'll be able to do by the end of the week

- Find the patches, the `[CLS]` token and the attention inside a Vision Transformer, and draw what it
  looks at.
- Explain how a model learns from images with no labels (MAE, DINOv2), and judge its features with a
  linear probe.
- Search images with text using CLIP, score the search with Recall@k and MRR, and classify images with
  no training.
- Show where CLIP fails — counting, left and right, written words, Arabic — and ask a vision-language
  model instead.
- Transcribe English and Arabic speech with Whisper, implement word error rate, and measure the effect
  of noise, silence and long audio.
- Generate speech, fix the text a TTS model reads wrongly, change its voice, and score it automatically
  with a speech-to-text round trip.

<div dir="rtl" align="right">

## ما ستقدر عليه بنهاية الأسبوع

- أن تجد الرقع ورمز `[CLS]` والانتباه داخل محوّل الرؤية، وترسم ما ينظر إليه.
- أن تشرح كيف يتعلّم نموذج من الصور دون تسميات (MAE وDINOv2)، وتحكم على تمثيلاته بفحص خطي.
- أن تبحث عن الصور بالنص مستعملًا CLIP، وتقيّم البحث بـRecall@k وMRR، وتصنّف الصور دون تدريب.
- أن تُظهر أين يفشل CLIP — العدّ، واليمين واليسار، والكلمات المكتوبة، والعربية — وتسأل نموذج رؤية ولغة بدلًا منه.
- أن تُفرِّغ الكلام الإنجليزي والعربي بـWhisper، وتنفّذ معدّل خطأ الكلمات، وتقيس أثر الضجيج والصمت والصوت الطويل.
- أن تولّد كلامًا، وتُصلح النص الذي يقرؤه نموذج تحويل النص إلى كلام خطأً، وتغيّر صوته، وتقيّمه آليًا برحلة ذهاب
  وإياب عبر تحويل الكلام إلى نص.

</div>

---

## Days

| Day | Theme | Lab |
|-----|-------|-----|
| D1 | Vision transformers and self-supervised learning | `D1_vit_ssl` |
| D2 | CLIP and vision-language models | `D2_clip_vlm` |
| D3 | Speech-to-text | `D3_speech_to_text` |
| D4 | Text-to-speech | `D4_text_to_speech` |
| D5 | — | no lab |

<div dir="rtl" align="right">

| اليوم | الموضوع | المعمل |
|-----|-------|-----|
| ١ | محوّلات الرؤية والتعلّم الذاتي الإشراف | `D1_vit_ssl` |
| ٢ | CLIP ونماذج الرؤية واللغة | `D2_clip_vlm` |
| ٣ | تحويل الكلام إلى نص | `D3_speech_to_text` |
| ٤ | تحويل النص إلى كلام | `D4_text_to_speech` |
| ٥ | — | لا معمل |

</div>

Each lab has a `_blank` notebook (hints only — the full challenge) and a `_guided` notebook (most of the
code given, fill in the TODOs). Every lab runs on a laptop CPU, and opens on Colab from the badge at its
top. The first run downloads the models — about 0.5–1.6 GB per day.

<div dir="rtl" align="right">

لكل معمل دفتر `_blank` (تلميحات فقط — التحدّي الكامل) ودفتر `_guided` (معظم الشيفرة معطاة، أكمل أسطر TODO). وكل
معمل يعمل على معالج حاسوب محمول، ويُفتح على Colab من الشارة أعلاه. ويُنزّل التشغيل الأول النماذج — نحو ٠٫٥ إلى ١٫٦
جيجابايت لكل يوم.

</div>
