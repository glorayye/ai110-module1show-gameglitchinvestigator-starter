import sys
from pathlib import Path

# Add parent directory to path so we can import logic_utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, message = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, message = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, message = check_guess(40, 50)
    assert result == "Too Low"


def test_form_submit_on_enter_parses_input():
    """
    Test the complete submit flow when user presses Enter in the form.
    Enter -> Form Submit -> parse_guess() -> check_guess() -> update_score()
    """
    # Simulate user pressing Enter with input "42" when secret is 50
    raw_input = "42"
    secret = 50
    current_score = 0
    attempt = 1
    
    # Step 1: Parse the input (happens on form submission)
    ok, parsed_guess, error_msg = parse_guess(raw_input)
    assert ok == True, "Form input should parse successfully"
    assert parsed_guess == 42, "Should convert string '42' to integer 42"
    assert error_msg is None, "No error should occur for valid input"
    
    # Step 2: Check the guess against secret
    result, message = check_guess(parsed_guess, secret)
    assert result == "Too Low", "Guess 42 should be too low compared to 50"
    assert "LOWER" in message, "Message should contain hint to go lower"
    
    # Step 3: Update score based on the result
    from logic_utils import update_score
    new_score = update_score(current_score, result, attempt)
    assert new_score == -5, "Too Low on first attempt should deduct 5 points"
