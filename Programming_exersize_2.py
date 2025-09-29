# Abrianna Johnson
# 9/21/25

Spam_Keywords = [
    'free', 'guaranteed', 'urgent', 'cash',
    'buy now', 'special offer', 'free gift', 'act now',
    'limited time offer', 'exclusive deal', 'click here',
    'order now', 'urgent', "you've been selected",
    'verify your account', 'security alert', 'immediately',
    'hurry', 'important', 'offer', 'deal', 'winner', 'promo',
    'free trial', 'save', 'subscribe', 'apply', 'join',
    'sign up', 'confirm']

def calculate_spam_score(message, keywords):
    spam_score = 0
    # Accumulator for the number of spam keywords
    found_keywords = []
    message_lower = message.lower()
    # Converts the message to all lowercase letters

    for keyword in keywords:
        # Counts the number of keywords in the message
        count = message_lower.count(keyword.lower())
        if count > 0:
            spam_score += count
            found_keywords.append(keyword)
    return spam_score, found_keywords

def spam_likelihood(score):
    if score == 0:
        return 'Very Unlikely to be Spam'
    elif score <= 3:
        return 'Unlikely to be Spam'
    elif score <= 5:
        return 'Somewhat Likely to be Spam'
    elif score <= 7:
        return 'Likely to be Spam'
    else:
        return 'Very Likely to be Spam'

def main():
    print('Enter your message to check for spam emails.')
    user_message = input('Your message: ')

    score, triggered = calculate_spam_score(user_message, Spam_Keywords)
    likelihood = spam_likelihood(score)

    print("\n------ Results ------")
    print(f'Spam Score: {score}')
    print(f'Likelihood of Spam: {likelihood}')
    print('---------------------------------')

    if triggered:
        print('Spam keywords found:')
        for word in triggered:
            print(f'- {word}')
    else:
        print('No spam keywords found')

if __name__ == "__main__":
    main()