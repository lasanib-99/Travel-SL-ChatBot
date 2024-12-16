def validate_user_input(user_question: str) -> bool:

    # Validate user input to ensure it's not empty or too short.
    if not user_question.strip():
        return False
    return True