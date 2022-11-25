def describe_city(city, country='chile'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('mardan')
describe_city('gujrawala', 'toronto')
describe_city('buneer')