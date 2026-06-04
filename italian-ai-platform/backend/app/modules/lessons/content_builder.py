from app.modules.curriculum.service import get_unit
from app.modules.lessons.schema import (
    LessonActivityResponse,
    LessonAIHelperContextResponse,
    LessonDetailResponse,
    LessonProgressResponse,
)

MODE_CONFIG = {
    "daily_communication": {
        "label": "Daily Communication",
        "focus": "Practical café conversation, listening, speaking, and everyday interaction",
        "guidance": "Focus on ordering food/drinks, asking prices, asking for the bill, roleplay and listening.",
    },
    "academic_purpose": {
        "label": "Academic Purpose",
        "focus": "Structured grammar, reading comprehension, writing accuracy, and exam-style practice",
        "guidance": "Focus on articles with food nouns, question words, negation, piacere, menu reading comprehension, short written responses.",
    },
}


def build_lesson_detail(unit_code: str, study_mode: str = "daily_communication") -> LessonDetailResponse:
    unit = get_unit(unit_code)
    mode = MODE_CONFIG.get(study_mode, MODE_CONFIG["daily_communication"])

    activities = [
        LessonActivityResponse(
            activity_type=a.activity_type,
            title=a.title,
            description=a.description,
            skill_focus=a.skill_focus,
            order_index=a.order_index,
        )
        for a in unit.activities
    ]

    progress = LessonProgressResponse()

    ai_context = LessonAIHelperContextResponse(
        unit_code=unit.code,
        level=unit.level_code,
        title=unit.title,
        summary=unit.summary,
        objective_types=list(unit.objectives.keys()),
    )

    return LessonDetailResponse(
        level=unit.level_code,
        unit_code=unit.code,
        title=unit.title,
        summary=unit.summary,
        objectives=unit.objectives,
        activities=activities,
        progress=progress,
        ai_helper_context=ai_context,
        study_mode=study_mode,
        mode_label=mode["label"],
        mode_focus=mode["focus"],
        mode_specific_guidance=mode["guidance"],
    )
