import uuid

A1_5_ITEMS = [
    {
        "item_type": "multiple_choice",
        "prompt": "How do you politely say \"I would like a coffee\" in Italian?",
        "options": ["Vorrei un caffè.", "Voglio caffè.", "Dammi caffè.", "Caffè per me."],
        "correct_answer": "Vorrei un caffè.",
        "explanation": "\"Vorrei...\" is more polite than \"Voglio...\" in café situations.",
        "weak_point": "cafe_vocabulary",
    },
    {
        "item_type": "fill_blank",
        "prompt": "Complete the question: \"_____ costa il cappuccino?\"",
        "options": None,
        "correct_answer": "Quanto",
        "explanation": "\"Quanto costa...?\" means \"How much does ... cost?\"",
        "weak_point": "asking_prices",
    },
    {
        "item_type": "multiple_choice",
        "prompt": "Which sentence correctly means \"I don't like tea\"?",
        "options": ["Non mi piace il tè.", "Mi piace non il tè.", "No mi piace tè.", "Mi non piace il tè."],
        "correct_answer": "Non mi piace il tè.",
        "explanation": "\"Non\" comes before the verb or expression to make a sentence negative.",
        "weak_point": "negation",
    },
    {
        "item_type": "short_answer",
        "prompt": "Write a polite phrase to ask for the bill.",
        "options": None,
        "correct_answer": "Il conto, per favore.",
        "keywords": ["conto", "favore"],
        "explanation": "\"Il conto, per favore\" is the polite way to ask for the bill.",
        "weak_point": "asking_for_bill",
    },
    {
        "item_type": "multiple_choice",
        "prompt": "Choose the correct article: \"_____ pizza\"",
        "options": ["una", "un", "uno", "il"],
        "correct_answer": "una",
        "explanation": "\"Pizza\" is feminine singular, so the indefinite article is \"una\".",
        "weak_point": "article_agreement",
    },
    {
        "item_type": "multiple_choice",
        "prompt": "How do you ask \"Where is the restaurant?\" in Italian?",
        "options": ["Dov'è il ristorante?", "Cosa il ristorante?", "Quanto il ristorante?", "Come il ristorante?"],
        "correct_answer": "Dov'è il ristorante?",
        "explanation": "\"Dove\" means \"where\". \"Dov'è\" is the contraction of \"dove è\".",
        "weak_point": "question_words",
    },
    {
        "item_type": "multiple_choice",
        "prompt": "Which sentence correctly uses \"mi piace\"?",
        "options": ["Mi piace la pasta.", "Mi piace le paste.", "Mi piaciono la pasta.", "Mi piaci la pasta."],
        "correct_answer": "Mi piace la pasta.",
        "explanation": "\"Mi piace\" is used with singular nouns. For plural, use \"mi piacciono\".",
        "weak_point": "piacere",
    },
    {
        "item_type": "short_writing",
        "prompt": "Write a short sentence ordering a cappuccino and a cornetto at a café.",
        "options": None,
        "correct_answer": "Vorrei un cappuccino e un cornetto, per favore.",
        "keywords": ["cappuccino", "cornetto"],
        "explanation": "A polite order uses \"Vorrei\" and includes \"per favore\".",
        "weak_point": "cafe_vocabulary",
    },
]

