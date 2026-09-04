# Capstone Project Ideas

Twelve concrete starting points, four per project type. Each gives a problem, a data route, and — most
usefully — **what makes it hard**, so you can judge whether it fits five weeks.

These are starting points, not a menu. The best projects come from a student who cared about something
before the brief was issued. If you have your own idea, propose it.

<div dir="rtl" align="right">

# أفكار لمشروع التخرّج

اثنتا عشرة نقطة انطلاق ملموسة، أربع لكل نوع مشروع. لكل واحدة مسألة ومسار بيانات — والأهم: **ما الذي
يجعلها صعبة**، لتحكم بنفسك إن كانت تناسب خمسة أسابيع.

وهذه نقاط انطلاق لا قائمة اختيار. وأفضل المشاريع تأتي من طالب كان يهتم بشيء قبل صدور التكليف. فإن كانت
لديك فكرتك فاقترحها.

</div>

---

## Before you pick

**The three questions that kill bad ideas early:**

1. **Can I get the data this week?** Not "does it exist" — can *you* hold 500 rows of it by Thursday?
   If the answer involves a permission request, an NDA, or a company that has not replied, pick
   something else.
2. **What would a useful answer look like?** If you cannot say what number or output would make this
   worth deploying, you do not have a problem yet.
3. **Is there a dumb baseline?** If you cannot think of a stupid way to answer the question, you cannot
   prove your clever way is better.

**Where to look for data:** `data.gov.sa` · World Bank and GCC statistical authorities · UCI ML
Repository · Hugging Face Datasets (check the licence field) · public APIs you can call yourself ·
websites you can scrape within their terms · **data you label yourself** — 300 hand-labelled examples
you collected is a stronger foundation than 50,000 rows you downloaded.

---

## Type (a) — Predictive services on tabular data

### a1. Delivery-time estimation

**Problem.** Given an order's characteristics — distance, time of day, item count, weather — predict how
long delivery takes. Serve it as an endpoint a dispatch system could call.

**Data.** Public logistics or ride-hailing datasets, plus a weather API you join on timestamp and
location.

**What makes it hard.** The target is heavily right-skewed — most deliveries are fine and a few are
disasters, and the disasters are the ones anyone cares about. Your metric choice does most of the work
here, and MAE will hide exactly the cases that matter.

**Baseline.** The historical mean delivery time. It is better than you expect.

---

### a2. Property valuation from listings

**Problem.** Estimate a property's asking price from its attributes and location.

**Data.** Scrape a listings site within its terms of service, or use an open real-estate dataset.
Several hundred listings is enough.

**What makes it hard.** Location dominates everything and is not a number. How you encode a
neighbourhood — one-hot, target encoding, coordinates, distance to a centre — *is* the project. Listing
prices are also asking prices, not sale prices, which is a limitation you must state.

**Baseline.** The median price per square metre in the same district.

---

### a3. Equipment failure prediction

**Problem.** From sensor readings, predict whether a machine will fail in the next N hours.

**Data.** NASA turbofan degradation, the AI4I predictive-maintenance dataset, or any public sensor
time series.

**What makes it hard.** Failures are rare — often under 2% — so accuracy is useless and your entire
evaluation rests on week 2 day 5. You must also be careful that no feature encodes the future: a
maintenance-log column that only gets filled in after a failure is a leak that will give you 0.99 and
mean nothing.

**Baseline.** Always predict "no failure". It will be 98% accurate, and that is the point.

---

### a4. Energy or water demand forecasting

**Problem.** Forecast consumption for the next day or week from historical usage plus calendar and
weather features.

**Data.** Open utility datasets; several countries and cities publish hourly load data.

**What makes it hard.** It is a time series, so a random train/test split leaks the future into the
past. You must split by time and say so. Seasonality, holidays, and Ramadan effects are real signal that
a naive model misses entirely.

**Baseline.** Yesterday's value. Or the same hour last week. Both are surprisingly strong, and beating
them honestly is the whole project.

---

## Type (b) — Computer vision services

### b1. Visual quality inspection

**Problem.** Classify product photos as acceptable or defective, served as an endpoint a QA station
could call.

**Data.** MVTec AD, or a set you photograph yourself — 300 images across a few defect types is plenty.

**What makes it hard.** Defects are rare and varied, and you will not have many examples of each. This
is week 4 days 4 and 5 in their purest form: augmentation and transfer learning are not optional here, they are the
project.

