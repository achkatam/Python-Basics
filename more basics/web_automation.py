import webbrowser as wbb


def web_automation():
    print(f'What should I look for ?')
    my_search = input()

    print(f'Opening now!')
    wbb.open(f'https://www.google.com/search?q=' + my_search)

web_automation()