A1_5_ACADEMIC_ITEMS = [
    {
        "item_type": "multiple_choice",
        "prompt": "Select the correct definite article for feminine singular nouns: '_____ pasta'",
        "options": ["la", "il", "lo", "le"],
        "correct_answer": "la",
        "explanation": "Feminine singular nouns use 'la' as the definite article.",
        "weak_point": "article_agreement",
    },
    {
        "item_type": "fill_blank",
        "prompt": "Complete with the correct question word: '_____ si chiama?' (What is his/her name?)",
        "options": None,
        "correct_answer": "Come",
        "explanation": "'Come' means 'how' or 'what' in questions about manner or identity.",
        "weak_point": "question_words",
    },
    {
        "item_type": "multiple_choice",
        "prompt": "Which sentence correctly expresses negation with 'piacere'?",
        "options": ["Non mi piacciono i dolci.", "Mi non piacciono i dolci.", "Mi piacciono non i dolci.", "Non mi piace i dolci."],
        "correct_answer": "Non mi piacciono i dolci.",
        "explanation": "'Non' precedes the verb. 'Piacciono' is used with plural nouns.",
        "weak_point": "negation",
    },
    {
        "item_type": "short_writing",
        "prompt": "Read the menu: 'Caffè €1.50, Cappuccino €2.00, Cornetto €1.80'. Write a sentence stating the total cost of one cappuccino and one cornetto.",
        "options": None,
        "correct_answer": "Un cappuccino e un cornetto costano tre euro e ottanta.",
        "keywords": ["cappuccino", "cornetto", "euro"],
        "explanation": "Reading comprehension: add the prices and express the total in Italian.",
        "weak_point": "menu_comprehension",
    },
    {
        "item_type": "multiple_choice",
        "prompt": "Choose the correct form of 'piacere': 'Mi _____ le fragole.' (I like strawberries.)",
        "options": ["piacciono", "piace", "piacere", "piaci"],
        "correct_answer": "piacciono",
        "explanation": "'Le fragole' is plural, so 'piacere' conjugates to 'piacciono'.",
        "weak_point": "piacere",
    },
    {
        "item_type": "short_writing",
        "prompt": "Write two sentences: one expressing what food you like, and one expressing what food you do not like. Use 'mi piace/piacciono' and 'non mi piace/piacciono'.",
        "options": None,
        "correct_answer": "Mi piace la pizza. Non mi piacciono i broccoli.",
        "keywords": ["mi piace", "non mi"],
        "explanation": "Practice expressing preferences with correct verb agreement and negation.",
        "weak_point": "piacere",
    },
]


def generate_a1_5_quiz(count: int = 5, study_mode: str = "daily_communication") -> dict:
    exercise_id = str(uuid.uuid4())
    items_source = A1_5_ACADEMIC_ITEMS if study_mode == "academic_purpose" else A1_5_ITEMS
    title = "A1.5 Academic Grammar and Reading Quiz" if study_mode == "academic_purpose" else "A1.5 Grammar and Vocabulary Quiz"
    instructions = "Answer the following exam-style questions focusing on grammar accuracy and reading comprehension." if study_mode == "academic_purpose" else "Answer the following questions about café vocabulary, grammar, and expressions."

    items = []
    for i, item_data in enumerate(items_source[:count]):
        item = {
            "item_id": f"{exercise_id}-{i}",
            "item_type": item_data["item_type"],
            "prompt": item_data["prompt"],
            "options": item_data["options"],
            "order_index": i + 1,
        }
        items.append(item)
    return {
        "exercise_id": exercise_id,
        "unit_code": "A1.5",
        "activity_type": "quiz",
        "title": title,
        "instructions": instructions,
        "items": items,
        "study_mode": study_mode,
        "_internal": items_source[:count],
    }


def _first_objective(unit, objective_type: str, fallback: str) -> str:
    items = unit.objectives.get(objective_type, [])
    return items[0] if items else fallback


def _objective_options(unit, preferred_type: str, correct: str, fallback_options: list[str]) -> list[str]:
    values = [item for item in unit.objectives.get(preferred_type, []) if item != correct]
    values.extend(option for option in fallback_options if option != correct)
    options = [correct]
    for value in values:
        if value not in options:
            options.append(value)
        if len(options) == 4:
            break
    while len(options) < 4:
        options.append(f"Practice topic {len(options)}")
    return options


