for x in range (1,31):
    print("BingBong" if x%15 == 0 else "Bing" if x%3==0 else"Bong" if x%5==0 else x)