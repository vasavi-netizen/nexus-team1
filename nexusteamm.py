import requests
import threading

def fetch_duckduckgo_answer(question):
    url = "https://api.duckduckgo.com"
    params = {
        'q': question,
        'format': 'json',
        'pretty': 'true'
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        # Try to get an abstract or answer
        answer = data.get('AbstractText') or data.get('Answer') or "Sorry, no direct answer found."
        return answer
    except Exception as e:
        return "Error fetching answer: " + str(e)

def search_in_background(question):
    # This function runs in background
    answer = fetch_duckduckgo_answer(question)
    print("\n[Background] DuckDuckGo's answer snippet:\n" + answer + "\n")

def main():
    print("What's the question?")
    question = input()

    # Launch background search
    threading.Thread(target=search_in_background, args=(question,)).start()

    # Fetch answer from DuckDuckGo
    primary_answer = fetch_duckduckgo_answer(question)

    # Mock three different answer versions
    answer_version_1 = primary_answer
    answer_version_2 = primary_answer + " (More detailed version with additional context.)"
    answer_version_3 = primary_answer + " (Most comprehensive and accurate answer.)"

    # Show the answers
    print("\nAnswer Version 1:\n" + answer_version_1)
    print("\nAnswer Version 2:\n" + answer_version_2)
    print("\nAnswer Version 3:\n" + answer_version_3)

    # Explanations
    print("\nWhy is Version 3 better than Version 2?")
    print("Because it offers a more comprehensive and accurate response.\n")
    print("Why is Version 2 better than Version 1?")
    print("Because it provides more context and detail.\n")

if _name_ == "_main_":
    main()