def generate_curriculum_quiz(unit, count: int = 5, study_mode: str = "daily_communication") -> dict:
    exercise_id = str(uuid.uuid4())
    communication_goal = _first_objective(unit, "communicative_goal", unit.title)
    grammar_goal = _first_objective(unit, "grammar", unit.title)
    vocabulary_goal = _first_objective(unit, "vocabulary", unit.title)
    speaking_goal = _first_objective(unit, "speaking", communication_goal)
    writing_goal = _first_objective(unit, "writing", communication_goal)
    reading_goal = _first_objective(unit, "reading", communication_goal)
    mode_is_academic = study_mode == "academic_purpose"

    base_items = [
        {
            "item_type": "multiple_choice",
            "prompt": f"What is the main focus of {unit.code} — {unit.title}?",
            "options": _objective_options(
                unit,
                "communicative_goal" if not mode_is_academic else "academic_certification",
                communication_goal if not mode_is_academic else _first_objective(unit, "academic_certification", communication_goal),
                [unit.title, grammar_goal, vocabulary_goal, reading_goal],
            ),
            "correct_answer": communication_goal if not mode_is_academic else _first_objective(unit, "academic_certification", communication_goal),
            "explanation": "This answer comes from the curriculum objectives for this unit.",
            "weak_point": "unit_objectives",
        },
        {
            "item_type": "short_answer",
            "prompt": f"Name one vocabulary or topic area practiced in {unit.code}.",
            "options": None,
            "correct_answer": vocabulary_goal,
            "keywords": [word.lower() for word in vocabulary_goal.replace(",", "").split()[:2] if len(word) > 2] or [unit.title.split()[0].lower()],
            "explanation": f"One vocabulary focus for this unit is: {vocabulary_goal}.",
            "weak_point": "vocabulary_focus",
        },
        {
            "item_type": "multiple_choice",
            "prompt": f"Which grammar point belongs to {unit.code}?",
            "options": _objective_options(unit, "grammar", grammar_goal, [communication_goal, vocabulary_goal, speaking_goal]),
            "correct_answer": grammar_goal,
            "explanation": "The grammar point is listed in the curriculum for this unit.",
            "weak_point": "grammar_focus",
        },
        {
            "item_type": "short_answer",
            "prompt": f"What speaking task should you be able to do after {unit.code}?",
            "options": None,
            "correct_answer": speaking_goal,
            "keywords": [word.lower() for word in speaking_goal.replace(",", "").split()[:2] if len(word) > 2] or ["speak"],
            "explanation": f"The speaking objective is: {speaking_goal}.",
            "weak_point": "speaking_focus",
        },
        {
            "item_type": "short_writing",
            "prompt": f"Write one short sentence in Italian related to {unit.title}.",
            "options": None,
            "correct_answer": writing_goal,
            "keywords": [],
            "explanation": f"A good answer should connect to the writing objective: {writing_goal}.",
            "weak_point": "writing_focus",
        },
        {
            "item_type": "multiple_choice",
            "prompt": f"Which activity is part of {unit.code}?",
            "options": _objective_options(
                unit,
                "reading",
                reading_goal,
                [activity.title for activity in unit.activities] + [grammar_goal, vocabulary_goal],
            ),
            "correct_answer": reading_goal,
            "explanation": "This item checks whether you recognize a curriculum activity/objective for the unit.",
            "weak_point": "reading_focus",
        },
    ]

    selected_items = base_items[: max(1, min(count, len(base_items)))]
    items = []
    for i, item_data in enumerate(selected_items):
        items.append({
            "item_id": f"{exercise_id}-{i}",
            "item_type": item_data["item_type"],
            "prompt": item_data["prompt"],
            "options": item_data["options"],
            "order_index": i + 1,
        })

    return {
        "exercise_id": exercise_id,
        "unit_code": unit.code,
        "activity_type": "quiz",
        "title": f"{unit.code} {unit.title} {'Academic' if mode_is_academic else 'Practice'} Quiz",
        "instructions": "Answer the questions using the unit objectives and lesson context.",
        "items": items,
        "study_mode": study_mode,
        "_internal": selected_items,
    }