**Baseline.** Always predict "acceptable".

---

### b2. Document type classification

**Problem.** Given a scanned page, classify it — invoice, contract, ID, form — so it can be routed
automatically.

**Data.** RVL-CDIP, or a set you assemble from public document templates.

**What makes it hard.** Documents look similar at low resolution and differ in fine detail. Also
genuinely useful: this is a real problem that real organisations pay to solve, which makes it a good
portfolio piece.

**Baseline.** The most common class.

---

### b3. Arabic handwriting or sign classification

**Problem.** Classify handwritten Arabic characters, digits, or road-sign images.

**Data.** AHCD (Arabic Handwritten Characters), or photograph signs yourself.

**What makes it hard.** Arabic letters change form by position, and several are distinguished only by
dots. Your confusion matrix will be interesting and your error analysis will almost write itself —
which is a good thing. **Beware augmentation**: horizontal flips are invalid here and will silently
poison your training set.

**Baseline.** Random, or the most common class.

---

### b4. Plant disease or crop-condition detection

**Problem.** Classify a leaf photo by disease, with a confidence, served behind an endpoint a farmer
could use from a phone.

**Data.** PlantVillage, or images you collect.

**What makes it hard.** The public datasets are photographed in controlled conditions, and real phone
photos are not — different lighting, backgrounds, and angles. **Test your model on a photo you take
yourself**, and report what happens. That gap between benchmark and reality is the most valuable finding
you can produce.

**Baseline.** Most common class.

---

## Type (c) — NLP: search, RAG, and recommenders

### c1. A RAG assistant over documents that matter to you

**Problem.** A question-answering assistant over a document collection — university regulations, a
technical manual set, government service documentation, internal policies you have permission to use.

**Data.** The documents themselves. Twenty to a hundred is plenty.

**What makes it hard.** **Evaluation.** "It seems to work" is not a result. You need an evaluation set
with known answers and known sources, and you must measure retrieval separately from generation — week 7
day 2 exists for this. Also: your system must refuse questions the documents cannot answer, and most
student RAG systems answer everything.

**Baseline.** Keyword search over the same documents. It is a real competitor and beats naive vector
search more often than people expect.

---

### c2. Semantic search over a corpus you assembled

**Problem.** Search a specialised collection — job postings, research abstracts, product listings — by
meaning rather than keyword.

**Data.** Scrape or collect it yourself.

**What makes it hard.** Chunking decides your quality, and you will only discover that by measuring
three chunk sizes. You also need relevance judgements to evaluate anything at all — which means
hand-labelling 30 or so query-document pairs. That labelling is not overhead; it is the project.

**Baseline.** BM25 or TF-IDF search.

---

### c3. A content-based recommender for a catalogue

**Problem.** Given something a user liked, recommend similar items from a catalogue you scraped —
books, courses, films, restaurants.

**Data.** Scrape a catalogue with descriptions. A few thousand items.

**What makes it hard.** With no interaction data you cannot use collaborative filtering, so cold start
is your whole world. Evaluation requires you to define what "relevant" means — and you choose that
definition, which means every number you report depends on a judgement you must defend.

**Baseline.** Recommend the most popular items. It is embarrassingly hard to beat.

---

### c4. Support-ticket triage

**Problem.** Classify incoming text — support tickets, complaints, reviews — by category and urgency, and
route them.

**Data.** Public support or complaint datasets; the US CFPB consumer-complaint database is large,
public, and genuinely messy.

**What makes it hard.** Categories overlap and the labels are inconsistent because humans assigned them.
Urgency is subjective. This is a good project for the week-5 comparison: TF-IDF against a fine-tuned
transformer, on cost as well as accuracy, since a triage system runs on every ticket.

**Baseline.** TF-IDF plus logistic regression. Make your transformer earn its cost.

---

### c5. Cross-modal search over a catalogue you assembled

**Problem.** Search a set of images with a sentence — "a red leather chair", "a page with a table on it"
— using CLIP, with no labels at all.

**Data.** A few thousand images with short captions or titles. A product catalogue, a photo archive, a
scanned document set.

