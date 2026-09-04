# Week 7 — RAG & Recommendation Systems

Large language models make things up when asked about facts they were never trained on. This is the week
you ground them in a knowledge base — and then use the same retrieval machinery to build a recommender.

<div dir="rtl" align="right">

# الأسبوع السابع — التوليد المُعزَّز بالاسترجاع وأنظمة التوصية

النماذج اللغوية الضخمة تختلق الإجابات حين تُسأل عن وقائع لم تُدرَّب عليها. هذا هو الأسبوع الذي تُسنِدها فيه
إلى قاعدة معرفة — ثم تستخدم آلية الاسترجاع نفسها لبناء نظام توصية.

</div>

---

## What you'll be able to do by the end of the week

- Explain exactly why a standalone LLM hallucinates, and demonstrate it on a corpus it has never seen.
- Chunk documents three different ways and measure which questions each strategy can and cannot answer.
- Stand up a vector database, index a corpus, and explain what approximate nearest-neighbour search
  trades away for speed.
- Build a full RAG pipeline that answers only from its sources, cites them, and **refuses** when the
  answer is not there.
- Evaluate a RAG system on faithfulness, answer relevance and context recall — and understand why a system
  answering every question scores worse than one that declines.
- Build both a collaborative and a content-based recommender on the same data and compare them with
  precision@k and NDCG.

<div dir="rtl" align="right">

## ما ستقدر عليه بنهاية الأسبوع

- أن تشرح بدقة لماذا يهلوس النموذج اللغوي وحده، وأن تُثبته على مُدوّنة لم يرها قط.
- أن تُقطّع الوثائق بثلاث طرق وتقيس أي الأسئلة يستطيع كل تقطيع الإجابة عنها.
- أن تُشغّل قاعدة متّجهات وتُفهرس مُدوّنة، وأن تشرح ما يتنازل عنه البحث التقريبي مقابل السرعة.
- أن تبني خط RAG كاملًا يجيب من مصادره فقط ويستشهد بها **ويرفض** حين لا تكون الإجابة موجودة.
- أن تُقيّم النظام بمقاييس الأمانة للمصدر وصلة الإجابة واستدعاء السياق — وأن تفهم لماذا يكون النظام الذي
  يجيب عن كل شيء أسوأ من الذي يعتذر.
- أن تبني نظام توصية تعاونيًا وآخر قائمًا على المحتوى على البيانات نفسها وتقارنهما.

</div>

---

## The days

| Day | Theory | Lab |
|---|---|---|
| **D1** | Why standalone LLMs hallucinate · knowledge cutoff · the RAG architecture · chunking strategies and what each one breaks | **Chunking & retrieval quality** — chunk one corpus three ways, measure which questions each can answer |
| **D2** | Embedding models for retrieval · vector databases · approximate nearest-neighbour search · Chroma and FAISS locally, Pinecone in the cloud | **Build the vector index** — ingest, embed, store, query, and read the top-k critically |
| **D3** | The full pipeline · context injection · citation prompting · query reformulation · making a system refuse | **Build a RAG assistant** — answers only from the documents, cites them, declines otherwise |
| **D4** | Evaluating RAG: faithfulness, answer relevance, context recall · failure modes · hybrid retrieval | **Evaluate your RAG** — 40 questions, 10 deliberately unanswerable |
| **D5** | Recommenders: collaborative vs content-based vs hybrid · cold start · embeddings in recommenders · precision@k, recall@k, NDCG, MAP · applied-NLP survey | **Semantic search + embedding recommender** — measured against a collaborative baseline |

**Assignment 6** is due on D2. **Assignment 7** (RAG chatbot) is issued on D3 and due D5.
**Capstone M3** (pipeline + serving) is due on D4.

<div dir="rtl" align="right">

## الأيام

