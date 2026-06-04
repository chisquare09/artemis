# Speaking Roleplay v1

Text-based café ordering roleplay for A1.5 unit.

## Overview

Learners practice ordering at an Italian café by responding to waiter prompts. This version is text-based; voice/speech features will be added later.

## Scenario

- **Scenario ID**: `cafe_ordering`
- **Roles**: Waiter (AI) / Customer (learner)
- **Turns**: 3 waiter prompts

### Waiter Turns
1. "Buongiorno! Cosa desidera?"
2. "Certo. Altro?"
3. "Sono tre euro."

## Evaluation

Responses are evaluated for:
- **Café vocabulary**: caffè, cappuccino, cornetto, etc.
- **Polite phrases**: per favore, grazie, prego
- **Ordering phrases**: vorrei, prendo, posso avere
- **Price/bill phrases**: quanto costa, il conto

### Weak Points Detected
- `cafe_vocabulary`
- `polite_phrases`
- `ordering_phrase`
- `asking_for_bill`
- `asking_prices`

## API Endpoints

### POST /api/speaking/roleplay/start
```json
{ "unit_code": "A1.5", "scenario_id": "cafe_ordering" }
```
Returns session_id and first waiter turn.

### POST /api/speaking/roleplay/respond
```json
{ "session_id": "...", "message": "Vorrei un caffè, per favore." }
```
Returns feedback and next waiter turn.

### POST /api/speaking/roleplay/finish
```json
{ "session_id": "..." }
```
Returns score and summary.

## Frontend Components

- `SpeakingRoleplay` - Main container
- `RoleplayChat` - Conversation display
- `RoleplayMessage` - Single message bubble
- `RoleplayFeedback` - Final score display

## Future Enhancements

- Voice input (speech-to-text)
- Pronunciation scoring
- More scenarios beyond café ordering
