# Capstone Rubric — Technical Report (12 of the 50%)

2,500–3,500 words, English or Arabic. Structure in [`report_template.md`](report_template.md).

<div dir="rtl" align="right">

# معيار تقييم التقرير التقني (١٢ من ٥٠٪)

من ٢٥٠٠ إلى ٣٥٠٠ كلمة، بالعربية أو الإنجليزية، وفق القالب.

</div>

---

## What a good report is

A record of your **judgement**, not a description of your code. The code is in the repository; the
report exists to say why it looks the way it does.

The two sections that separate a good report from an average one are **"what I tried and rejected"** and
**"limitations"** — because they are the only two that cannot be written by someone who did not do the
work.

<div dir="rtl" align="right">

## ما هو التقرير الجيّد

سجلٌّ **لأحكامك**، لا وصفٌ لشيفرتك. فالشيفرة في المستودع، والتقرير موجود ليقول لماذا هي على هذه الصورة.

والقسمان اللذان يفصلان التقرير الجيّد عن المتوسّط هما **«ما جرّبته ورفضته»** و**«الحدود»** — لأنهما
القسمان الوحيدان اللذان لا يستطيع كتابتهما من لم يقم بالعمل.

</div>

---

## Weights

| Criterion | Points |
|---|---|
| 1. Problem framing and data account | 3 |
| 2. Method and justification | 4 |
| 3. Results and error analysis | 3 |
| 4. Limitations and next steps | 2 |
| **Total** | **12** |

Writing quality is not a separate criterion. It is judged inside each one — an argument that cannot be
followed has not been made.

---

## 1. Problem framing and data account (3)

| Band | Descriptor |
|---|---|
| **Excellent** | The problem is stated in a sentence a non-specialist understands, with a clear account of who would use the output and for what decision. The data's provenance, licence, and shape are given. **At least one real problem in the data is named and its consequence explained.** |
| **Good** | Clear problem statement and data description. Problems in the data are mentioned but their consequences are not drawn out. |
| **Pass** | The problem is stated but vaguely, or in terms of the technique rather than the need ("I wanted to use BERT"). The data is described mechanically. |
| **Fail** | No clear problem. The data appears without provenance. |

---

## 2. Method and justification (4)

| Band | Descriptor |
|---|---|
| **Excellent** | Every significant choice — model, features, metric, threshold, chunk size — is explained. **At least one alternative was genuinely tried and rejected, with the evidence given.** The reader can follow the reasoning from problem to system without a gap. |
| **Good** | The main choices are explained and mostly justified. Alternatives are mentioned but not evidenced. |
| **Pass** | The method is described accurately but the choices are asserted rather than argued. Reads as a list of steps. |
| **Fail** | The method cannot be reconstructed from the report, or contradicts the code. |

**Marker prompt:** could a competent colleague rebuild this system from the report alone? At Excellent,
yes.

---

## 3. Results and error analysis (3)

| Band | Descriptor |
|---|---|
| **Excellent** | Results are reported against the baseline with the metric justified. **Error analysis identifies a pattern**, not a list — "the model fails on short reviews and on the two under-represented classes" rather than "here are ten wrong predictions". Charts are labelled, legible, and each one earns its place. |
| **Good** | Results are clear and compared to a baseline. Error analysis is concrete but does not generalise into a pattern. |
| **Pass** | Results are reported. The baseline comparison is present but thin. Error analysis is a table of failures with no interpretation. |
| **Fail** | Results without a baseline, or presented more favourably than the evidence supports. No error analysis. |

**A single number with no baseline beside it is a Pass ceiling regardless of how good the number is.**

---

## 4. Limitations and next steps (2)

| Band | Descriptor |
|---|---|
| **Excellent** | Limitations are specific and uncomfortable — the student names something that genuinely weakens their own result, and explains its effect. Next steps are concrete and prioritised, and follow from the limitations rather than being a wish list. |
| **Good** | Real limitations, stated clearly. Next steps are sensible. |
| **Pass** | Generic limitations ("more data would help", "more time would help"). Next steps are vague. |
| **Fail** | No limitations section, or it claims there are none. |

**The single best sentence a student can write in this whole report** is one that begins: *"The main
reason this result might be wrong is…"* — and then answers it honestly.

---

## Word count

2,500–3,500 words. A ±10% margin applies. Beyond that, one band is deducted from the criterion the
excess damages most — usually because padding replaces argument.

Code listings, figure captions, references, and appendices do not count.

---

## Language

English or Arabic, the student's choice. **Neither is penalised, and neither is preferred.** Terminology
should follow [`../docs/Glossary_AR_EN.md`](../docs/Glossary_AR_EN.md), with technical identifiers left
in Latin script.

<div dir="rtl" align="right">

## اللغة

بالعربية أو الإنجليزية، والخيار للطالب. **لا تُخصم درجات على أيّهما ولا تُفضَّل إحداهما.** ويُتّبع المسرد
في المصطلحات، مع إبقاء المعرّفات التقنية بالحروف اللاتينية.

</div>

---

## Marker's checklist

- [ ] Word count within range.
- [ ] The problem is stated in one comprehensible sentence.
- [ ] The data's source and licence are given.
- [ ] At least one genuine data problem is named.
- [ ] At least one rejected alternative is described with evidence.
- [ ] A baseline number appears next to the result.
- [ ] The metric choice is justified.
- [ ] Error analysis reaches a pattern.
- [ ] Limitations are specific rather than boilerplate.
- [ ] Every figure is labelled and referenced in the text.
- [ ] The report does not contradict the repository.

That last one matters. Read the evaluation code, then read the results section. A gap between them is
the single most serious finding available in this rubric.
