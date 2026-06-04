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
