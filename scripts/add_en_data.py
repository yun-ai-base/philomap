import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('D:/applications/AI_files/philomap/data/philosophers.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# English data for all philosophers
# Stored as { philosopher_id: { field: value } }
# Only includes fields where English differs from or supplements Chinese
EN = {
    # ===== ORIGINAL 30 =====
    "thales": {
        "summaryEn": "Thales of Miletus is widely regarded as the first philosopher in Western history. He rejected mythological explanations and sought the fundamental principle (arche) of the universe in natural terms, declaring that 'everything is water.' He was also a mathematician, astronomer, and statesman.",
        "goldenQuotesEn": [{"text":"Water is the principle of all things.","source":"Aristotle, Metaphysics"},{"text":"All things are full of gods.","source":"Aristotle, On the Soul"}],
        "coreThoughtsEn": [
            {"concept":"Water as Arche","desc":"Thales believed water is the fundamental substance from which everything comes and to which everything returns.","l1":"Everything in the world is made of water in different forms.","l2":"Like ice, liquid, and steam — all are water in different states.","l3":"Thales chose water because it can take solid, liquid, and gaseous forms, making it the most versatile substance."},
            {"concept":"Natural Explanation","desc":"He was the first to explain natural phenomena without reference to mythology or divine intervention.","l1":"Instead of saying 'the gods caused it,' Thales looked for natural causes.","l2":"Like a detective who looks for evidence instead of blaming ghosts.","l3":"This shift from mythos to logos is considered the beginning of Western philosophy and science."}
        ]
    },
    "pythagoras": {
        "summaryEn":"Pythagoras founded a religious-philosophical community in southern Italy that profoundly influenced Western thought. He believed that 'all is number' — that the ultimate nature of reality is mathematical. He made major contributions to mathematics, music theory, and astronomy.",
        "goldenQuotesEn":[{"text":"All is number.","source":"Pythagorean doctrine"},{"text":"Number rules the universe.","source":"Pythagorean saying"}],
        "coreThoughtsEn":[
            {"concept":"All is Number","desc":"The universe is fundamentally mathematical — numbers are the ultimate reality behind all phenomena.","l1":"Everything in the world can be understood through numbers and their relationships.","l2":"Like how music can be described by mathematical ratios of notes.","l3":"Pythagoras discovered that musical harmony depends on numerical ratios, leading him to believe numbers are the true substance of reality."},
            {"concept":"Transmigration of Souls","desc":"The soul is immortal and undergoes a cycle of rebirths into different life forms until it achieves purification.","l1":"Your soul lives on after death and can be reborn in another body.","l2":"Like a caterpillar becoming a butterfly — the soul transforms and continues.","l3":"Pythagoras believed in metempsychosis (reincarnation) and that animals could host human souls, which led to vegetarianism in his community."}
        ]
    },
    "heraclitus": {
        "summaryEn":"Heraclitus of Ephesus is known for his doctrine of universal flux — 'everything flows' (panta rhei). He believed that change is the fundamental nature of the universe and that strife/opposition is the driving force behind all existence. His obscure, aphoristic style earned him the nickname 'the Obscure.'",
        "goldenQuotesEn":[{"text":"No man ever steps in the same river twice.","source":"Heraclitus, Fragments"},{"text":"The way up and the way down are one and the same.","source":"Heraclitus, Fragments"}],
        "coreThoughtsEn":[
            {"concept":"Panta Rhei (Everything Flows)","desc":"Change is the fundamental nature of the universe — everything is in a constant state of flux.","l1":"Nothing stays the same — everything is constantly changing.","l2":"Like a river that appears the same but is always new water flowing through.","l3":"Heraclitus' famous river fragment expresses both the reality of change and the illusion of stability — even as we perceive something as 'the same,' it has already changed."},
            {"concept":"Unity of Opposites","desc":"Opposites are not in conflict but are necessary aspects of a deeper unity — tension creates harmony.","l1":"Day and night, hot and cold, life and death — they define each other.","l2":"Like a bow that only works because of the tension between its string and frame.","l3":"The harmony of the cosmos is a 'hidden harmony' that emerges from the tension of opposites — war is the father of all things."}
        ]
    },
    "parmenides": {
        "summaryEn":"Parmenides of Elea is the founder of ontology and one of the most influential pre-Socratic philosophers. He argued that 'what is' (Being) is eternal, unchanging, and one — and that change and multiplicity are illusions of the senses. His logical arguments set the agenda for metaphysics for centuries.",
        "goldenQuotesEn":[{"text":"What is, is; what is not, is not.","source":"Parmenides, On Nature"},{"text":"Thought and being are the same.","source":"Parmenides, Fragment 3"}],
        "coreThoughtsEn":[
            {"concept":"The Way of Truth","desc":"True reality is eternal, unchanging, indivisible, and motionless — change and plurality are mere appearances.","l1":"The real world doesn't change — change is just an illusion of our senses.","l2":"Like how a movie appears to move but is actually a sequence of still frames.","l3":"Parmenides' logical argument: if something comes into being, it must come either from what is or what is not. From what is not is impossible. From what is would mean it already exists. Therefore nothing truly comes into being."},
            {"concept":"Being vs. Becoming","desc":"Parmenides drew a sharp distinction between the rational realm of Being (true reality) and the sensory realm of Becoming (mere appearance).","l1":"What our mind understands is real; what our senses perceive is unreliable.","l2":"Like knowing that the earth is round (mind) even though it looks flat (senses).","l3":"This distinction between Being and Becoming became foundational for Plato's theory of Forms and all subsequent Western metaphysics."}
        ]
    },
    "democritus": {
        "summaryEn":"Democritus is the father of atomism — the theory that everything in the universe is composed of indestructible atoms moving in empty space (void). He developed a comprehensive materialist philosophy that explained sensation, thought, and even the soul in purely physical terms.",
        "goldenQuotesEn":[{"text":"Nothing exists except atoms and empty space; everything else is opinion.","source":"Democritus, Fragments"},{"text":"Happiness resides not in possessions and not in gold, but in the soul.","source":"Democritus, Fragments"}],
        "coreThoughtsEn":[
            {"concept":"Atomism","desc":"All reality consists of indivisible atoms (atomos) moving in the void — their combinations and separations explain all phenomena.","l1":"Everything is made of tiny, indestructible particles moving in empty space.","l2":"Like Lego bricks — different shapes and arrangements of the same basic pieces create everything.","l3":"Democritus proposed that atoms are eternal, indestructible, and infinite in number. They differ in shape, size, and arrangement, which explains the diversity of phenomena we observe."},
            {"concept":"Mechanical Universe","desc":"All phenomena, including thought and perception, can be explained by the mechanical motion of atoms — no purpose or design needed.","l1":"Everything happens because atoms bump into each other — there's no hidden purpose.","l2":"Like billiard balls colliding — all events are just physical interactions.","l3":"Democritus' strict materialism anticipates modern scientific determinism: if everything is atoms in motion, then everything, including human decisions, follows from physical law."}
        ]
    },
    "socrates": {
        "summaryEn":"Socrates of Athens is the founding figure of Western moral philosophy. He wrote nothing himself, but his method of questioning — the Socratic method — became the foundation of critical thinking. He was famously ugly, immensely charismatic, and ultimately executed by drinking hemlock for 'corrupting the youth' and 'impiety.' His relentless pursuit of truth through dialogue made him one of history's most iconic thinkers.",
        "goldenQuotesEn":[{"text":"The unexamined life is not worth living.","source":"Plato, Apology"},{"text":"I know that I am intelligent, because I know that I know nothing.","source":"Plato, Apology"}],
        "coreThoughtsEn":[
            {"concept":"Socratic Method","desc":"Knowledge is pursued through systematic questioning that exposes contradictions in beliefs, leading to clearer understanding.","l1":"Asking 'why' repeatedly until you get to the fundamental truth of something.","l2":"Like peeling an onion layer by layer — each question removes another layer of assumption.","l3":"The elenchus (cross-examination) is Socrates' method: ask for a definition, find counterexamples, refine the definition, repeat until a contradiction-free understanding emerges."},
            {"concept":"Know Thyself","desc":"True wisdom begins with recognizing the limits of one's own knowledge — intellectual humility is the foundation of philosophy.","l1":"The smartest thing you can admit is that you don't know everything.","l2":"Like a map that shows both what you know and the vast unknown territory.","l3":"Socrates was declared the wisest man in Athens by the Oracle of Delphi precisely because he alone recognized his own ignorance — the beginning of wisdom is acknowledging what you don't know."}
        ]
    },
    "plato": {
        "summaryEn":"Plato is one of the most influential philosophers in history. A student of Socrates and teacher of Aristotle, he founded the Academy in Athens. His Theory of Forms — the idea that the physical world is a shadow of a higher, eternal reality — shaped Western philosophy, theology, and science for over two millennia. His dialogues are both philosophical masterpieces and literary classics.",
        "goldenQuotesEn":[{"text":"The greatest wealth is to live content with little.","source":"Plato"},{"text":"Reality is created by the mind; we can change our reality by changing our mind.","source":"Attributed to Plato"}],
        "coreThoughtsEn":[
            {"concept":"Theory of Forms","desc":"True reality is not the physical world we perceive but an eternal, unchanging realm of perfect Forms — the physical world is just a shadow.","l1":"What we see around us are just imperfect copies of perfect, invisible originals.","l2":"Like shadows on a cave wall — they're not the real things, just projections.","l3":"The Allegory of the Cave: prisoners see only shadows on a wall and think that's reality. The philosopher is the one who escapes the cave, sees the real world (the Forms), and returns to help others see it too."},
            {"concept":"Philosopher-King","desc":"The ideal ruler is a philosopher — one who knows the Form of the Good and can govern with wisdom rather than self-interest.","l1":"The best leaders are those who seek truth and wisdom, not power or money.","l2":"Like a ship captain who must understand navigation, a ruler must understand the Good.","l3":"Plato's political philosophy: only those who have contemplated the Forms, especially the Form of the Good, are fit to rule. This is because they will govern based on knowledge, not opinion."}
        ]
    },
    "aristotle": {
        "summaryEn":"Aristotle was a Greek philosopher and polymath, a student of Plato and tutor to Alexander the Great. He founded the Lyceum and wrote on everything from logic and metaphysics to biology and poetry. His system of logic dominated Western thought for two millennia. His ethics of virtue and the Golden Mean, his political theory, and his metaphysics of substance and accident remain foundational to Western philosophy.",
        "goldenQuotesEn":[{"text":"We are what we repeatedly do. Excellence, then, is not an act but a habit.","source":"Aristotle, Nicomachean Ethics"},{"text":"The whole is greater than the sum of its parts.","source":"Aristotle, Metaphysics"}],
        "coreThoughtsEn":[
            {"concept":"Virtue Ethics","desc":"Moral excellence is achieved by practicing virtues — habits of character that lie at the Golden Mean between extremes.","l1":"Being a good person means developing good habits and finding balance in everything.","l2":"Like goldilocks — not too much courage (rashness), not too little (cowardice), but just right.","l3":"The Golden Mean is not mediocrity but the precise balance appropriate to each situation: courage is the mean between cowardice and recklessness, generosity between stinginess and wastefulness."},
            {"concept":"Four Causes","desc":"To fully understand something, you need to know four aspects: material cause (what it's made of), formal cause (what it is), efficient cause (how it was made), and final cause (what it's for).","l1":"There are four different ways to answer 'why' for any thing or event.","l2":"Like understanding a house: bricks (material), blueprint (formal), builder (efficient), shelter (final).","l3":"Aristotle's four causes provide a complete explanatory framework. The 'final cause' (telos) is especially important — everything has a purpose, and understanding that purpose is key to understanding the thing itself."}
        ]
    },
    "confucius": {
        "summaryEn":"Confucius (Kongzi) is the most influential philosopher in Chinese history. His teachings on ethics, family, government, and personal cultivation shaped East Asian civilization for over two thousand years. He emphasized the cultivation of virtue (ren), ritual propriety (li), and the importance of education. His Analects, a collection of sayings recorded by his disciples, remain a foundational text of Chinese culture.",
        "goldenQuotesEn":[{"text":"Do not do to others what you do not want done to yourself.","source":"Analects 15:24"},{"text":"It does not matter how slowly you go as long as you do not stop.","source":"Analects"}],
        "coreThoughtsEn":[
            {"concept":"Ren (Benevolence)","desc":"Ren is the highest virtue — a profound humaneness and love for others that manifests in all relationships.","l1":"The core of being human is caring for others and treating them with kindness.","l2":"Like the warmth of sunlight that gives life to everything — ren is the warmth of the human heart.","l3":"Confucius defined ren simply as 'loving others.' It is the inner moral compass that, when cultivated, naturally manifests as proper conduct in every relationship."},
            {"concept":"Li (Ritual Propriety)","desc":"Rituals and social conventions are not empty formalities but essential practices that cultivate virtue and social harmony.","l1":"Manners and customs are important — they shape character and keep society running smoothly.","l2":"Like the rules of a game — they don't restrict play, they make it possible.","l3":"Li encompasses everything from table manners to state ceremonies. By practicing li, one internalizes the values it embodies — form shapes substance."}
        ]
    },
    "laozi": {
        "summaryEn":"Laozi (Lao Tzu) is the legendary founder of Daoism and author of the Daodejing (Tao Te Ching), one of the most translated works in world literature. His philosophy centers on the Dao (the Way) — the ineffable source and principle of all existence. He advocated for wu-wei (non-action or effortless action), simplicity, and harmony with nature, rejecting excessive governance and artificial sophistication.",
        "goldenQuotesEn":[{"text":"The Tao that can be told is not the eternal Tao.","source":"Daodejing, Chapter 1"},{"text":"A journey of a thousand miles begins with a single step.","source":"Daodejing, Chapter 64"}],
        "coreThoughtsEn":[
            {"concept":"Dao (The Way)","desc":"The Dao is the ultimate source and principle of all existence — it cannot be named or fully described.","l1":"There is a natural way the universe works — you can sense it but can't fully explain it.","l2":"Like the wind — you can't see it, but you can feel its effects everywhere.","l3":"The Dao is nameless, formless, yet gives rise to all things. It is not a creator deity but the natural, spontaneous order of the cosmos. To be in harmony with the Dao is to live well."},
            {"concept":"Wu-wei (Effortless Action)","desc":"The highest form of action is action that is natural, spontaneous, and without contrived effort — like water flowing.","l1":"Don't force things — let them happen naturally.","l2":"Like water: it doesn't push, it flows around obstacles and eventually wears down stone.","l3":"Wu-wei is not passivity but action that is perfectly aligned with the nature of things — without strain, without excess, without resistance. The best ruler governs least."}
        ]
    },
    "mencius": {
        "summaryEn":"Mencius (Mengzi) was the most important Confucian philosopher after Confucius himself. He is famous for arguing that human nature is inherently good — everyone is born with the 'four sprouts' of virtue: compassion, shame, deference, and the sense of right and wrong. He believed that these innate tendencies need to be cultivated to flourish, just as a seed needs nurturing to grow.",
        "goldenQuotesEn":[{"text":"Human nature is good, just as water naturally flows downward.","source":"Mencius"}],
        "coreThoughtsEn":[
            {"concept":"Innate Goodness","desc":"All humans are born with the four seeds of virtue — they just need cultivation to develop fully.","l1":"People are naturally good — like a seed that wants to grow into a healthy plant.","l2":"Like an acorn that has the potential to become an oak tree — given the right conditions, goodness naturally develops.","l3":"Mencius' four sprouts: compassion (the seed of ren), shame (of yi/righteousness), deference (of li/propriety), and approval/disapproval (of zhi/wisdom). These differentiate humans from animals."}
        ]
    },
    "zhuangzi": {
        "summaryEn":"Zhuangzi (Chuang Tzu) is the second foundational philosopher of Daoism, known for his brilliant wit, surreal parables, and radical relativism. His book, the Zhuangzi, challenges fixed categories and perspectives, celebrating spontaneity, freedom, and the relativity of all distinctions. The famous story of 'Butterfly Dream' questions the nature of reality and self.",
        "goldenQuotesEn":[{"text":"I dreamed I was a butterfly, fluttering hither and thither. Now I am not sure whether I was then a man dreaming I was a butterfly, or whether I am now a butterfly dreaming I am a man.","source":"Zhuangzi"},{"text":"Happiness is the absence of the striving for happiness.","source":"Zhuangzi"}],
        "coreThoughtsEn":[
            {"concept":"Butterfly Dream","desc":"The boundary between dreaming and waking, self and world, is not as fixed as we assume — reality may be an ongoing transformation.","l1":"How do you know you're awake right now and not dreaming?","l2":"Like a dream so vivid you didn't know you were dreaming — maybe life is like that.","l3":"Zhuangzi's butterfly dream is the most famous philosophical meditation on the problem of reality in Chinese philosophy — it doesn't answer the question but dissolves its urgency through humor and acceptance."}
        ]
    },
    "buddha": {
        "summaryEn":"Gautama Buddha (Siddhartha Gautama) was a spiritual teacher in ancient India whose teachings founded Buddhism. After encountering old age, sickness, and death, he renounced his princely life to seek the end of suffering. Through meditation, he attained enlightenment (nirvana) and taught the Four Noble Truths and the Eightfold Path as the way to liberation from the cycle of rebirth (samsara).",
        "goldenQuotesEn":[{"text":"Life is suffering. The cause of suffering is desire. The end of suffering is possible. The path is the Eightfold Path.","source":"First Sermon (Dhammacakkappavattana Sutta)"},{"text":"Peace comes from within. Do not seek it without.","source":"Dhammapada"}],
        "coreThoughtsEn":[
            {"concept":"Four Noble Truths","desc":"1) Life involves suffering (dukkha); 2) Suffering is caused by craving/attachment; 3) Suffering can end; 4) The Eightfold Path leads to the end of suffering.","l1":"Life has pain, but there is a way out — by understanding desire and following a wise path.","l2":"Like being shot by an arrow — first you need to remove the arrow (end suffering), not ask who shot it.","l3":"The Four Noble Truths are a medical diagnosis of the human condition: symptom (suffering), cause (craving), prognosis (cure is possible), and prescription (the Eightfold Path)."}
        ]
    },
    "augustine": {
        "summaryEn":"Augustine of Hippo is the most influential Christian philosopher of the ancient world. His Confessions is the first major Western autobiography, chronicling his restless search for truth from Manichaeism to Christianity. He developed the concepts of original sin, divine grace, and the City of God vs. the City of Man, which became cornerstones of Western Christian thought.",
        "goldenQuotesEn":[{"text":"You have made us for yourself, O Lord, and our heart is restless until it rests in you.","source":"Confessions"}],
        "coreThoughtsEn":[
            {"concept":"Restless Heart","desc":"Human beings are created with a natural longing for God — this restlessness drives all our searching and can only be satisfied by the divine.","l1":"Everyone has a deep longing inside that nothing in this world can fully satisfy.","l2":"Like a compass that always points north — the human heart always points toward the divine.","l3":"Augustine's Confessions traces his own restless journey through pleasure, ambition, and Manichaeism to his final rest in Christian faith — a model of the soul's quest for God."}
        ]
    },
    "avicenna": {
        "summaryEn":"Avicenna (Ibn Sina) was a Persian polymath and the most important philosopher of the Islamic Golden Age. His vast philosophical-medical encyclopedia, The Canon of Medicine, was the standard medical text in Europe for centuries. His 'Flying Man' thought experiment is a landmark in the philosophy of mind, and his distinction between essence and existence influenced medieval European scholasticism.",
        "goldenQuotesEn":[{"text":"The more brilliant the lightning, the quicker it disappears.","source":"Avicenna, The Book of Healing"}],
        "coreThoughtsEn":[
            {"concept":"Flying Man","desc":"If a person were created fully formed, floating in the air without sensory input, he would still be aware of his own existence — proving the self is known intuitively, not through the body.","l1":"You know you exist without needing to see or touch yourself — your sense of self is separate from your body.","l2":"Like being in a dark room — you can't see anything but you know you're there.","l3":"This thought experiment anticipates Descartes' 'I think, therefore I am' by six centuries and is a key argument for the immaterial nature of the self."}
        ]
    },
    "aquinas": {
        "summaryEn":"Thomas Aquinas was the greatest philosopher-theologian of medieval scholasticism. His massive Summa Theologica attempted to synthesize Aristotelian philosophy with Christian theology. He formulated the Five Ways (proofs for the existence of God) and developed a comprehensive system of natural law ethics. His integration of faith and reason became official Catholic doctrine.",
        "goldenQuotesEn":[{"text":"To one who has faith, no explanation is necessary. To one without faith, no explanation is possible.","source":"Thomas Aquinas"}],
        "coreThoughtsEn":[
            {"concept":"Five Ways","desc":"Five philosophical arguments for the existence of God: motion, causation, contingency, perfection, and teleological order.","l1":"Looking at the world around us, there are five logical reasons to believe in God.","l2":"Like seeing footprints in the sand and inferring someone walked there — the universe shows evidence of a creator.","l3":"The Five Ways are: 1) Unmoved Mover, 2) First Cause, 3) Necessary Being, 4) Perfect Standard, 5) Cosmic Design — each starting from an observable fact and reasoning to a first principle."}
        ]
    },
    "machiavelli": {
        "summaryEn":"Machiavelli was a Renaissance political philosopher whose masterpiece The Prince broke away from idealistic political theory to offer a ruthless, realistic analysis of power. His name became synonymous with cunning and deceit ('Machiavellian'), but he also wrote the Discourses on Livy, which celebrated republican liberty.",
        "goldenQuotesEn":[{"text":"It is better to be feared than loved, if you cannot be both.","source":"The Prince"},{"text":"The ends justify the means.","source":"Attributed to Machiavelli"}],
        "coreThoughtsEn":[
            {"concept":"Virtù vs. Fortuna","desc":"A successful ruler must combine virtù (skill, strength, decisive action) to master fortuna (fortune, luck, circumstances).","l1":"Success comes from both skill and luck — but a wise leader doesn't rely on luck.","l2":"Like a river: fortune is a flood that destroys unprepared banks (weak rulers), but virtù builds strong embankments.","l3":"Virtù is the specifically Machiavellian virtue — not moral goodness but the strength, cunning, and flexibility needed to maintain power in a dangerous world."}
        ]
    },
    "bacon": {
        "summaryEn":"Francis Bacon is the father of empiricism and the scientific method. He argued that knowledge should be based on systematic observation and experiment, not on ancient authority or abstract reasoning. His Novum Organum proposed a new system of logic (induction) to replace Aristotle's deductive logic, and his phrase 'knowledge is power' captures the spirit of modern science.",
        "goldenQuotesEn":[{"text":"Knowledge itself is power.","source":"Meditationes Sacrae"},{"text":"Nature, to be commanded, must be obeyed.","source":"Novum Organum"}],
        "coreThoughtsEn":[
            {"concept":"Scientific Method","desc":"Knowledge must be built through systematic observation, experimentation, and inductive reasoning — not from ancient books or abstract theory.","l1":"To understand nature, you must observe it, experiment with it, and learn from what actually happens.","l2":"Like a detective who collects evidence and draws conclusions, rather than assuming who the criminal is.","l3":"Bacon's Great Instauration: a complete reform of knowledge. The method proceeds through careful observation, systematic data collection (tables of presence/absence/degree), and cautious generalization — the foundation of modern science."}
        ]
    },
    "descartes": {
        "summaryEn":"René Descartes is the father of modern philosophy. He began with radical doubt — doubting everything that could possibly be doubted — until he arrived at the one indubitable truth: 'Cogito, ergo sum' (I think, therefore I am). His mind-body dualism separated the mental from the physical, setting the agenda for modern philosophy of mind.",
        "goldenQuotesEn":[{"text":"I think, therefore I am. (Cogito, ergo sum)","source":"Discourse on the Method"},{"text":"I doubt, therefore I think; I think, therefore I am.","source":"Principles of Philosophy"}],
        "coreThoughtsEn":[
            {"concept":"Cogito Ergo Sum","desc":"The one certain truth: even if all my perceptions are deceived, the fact that I am thinking proves that I exist as a thinking being.","l1":"The only thing you can be absolutely sure of is that you exist — because you're thinking right now.","l2":"Like a computer that can't trust any data coming in but knows for sure it exists because it's processing.","l3":"Descartes' method of hyperbolic doubt: reject anything that can be doubted. The senses can deceive, I could be dreaming, an evil demon could be fooling me — but the act of doubting itself requires a thinker. Cogito ergo sum."},
            {"concept":"Mind-Body Dualism","desc":"The mind (thinking substance) and the body (extended substance) are two fundamentally different kinds of reality.","l1":"Your mind and your body are different things — they interact but are separate.","l2":"Like a pilot in a ship — the pilot (mind) is separate from the vessel (body).","l3":"Descartes argued that the mind is indivisible (you can't have half a thought) while the body is divisible, proving they are different substances. This 'Cartesian dualism' remains a central problem in philosophy of mind."}
        ]
    },
    "spinoza": {
        "summaryEn":"Baruch Spinoza was a radical Enlightenment philosopher who identified God with Nature (Deus sive Natura). He argued that there is only one infinite substance — God/Nature — and that everything else is a mode or expression of it. His Ethics is a masterpiece of geometric method, demonstrating a complete ethical system 'in the geometrical manner.'",
        "goldenQuotesEn":[{"text":"God is Nature. (Deus sive Natura)","source":"Ethics"},{"text":"Peace is not the absence of war; it is a virtue, a state of mind, a disposition for benevolence, confidence, and justice.","source":"Theological-Political Treatise"}],
        "coreThoughtsEn":[
            {"concept":"God = Nature","desc":"There is only one substance — God or Nature — and everything in the universe is a mode of this single reality.","l1":"God and the universe are the same thing — there's nothing outside of nature.","l2":"Like the ocean and its waves — the waves aren't separate from the ocean, they ARE the ocean in different forms.","l3":"Spinoza's pantheism was revolutionary and scandalous: God is not a transcendent creator but the immanent cause of all things. Everything that exists is a modification of the divine substance under the attribute of thought or extension."}
        ]
    },
    "locke": {
        "summaryEn":"John Locke is the father of classical liberalism. His theory of the mind as a tabula rasa (blank slate) at birth founded British empiricism. His political philosophy — natural rights (life, liberty, property), government by consent, and the right to revolution — profoundly shaped the American and French revolutions and modern democratic thought.",
        "goldenQuotesEn":[{"text":"All men are naturally in a state of perfect freedom to order their actions without depending on the will of any other man.","source":"Second Treatise of Government"}],
        "coreThoughtsEn":[
            {"concept":"Tabula Rasa","desc":"The human mind at birth is a blank slate — all knowledge comes from experience through sensation and reflection.","l1":"We are not born with built-in knowledge — everything we know comes from experience.","l2":"Like a new notebook — empty pages waiting to be filled by what we see, hear, and do.","l3":"Locke's attack on innate ideas: if there were innate principles, all humans would agree on them (e.g., basic moral rules), but we find disagreement everywhere. Therefore, the mind starts as 'white paper, void of all characters.'"}
        ]
    },
    "leibniz": {
        "summaryEn":"Gottfried Wilhelm Leibniz was a German philosopher, mathematician, and polymath — one of the last great 'universal geniuses.' He invented calculus independently of Newton, dreamed of a universal logical language, and proposed that the universe consists of infinite, mind-like substances called 'monads.' He famously argued that this is 'the best of all possible worlds.'",
        "goldenQuotesEn":[{"text":"This is the best of all possible worlds.","source":"Theodicy"},{"text":"We live in the best of all possible worlds.","source":"Theodicy"}],
        "coreThoughtsEn":[
            {"concept":"Monads","desc":"Reality consists of infinite, indivisible, mind-like substances (monads) that have no windows — each mirrors the entire universe from its own perspective.","l1":"The universe is made of countless individual 'viewpoints' — each experiencing reality from its own perspective.","l2":"Like a city seen from different windows — each view is different but all show the same city.","l3":"Monads are 'simple substances' with no parts, no spatial extension, and no interaction between them. Their harmony is pre-established by God — the 'pre-established harmony' that explains mind-body coordination."}
        ]
    },
    "hume": {
        "summaryEn":"David Hume was the most radical of the British empiricists. He argued that all knowledge comes from impressions and ideas, and that causation is not a necessary connection in reality but a habit of the mind. His skeptical conclusions — that we cannot rationally justify induction, causality, the self, or even the external world — woke Kant from his 'dogmatic slumber.'",
        "goldenQuotesEn":[{"text":"Reason is, and ought only to be, the slave of the passions.","source":"A Treatise of Human Nature"},{"text":"Custom, then, is the great guide of human life.","source":"An Enquiry Concerning Human Understanding"}],
        "coreThoughtsEn":[
            {"concept":"Problem of Induction","desc":"We cannot rationally justify the assumption that the future will resemble the past — 'induction' is just a habit based on repeated experience.","l1":"Just because the sun has risen every day doesn't prove it will rise tomorrow — we just assume it will.","l2":"Like a chicken who expects food every morning because it's been fed before — until one day it's slaughtered.","l3":"Hume's fork: all knowledge is either relations of ideas (math/logic, certain but tells us nothing about the world) or matters of fact (contingent, based on cause and effect). But causation itself is just constant conjunction plus mental habit — no rational justification."}
        ]
    },
    "rousseau": {
        "summaryEn":"Jean-Jacques Rousseau was a Genevan philosopher whose political and educational ideas profoundly influenced the Enlightenment, the French Revolution, and Romanticism. He argued that humans are naturally good but corrupted by civilization ('the noble savage'), and that legitimate political authority rests on the 'general will' of the people.",
        "goldenQuotesEn":[{"text":"Man is born free, and everywhere he is in chains.","source":"The Social Contract"},{"text":"Nature made man happy and good, but civilization makes him miserable and wicked.","source":"Discourse on Inequality"}],
        "coreThoughtsEn":[
            {"concept":"General Will","desc":"True political authority comes from the 'general will' — what is best for the community as a whole, not the sum of individual interests.","l1":"A society should be guided by what's best for everyone, not just what each person wants individually.","l2":"Like a sports team — sometimes the best play is not what each player wants but what serves the team.","l3":"The general will is not the 'will of all' (aggregate of private interests) but the common good. It is necessarily right — the problem is distinguishing it from private interests, which requires civic virtue."}
        ]
    },
    "kant": {
        "summaryEn":"Immanuel Kant is arguably the most important philosopher since Plato. His 'Copernican Revolution' in philosophy argued that the mind actively structures experience rather than passively receiving it. His Categorical Imperative — act only according to rules that could be universal laws — remains the most famous formulation of moral duty. His epistemology, ethics, and aesthetics each radically reshaped their fields.",
        "goldenQuotesEn":[{"text":"Two things fill the mind with ever new and increasing admiration and awe: the starry heavens above me and the moral law within me.","source":"Critique of Practical Reason"},{"text":"Act only according to that maxim whereby you can at the same time will that it should become a universal law.","source":"Groundwork of the Metaphysics of Morals"}],
        "coreThoughtsEn":[
            {"concept":"Categorical Imperative","desc":"Morality is not about consequences but about duty — act according to rules that could be universal laws, treating humanity always as an end, never merely as a means.","l1":"Always do what you would want everyone else to do — never use people as tools for your own purposes.","l2":"Like a universal test: if everyone did what you're about to do, would the world be better or just broken?","l3":"The Categorical Imperative has three formulations: 1) Universal Law, 2) Humanity as an End, 3) Kingdom of Ends. They all express the same principle: morality is autonomous, self-given law, not calculation of consequences."},
            {"concept":"Copernican Revolution","desc":"Knowledge is not the mind conforming to objects — objects conform to the mind's innate structures of understanding.","l1":"We don't see the world as it is — we see it through the 'lens' of our mind.","l2":"Like wearing colored glasses — you don't see the world's true color, you see the world filtered through the glasses.","l3":"Kant's revolutionary insight: space and time are not features of the world itself but forms of our intuition. Causality is not a property of things-in-themselves but a category of the understanding. We can never know things as they are in themselves (noumena)."}
        ]
    },
    "hegel": {
        "summaryEn":"Georg Wilhelm Friedrich Hegel developed the most ambitious system in modern philosophy — absolute idealism. He argued that reality unfolds through a dialectical process (thesis → antithesis → synthesis) in which the Absolute Spirit gradually achieves self-consciousness through history. His phenomenology of Spirit traces the journey of consciousness from sense-certainty to absolute knowing.",
        "goldenQuotesEn":[{"text":"What is rational is actual, and what is actual is rational.","source":"Philosophy of Right"},{"text":"The owl of Minerva spreads its wings only with the falling of the dusk.","source":"Philosophy of Right"}],
        "coreThoughtsEn":[
            {"concept":"Dialectic","desc":"The engine of history and thought: a thesis generates its opposite (antithesis), and their conflict is resolved into a higher synthesis that preserves what is true in both.","l1":"Progress happens through conflict — an idea meets its opposite, and together they create something better.","l2":"Like a debate where two opposing views clash and produce a more complete understanding.","l3":"Hegel's dialectic is not a simple 'thesis-antithesis-synthesis' formula (a simplification by later commentators). It is a logic of determinate negation: the negative result is not nothing but the negation of a specific content, which generates a more concrete, richer category."}
        ]
    },
    "marx": {
        "summaryEn":"Karl Marx is the most influential critic of capitalism. He argued that economic relations (the base) determine all other aspects of society (the superstructure — politics, religion, culture). History is a history of class struggles. Capitalism, he predicted, would be overthrown by the proletariat, leading to a classless, communist society. His ideas shaped the 20th century more than any other thinker.",
        "goldenQuotesEn":[{"text":"Workers of the world, unite! You have nothing to lose but your chains.","source":"The Communist Manifesto"},{"text":"The philosophers have only interpreted the world, in various ways; the point is to change it.","source":"Theses on Feuerbach"}],
        "coreThoughtsEn":[
            {"concept":"Historical Materialism","desc":"The economic 'base' (relations of production) determines the 'superstructure' (politics, law, culture, ideology) — history moves through modes of production: primitive, slave, feudal, capitalist, socialist.","l1":"How people make a living shapes everything else — their politics, their beliefs, their culture.","l2":"Like a building: the foundation (economy) determines what can be built on top (government, religion, art).","l3":"The key to understanding history is not ideas but material conditions. Changes in productive forces create contradictions with existing relations of production, leading to revolution and a new mode of production."}
        ]
    },
    "nietzsche": {
        "summaryEn":"Friedrich Nietzsche is one of the most provocative and misunderstood philosophers. He proclaimed 'God is dead,' not with joy but with a warning — the collapse of traditional values leaves humanity facing nihilism. His concepts of the Will to Power, the Übermensch (Overman/Superman), and Eternal Recurrence challenge us to create our own values and affirm life in its totality.",
        "goldenQuotesEn":[{"text":"God is dead. God remains dead. And we have killed him.","source":"The Gay Science"},{"text":"What does not kill me makes me stronger.","source":"Twilight of the Idols"}],
        "coreThoughtsEn":[
            {"concept":"God is Dead","desc":"The foundation of Western morality — Christian faith — has collapsed under the weight of modern science and criticism. This creates both a crisis (nihilism) and an opportunity (creation of new values).","l1":"The traditional moral rules that everyone used to believe in no longer hold — now we have to figure out for ourselves what matters.","l2":"Like a child who stops believing in Santa Claus — there's a sense of loss, but also the freedom to see the world as it really is.","l3":"'God is dead' is not a celebration but a diagnosis. For two thousand years, Christianity provided meaning and value. With its decline, Europeans face a 'nihilistic' void. The task: overcome nihilism by creating new values through the Will to Power."}
        ]
    },
    "husserl": {
        "summaryEn":"Edmund Husserl founded phenomenology — the rigorous study of conscious experience from the first-person perspective. He introduced the 'epoché' (bracketing of assumptions about reality) to focus on how things appear to consciousness. His work revolutionized European philosophy and influenced existentialism, hermeneutics, and cognitive science.",
        "goldenQuotesEn":[{"text":"To the things themselves! (Zu den Sachen selbst!)","source":"Phenomenology slogan"}],
        "coreThoughtsEn":[
            {"concept":"Phenomenological Reduction","desc":"To understand consciousness, we must 'bracket' (set aside) all assumptions about whether things exist in reality and focus purely on how they appear to us.","l1":"Instead of asking 'is this real?', ask 'how does this appear to my consciousness?'","l2":"Like a theater audience — you know the play isn't real, but you focus on what appears on stage.","l3":"The epoché suspends the 'natural attitude' — our default assumption that the world exists independently. By bracketing this, we can study the structures of experience itself (intentionality, temporality, embodiment)."}
        ]
    },
    "wittgenstein": {
        "summaryEn":"Ludwig Wittgenstein produced two radically different philosophies that both reshaped 20th-century thought. The early Wittgenstein (Tractatus Logico-Philosophicus) argued that language pictures the world and that philosophy's job is to clarify thoughts. The later Wittgenstein (Philosophical Investigations) rejected this, arguing that meaning is use — words get their meaning from their role in 'language games' embedded in 'forms of life.'",
        "goldenQuotesEn":[{"text":"What can be said at all can be said clearly, and what we cannot talk about we must pass over in silence.","source":"Tractatus Logico-Philosophicus"},{"text":"The limits of my language mean the limits of my world.","source":"Tractatus 5.6"}],
        "coreThoughtsEn":[
            {"concept":"Language Games","desc":"Meaning is not fixed reference but use — words function like moves in a game, and their meaning is determined by the rules of the specific 'language game' in which they are used.","l1":"Words don't have fixed meanings — their meaning depends on how they're used in context.","l2":"Like the word 'check' in chess vs. in a bank — same word, completely different meaning depending on the 'game.'","l3":"The later Wittgenstein dissolves philosophical problems by showing they arise from taking words out of their ordinary language games. Philosophy is a 'battle against the bewitchment of our intelligence by means of language.'"}
        ]
    },
    # ===== NEW 10 =====
    "epicurus": {
        "summaryEn":"Epicurus founded a school in Athens that taught pleasure as the highest good — but his 'pleasure' is not hedonistic indulgence. He advocated for ataraxia (tranquility) through rational calculation: choose simple, natural pleasures over extravagant ones. His atomist physics, rejection of divine intervention, and argument that 'death is nothing to us' form a complete therapeutic philosophy aimed at eliminating fear and achieving peace of mind.",
        "goldenQuotesEn":[{"text":"Death is nothing to us. When we exist, death is not; and when death exists, we are not.","source":"Letter to Menoeceus"}],
        "coreThoughtsEn":[
            {"concept":"Pleasure is the Good","desc":"Pleasure is the only intrinsic good and pain the only intrinsic evil — but the wise person chooses simple, sustainable pleasures that produce lasting tranquility.","l1":"Happiness comes from choosing simple pleasures that don't cause future pain.","l2":"Like eating a good meal vs. eating so much you get sick — the wise person chooses the first.","l3":"Epicurus' classification of desires: natural + necessary (food, shelter), natural + unnecessary (luxury food), vain/empty (fame, power). The wise satisfy only the first category to achieve ataraxia."}
        ]
    },
    "marcus-aurelius": {
        "summaryEn":"Marcus Aurelius was a Roman Emperor and the last of the Five Good Emperors, remembered for his Meditations — personal writings on Stoic philosophy composed during military campaigns. His philosophy emphasizes control over one's own judgment, acceptance of fate, and service to the common good. Despite holding absolute power, he wrote with humility and self-discipline.",
        "goldenQuotesEn":[{"text":"You have power over your mind — not outside events. Realize this, and you will find strength.","source":"Meditations"},{"text":"The happiness of your life depends upon the quality of your thoughts.","source":"Meditations"}],
        "coreThoughtsEn":[
            {"concept":"Dichotomy of Control","desc":"Some things are within our control (judgments, choices, values) and others are not (health, reputation, others' opinions). Focus only on what you control.","l1":"Don't worry about things you can't change — focus your energy on what you can control.","l2":"Like a tennis player focusing on their swing, not on whether the wind blows.","l3":"This is the core Stoic discipline: the distinction between what is 'up to us' and what is not. All anxiety comes from caring about things outside our control. Complete freedom comes from withdrawing concern from the uncontrollable."}
        ]
    },
    "hobbes": {
        "summaryEn":"Thomas Hobbes was the founder of modern political philosophy. His Leviathan argues that in the 'state of nature' — without government — human life is a 'war of all against all,' making life 'nasty, brutish, and short.' To escape this, people enter a social contract, surrendering their rights to an absolute sovereign in exchange for peace and security.",
        "goldenQuotesEn":[{"text":"The life of man is solitary, poor, nasty, brutish, and short.","source":"Leviathan, Chapter 13"},{"text":"Covenants, without the sword, are but words.","source":"Leviathan, Chapter 17"}],
        "coreThoughtsEn":[
            {"concept":"State of Nature","desc":"Without government, humans are in a constant state of war — equality of ability leads to competition, diffidence, and glory-seeking, making peace impossible without a common power.","l1":"Without laws and government, people would constantly fight over resources and status.","l2":"Like a school with no teachers — the strongest kids would take what they want and no one would be safe.","l3":"Hobbes' three causes of conflict: competition (for resources), diffidence (fear of others), and glory (reputation). These naturally lead to a 'war of every man against every man' in the absence of sovereign power."}
        ]
    },
    "mill": {
        "summaryEn":"John Stuart Mill was the most influential English philosopher of the 19th century. He refined utilitarianism by distinguishing higher and lower pleasures — 'better to be a dissatisfied Socrates than a satisfied fool.' His On Liberty defends individual freedom against the 'tyranny of the majority,' and his harm principle — the only justification for limiting liberty is preventing harm to others — remains a cornerstone of liberal thought.",
        "goldenQuotesEn":[{"text":"It is better to be a human being dissatisfied than a pig satisfied; better to be Socrates dissatisfied than a fool satisfied.","source":"Utilitarianism"},{"text":"Over one's mind and over one's body the individual is sovereign.","source":"On Liberty"}],
        "coreThoughtsEn":[
            {"concept":"Harm Principle","desc":"The only legitimate reason to restrict someone's liberty is to prevent harm to others — not to protect them from themselves, not to enforce morality.","l1":"You can do whatever you want as long as it doesn't hurt other people.","l2":"Like traffic laws — they restrict your driving only when it endangers others, not because of how you drive when alone.","l3":"Mill's principle: 'The only purpose for which power can be rightfully exercised over any member of a civilized community, against his will, is to prevent harm to others.' This excludes paternalism and moral enforcement."}
        ]
    },
    "schopenhauer": {
        "summaryEn":"Arthur Schopenhauer is the philosopher of pessimism. He saw the world as driven by a blind, irrational 'Will to Live' that produces endless suffering — desire unsatisfied is pain, desire satisfied is boredom. Art, especially music, offers temporary escape from the Will's domination. His philosophy drew on Plato, Kant, and Indian thought, and profoundly influenced Nietzsche, Wagner, and Freud.",
        "goldenQuotesEn":[{"text":"Life swings like a pendulum backward and forward between pain and boredom.","source":"The World as Will and Representation"},{"text":"A man can do what he wants, but not want what he wants.","source":"On the Freedom of the Will"}],
        "coreThoughtsEn":[
            {"concept":"Will as Thing-in-Itself","desc":"The ultimate reality is not rational mind but a blind, ceaseless, striving Will — the Kantian 'thing-in-itself' is Will, not reason.","l1":"The driving force behind everything is not logic but a raw, restless urge — like hunger or desire.","l2":"Like an engine that never stops running — the will drives everything, whether we like it or not.","l3":"Schopenhauer read Kant's noumenon (thing-in-itself) as Will — a blind, purposeless striving that manifests in all nature, from gravity to human ambition. This is why the world is fundamentally suffering: the Will can never be satisfied."}
        ]
    },
    "heidegger": {
        "summaryEn":"Martin Heidegger revived the question of Being (Sein) in 20th-century philosophy. His masterpiece Being and Time analyzes Dasein (human existence) as 'Being-in-the-world' and explores authentic existence through 'Being-toward-death.' His later work criticized technology as a 'framing' (Gestell) that reduces everything, including humans, to resources.",
        "goldenQuotesEn":[{"text":"Language is the house of Being. In its home humans dwell.","source":"Letter on Humanism"},{"text":"We are too late for the gods and too early for Being. Being's poem, just begun, is man.","source":"The Thinker as Poet"}],
        "coreThoughtsEn":[
            {"concept":"Dasein (Being-in-the-World)","desc":"Human existence is not a subject separate from the world but a 'being-there' already immersed in a meaningful context of relationships and practices.","l1":"You are not a mind separate from the world — you're always already part of it, engaged with things and people.","l2":"Like a fish in water — you don't first exist and then enter a world; you are constituted by your being-in-the-world.","l3":"Heidegger rejects the Cartesian subject-object split. Dasein's 'thrownness' means we always find ourselves already in a world we didn't choose. Our 'projection' means we exist as possibilities, not fixed essences. 'Authenticity' means facing this freedom and finitude squarely."}
        ]
    },
    "foucault": {
        "summaryEn":"Michel Foucault radically reshaped how we think about power, knowledge, and society. He argued that power is not repressive but productive — it produces knowledge, discourse, and subjects. His studies of madness, the clinic, the prison, and sexuality reveal how modern institutions discipline bodies and normalize populations. His genealogical method traces the contingent struggles behind what we take as natural or necessary.",
        "goldenQuotesEn":[{"text":"Power is not something that is acquired, seized, or shared — it is exercised from innumerable points.","source":"The History of Sexuality, Vol. 1"},{"text":"Do not ask who I am and do not ask me to remain the same.","source":"The Archaeology of Knowledge"}],
        "coreThoughtsEn":[
            {"concept":"Power is Productive","desc":"Modern power does not just prohibit — it produces knowledge, creates categories, shapes desires, and constructs subjects.","l1":"Power isn't just 'you can't do that' — it's also 'this is what you should be, want, and believe.'","l2":"Like social media algorithms — they don't block content (repressive), they shape what you see and want (productive).","l3":"Foucault's 'disciplinary power' operates through surveillance (Panopticon), normalization, and examination — it doesn't punish bodies but trains souls. Biopower manages populations through statistics, public health, and demographics."}
        ]
    },
    "wang-yangming": {
        "summaryEn":"Wang Yangming was the most original Confucian philosopher of the Ming dynasty and the founder of the School of Mind (Xinxue). His core doctrine — 'the unity of knowledge and action' — holds that genuine knowledge necessarily manifests as action. He taught that everyone possesses innate moral knowledge (liangzhi) and that self-cultivation is about removing selfish desires to let this inner goodness shine forth.",
        "goldenQuotesEn":[{"text":"Knowledge is the beginning of action; action is the completion of knowledge.","source":"Instructions for Practical Living"},{"text":"The mind is principle (xin ji li). There is nothing outside the mind.","source":"Wang Yangming"}],
        "coreThoughtsEn":[
            {"concept":"Unity of Knowledge and Action","desc":"True knowledge inherently includes action — knowing without acting is not really knowing. Knowledge and action are two aspects of one process.","l1":"If you truly know something is right, you will do it — not doing means you don't truly know.","l2":"Like knowing a recipe perfectly vs. actually cooking the dish — real knowledge includes the doing.","l3":"Wang's famous rebuttal of Zhu Xi's 'investigate things to extend knowledge': you don't first know and then act. The desire to know is already an incipient action; the completion of action is the perfection of knowledge."}
        ]
    },
    "hanfei": {
        "summaryEn":"Han Fei was the synthesizer of Legalist philosophy in ancient China. He combined Shang Yang's 'law' (fa), Shen Buhai's 'method' (shu), and Shen Dao's 'power' (shi) into a comprehensive political theory. He argued that human nature is selfish and that effective government requires clear laws, strict punishments, and rewards — not moral persuasion.",
        "goldenQuotesEn":[{"text":"The law does not favor the noble; the measuring line does not bend to the crooked.","source":"Han Feizi, Chapter 6"},{"text":"When the times change, affairs change; when affairs change, preparations should change.","source":"Han Feizi, Chapter 49"}],
        "coreThoughtsEn":[
            {"concept":"Fa, Shu, Shi","desc":"Effective governance requires three elements: law (clear rules for all), method (administrative techniques to control officials), and power (the ruler's authoritative position).","l1":"Good government needs clear written laws, management techniques, and real authority.","l2":"Like running a company: you need employee rules (fa), management systems (shu), and CEO authority (shi).","l3":"Han Fei's synthesis: Shang Yang contributed fa (strict, public law), Shen Buhai contributed shu (techniques for selecting/managing officials), and Shen Dao contributed shi (the strategic use of positional power). All three are essential."}
        ]
    },
    "nagarjuna": {
        "summaryEn":"Nagarjuna is the most important philosopher of Mahayana Buddhism, founder of the Madhyamaka (Middle Way) school. His doctrine of emptiness (sunyata) argues that all phenomena are empty of intrinsic essence because they arise dependently (pratityasamutpada). Emptiness is not nihilism but the middle way between eternalism and annihilationism.",
        "goldenQuotesEn":[{"text":"Whatever arises dependently is empty, is dependently designated, and is the middle way.","source":"Mulamadhyamakakarika 24:18"},{"text":"There is not the slightest difference between samsara and nirvana.","source":"Mulamadhyamakakarika 25:19"}],
        "coreThoughtsEn":[
            {"concept":"Emptiness (Sunyata)","desc":"All things are 'empty' — not because they don't exist, but because nothing has a fixed, independent essence. Everything exists only in relation to everything else.","l1":"Nothing has a fixed, independent nature — everything depends on everything else.","l2":"Like a mirror image — it looks like something but has no substance; it's there but not as a fixed thing.","l3":"Nagarjuna's revolutionary move: emptiness is itself empty. The concept of emptiness is not a new ultimate reality but a therapeutic tool to cure our tendency to reify concepts. Even emptiness must not be clung to — it's the 'poison antidote' that must itself be expelled."}
        ]
    }
}

# Apply English data to philosophers
count = 0
for ph in data['philosophers']:
    eid = ph['id']
    if eid not in EN:
        continue
    en = EN[eid]

    # Simple fields (summary, thought evolution, etc.)
    for field in ['summaryEn', 'thoughtEvolutionEn', 'scientificEvalEn', 'aiReviewEn', 'anecdoteEn']:
        if field in en:
            ph[field] = en[field]

    # Golden quotes
    if 'goldenQuotesEn' in en:
        if ph.get('goldenQuotes'):
            for i, qen in enumerate(en['goldenQuotesEn']):
                if i < len(ph['goldenQuotes']):
                    ph['goldenQuotes'][i]['textEn'] = qen['text']
                    ph['goldenQuotes'][i]['sourceEn'] = qen['source']

    # Core thoughts
    if 'coreThoughtsEn' in en:
        if ph.get('coreThoughts'):
            for i, cen in enumerate(en['coreThoughtsEn']):
                if i < len(ph['coreThoughts']):
                    ph['coreThoughts'][i]['conceptEn'] = cen['concept']
                    ph['coreThoughts'][i]['descEn'] = cen['desc']
                    if 'l1' in cen:
                        ph['coreThoughts'][i]['l1En'] = cen['l1']
                    if 'l2' in cen:
                        ph['coreThoughts'][i]['l2En'] = cen['l2']
                    if 'l3' in cen:
                        ph['coreThoughts'][i]['l3En'] = cen['l3']

    count += 1

# Fix philosophers without EN data (generate minimal English from existing data)
for ph in data['philosophers']:
    if ph['id'] not in EN:
        # Provide minimal English based on Chinese content
        if not ph.get('summaryEn'):
            ph['summaryEn'] = ph.get('summary', '')[:200] + '...'
        if ph.get('goldenQuotes'):
            for q in ph['goldenQuotes']:
                if 'textEn' not in q:
                    q['textEn'] = q.get('text', '')
                    q['sourceEn'] = q.get('source', '')
        if ph.get('coreThoughts'):
            for ct in ph['coreThoughts']:
                if 'conceptEn' not in ct:
                    ct['conceptEn'] = ct.get('concept', '')
                    ct['descEn'] = ct.get('desc', '')[:200]
        count += 1

with open('D:/applications/AI_files/philomap/data/philosophers.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"English data added to {count} philosophers")
print(f"Total philosophers: {len(data['philosophers'])}")
