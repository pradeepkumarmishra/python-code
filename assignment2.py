import json

with open("/Users/pradeepmishra/Downloads/Assignment_JSON_Generators_Decorators/sales_data.json", "r") as f:
    data = json.load(f)

    #task 2
    categorized_data = {}
    for d in data:
        if d['category'] not in categorized_data:
            categorized_data[d['category']] = d['price_per_unit'] * d['quantity']
        else:
            categorized_data[d['category']] += d['price_per_unit'] * d['quantity']



    # sales_result = [{"category": key, "total_sales": value } for key, value in categorized_data.items()]
    # print(json.dumps(sales_result))
    # # task 3
    # json_str = json.dumps(sales_result, indent=4)
    #
    # with open("aggregated_sales.json", "w") as f:
    #     f.write(json_str)
    #
    # task 4
    # def read_and_filter_temperatures(file_name, threshold):
    #     with open(f"/Users/pradeepmishra/Downloads/Assignment_JSON_Generators_Decorators/{file_name}", "r") as file:
    #         for line in file.readlines():
    #             sensor_name,temp = line.strip().split(',')
    #             if float(temp) > threshold:
    #                 yield temp
    #
    # sensor_data = read_and_filter_temperatures("sensor_data.txt", 20)
    # for sensor in sensor_data:
    #     print(sensor)

    # task 5
    def cache_decorator(func):
        ticker_cache = {}
        def wrapper(*args, **kwargs):
            if args in ticker_cache:
                print("Getting company from cache...")
            else:
                ticker_cache[args] = func(*args, **kwargs)
            return ticker_cache[args]
        return wrapper


    @cache_decorator
    def get_company_name(ticker):
        """Simulated API function to fetch a company name based on the ticker symbol."""
        # Simulate different responses based on the ticker symbol
        print("Getting api name from api...")
        api_responses = {
            "AAPL": "Apple Inc.",
            "MSFT": "Microsoft Corporation",
            "GOOGL": "Alphabet Inc."
        }
        return api_responses.get(ticker, "Unknown Company")

    print(get_company_name("AAPL"))  # Expected to trigger an API call
    print(get_company_name("AAPL"))
    print(get_company_name("AAPL"))
    print(get_company_name("MSFT"))  # Expected to trigger an API call
    print(get_company_name("MSFT"))  # Expected to use cached data
    print(get_company_name("GOOGL"))  # Expected to trigger an API call
    print(get_company_name("GOOGL"))



