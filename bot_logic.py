import random
def gen_pass(pass_length):
    elements = "1234567890!@#$%^&*()-_=+[]{};:,.<>?/ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def coinflip():
    num = random.randint(1,2)
    if num == 1:
        return "Heads"
    else:
        return "Tails"
    
def roll_dice():
    return random.randint(1,6)

def qotd():
    quotes_of_the_day = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Don't watch the clock; do what it does. Keep going. – Sam Levenson"
    "You miss 100 percent of the shots you don't take. – Wayne Gretzky",
    "The best time to plant a tree was 20 years ago. The second best time is now. – Chinese Proverb",
    "It does not matter how slowly you go as long as you do not stop. – Confucius",
    "Everything you’ve ever wanted is on the other side of fear. – George Addair",
    "Hardships often prepare ordinary people for an extraordinary destiny. – C.S. Lewis",
    "Dream big and dare to fail. – Norman Vaughan",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. – Zig Ziglar",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "Don’t wait. The time will never be just right. – Napoleon Hill",
    "Act as if what you do makes a difference. It does. – William James",
    "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau",
    "Keep your face always toward the sunshine—and shadows will fall behind you. – Walt Whitman",
    "Opportunities don't happen, you create them. – Chris Grosser",
    "Try not to become a man of success, but rather try to become a man of value. – Albert Einstein",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Don’t stop when you’re tired. Stop when you’re done."]

    qts = random.choice(quotes_of_the_day)
    return qts

def tolong():
    hlp = "pass, coin, dice, quotes"
    return hlp