**What makes it hard.** Everything rests on the honesty of your evaluation, because a cross-modal demo
looks impressive while being wrong. You must build a query set with known-correct answers and report
Recall@k in **both** directions — text→image and image→text are not equally good, and the gap is
interesting. Week 6 day 5's failure taxonomy is your starting point: counting, spatial relations, text
inside images, and anything culturally under-represented in web data, which explicitly includes much
Arabic content.

**Baseline.** Keyword search over the captions. On short, well-written captions it is genuinely hard to
beat, and finding out where CLIP wins is the project.

---

### c6. A visual classifier built from 200 labels

**Problem.** A classification task where labelling is the bottleneck — a domain you have images of and
almost no labels for. Label 200 of them and get a usable model.

**Data.** Your own images, or a public set whose labels you deliberately throw away and re-label a
fraction of.

**What makes it hard.** This is week 6 as an engineering problem rather than a lecture. Frozen DINOv2
features plus a linear probe is your first model, and it should be running within a day. The project is
then the label-efficiency curve: accuracy against label count at 10, 25, 50, 100, 200. That curve is
your result, and it is a far more interesting deliverable than one accuracy number.

**Baseline.** Two of them, and you need both: the majority class, and a from-scratch CNN on the same 200
labels. The second one is the number that shows what the pretrained representation was worth.

---

## Ideas to avoid

Not because they are bad problems, but because they do not fit five weeks or do not exercise what this
course taught.

| Idea | Why not |
|---|---|
| Stock price prediction | The efficient-market problem means your model will not beat a random walk, and you will spend five weeks discovering that. If you want financial data, forecast something else — volume, volatility, sentiment. |
| A general-purpose chatbot | Not a scoped problem, and there is nothing to evaluate. A **domain-specific RAG assistant** is the version of this that works. |
| Retraining a large language model | You do not have the compute, and it is not what the course taught. Fine-tuning a small model is fine. |
| Anything on a clean Kaggle competition dataset | Requirement 1 excludes it. The mess is the point. |
| A dataset behind a permission request you have not received | If the data does not arrive in week 5, you have no project. Have a backup or pick something else. |
| A project that needs you to pretrain a self-supervised model from scratch | Week 6 shows you why: DINO and MAE were trained at a scale nobody in this room can reproduce. Use a pretrained backbone and spend your effort on the head. |

<div dir="rtl" align="right">

## أفكار يُنصح بتجنّبها

**التنبّؤ بأسعار الأسهم** — كفاءة السوق تعني أن نموذجك لن يتفوّق على المسار العشوائي، وستمضي خمسة أسابيع
لتكتشف ذلك. **روبوت محادثة عام** — ليس مسألة محدّدة ولا شيء فيه للتقييم، والبديل الناجح هو مساعد RAG
متخصّص. **إعادة تدريب نموذج لغوي كبير** — لا تملك العتاد وليس هذا ما دُرّس. **أي مجموعة بيانات مسابقة
نظيفة** — المتطلّب الأول يستبعدها، فالفوضى هي المقصودة. **بيانات تنتظر إذنًا لم يصلك** — إن لم تصل في
الأسبوع الخامس فلا مشروع لديك.

</div>

---

## Still stuck?

Answer these three, in order, and a project usually falls out:

1. What is something you or someone you know spends time on that a computer could estimate or find
   faster?
2. What data would that need, and can you get 500 rows of it this week?
3. What is the stupidest possible way to answer the question? That is your baseline, and if your
   clever method cannot beat it, that is a finding worth reporting too.

Then talk to an instructor **before** you write the proposal. Ten minutes of conversation in week 4
saves a fortnight in week 6.

<div dir="rtl" align="right">

## ما زلت متردّدًا؟

أجب عن هذه الثلاثة بالترتيب فيظهر المشروع عادةً: ما الشيء الذي تقضي فيه — أو يقضي فيه من تعرف — وقتًا
ويستطيع الحاسوب تقديره أو إيجاده أسرع؟ وما البيانات اللازمة لذلك، وهل تستطيع الحصول على ٥٠٠ صفٍّ منها هذا
الأسبوع؟ وما أغبى طريقة ممكنة للإجابة عن السؤال؟ — تلك هي خط أساسك، وإن عجزت طريقتك الذكية عن تجاوزه فتلك
نتيجة تستحق التقرير أيضًا.

ثم تحدّث مع مدرّب **قبل** كتابة المقترح. فعشر دقائق حوار في الأسبوع الرابع توفّر أسبوعين في السادس.

</div>