| اليوم | النظري | المعمل |
|---|---|---|
| **١** | لماذا تهلوس النماذج · حدّ المعرفة · معمارية RAG · استراتيجيات التقطيع | **التقطيع وجودة الاسترجاع** |
| **٢** | نماذج التمثيل للاسترجاع · قواعد المتّجهات · البحث التقريبي · Chroma وFAISS وPinecone | **بناء فهرس المتّجهات** |
| **٣** | الخط الكامل · إدخال السياق · الاستشهاد · إعادة صياغة الاستعلام · الرفض | **بناء مساعد RAG** |
| **٤** | تقييم RAG: الأمانة للمصدر وصلة الإجابة واستدعاء السياق · أنماط الفشل · الاسترجاع الهجين | **تقييم نظامك** |
| **٥** | أنظمة التوصية: التعاوني والقائم على المحتوى والهجين · البداية الباردة · المقاييس · مسح تطبيقات اللغة | **البحث الدلالي ونظام التوصية** |

**التكليف السادس** يُسلَّم في اليوم الثاني، و**السابع** يُطرح في اليوم الثالث ويُسلَّم في الخامس.
**المرحلة الثالثة من مشروع التخرّج** تُسلَّم في اليوم الرابع.

</div>

---

## This week carries two modules

Weeks 1 to 6 each delivered one module of the programme. This week delivers **two**: retrieval-augmented
generation and recommendation systems.

That is not a squeeze. Recommenders run on exactly the machinery RAG builds — embeddings from week 6, a
vector index from D2, and similarity search. By D5 the infrastructure already exists, so the session is
about the *ideas specific to recommendation* — collaborative filtering, cold start, ranking metrics —
rather than about plumbing you have already built twice.

Merging them is also what frees week 8 entirely for the capstone, which is where you will want the time.

<div dir="rtl" align="right">

## هذا الأسبوع يحمل وحدتين

كل أسبوع من الأول إلى السادس قدّم وحدة واحدة، وهذا الأسبوع يقدّم **وحدتين**: التوليد المُعزَّز بالاسترجاع
وأنظمة التوصية. وهذا ليس ضغطًا: فأنظمة التوصية تعمل على الآلية نفسها التي يبنيها RAG — تمثيلات الأسبوع
السادس وفهرس المتّجهات من اليوم الثاني وبحث التشابه. فبحلول اليوم الخامس تكون البنية جاهزة، وتصير الجلسة
عن **الأفكار الخاصة بالتوصية** لا عن أنابيب بنيتها مرّتين. ودمجهما هو أيضًا ما يُفرغ الأسبوع الثامن كاملًا
لمشروع التخرّج.

</div>

---

## The most important idea of the week

**A system that answers every question is worse than one that declines.**

The evaluation set on D4 has 40 questions, and 10 of them cannot be answered from the documents. A model
that produces a confident answer for all 40 scores lower than one that refuses those 10 — because in a
real deployment, a confident wrong answer about a company policy is the failure that gets the project
cancelled.

Refusing correctly is a skill, it is measurable, and it is what separates a demo from a system.

<div dir="rtl" align="right">

## أهم فكرة في هذا الأسبوع

**النظام الذي يجيب عن كل سؤال أسوأ من الذي يعتذر.**

مجموعة التقييم في اليوم الرابع فيها أربعون سؤالًا، عشرة منها لا يمكن الإجابة عنها من الوثائق. والنموذج
الذي يُنتج إجابة واثقة عن الأربعين جميعًا يحصل على نتيجة أدنى من الذي يرفض تلك العشرة — لأن الإجابة
الواثقة الخاطئة عن سياسة شركة هي الخطأ الذي يُلغي المشروع في الواقع. والرفض في موضعه مهارة، وقابل للقياس،
وهو ما يفرّق بين العرض التوضيحي والنظام.

</div>

---

## You need an API key

D3 onwards calls a language model. The course uses **OpenRouter**, which is OpenAI-SDK-compatible and has
free model slugs, so no payment method is required. Setup instructions:
[`../docs/Data_Guide.md`](../docs/Data_Guide.md).

Put the key in `.env`. Never commit it, and never paste it into a notebook cell.

<div dir="rtl" align="right">

## تحتاج مفتاح واجهة برمجية

من اليوم الثالث فصاعدًا تُستدعى نماذج لغوية. يستخدم المقرّر **OpenRouter** المتوافق مع واجهة OpenAI وفيه
نماذج مجانية، فلا حاجة إلى وسيلة دفع. ضع المفتاح في ملف `.env`، ولا تُضِفه إلى git ولا تكتبه داخل خلية في
الدفتر.

</div>
