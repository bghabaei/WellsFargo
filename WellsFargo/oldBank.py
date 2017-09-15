    # Wells Fargo - Automatic Teller Machine (References)

bankMoto = str ("Together Well Go Far");
bankWelcome = str ("Welcome to Wells Fargo. " + bankMoto);
bankGoodbye = str ("Goodbye from Wells Fargo. " + bankMoto);
askBankNumber = str ("Enter Bank Number:" );
askBankKey = str ("Enter Bank Key:");
bankNumber = int (input(askBankNumber));
bankKey = int (input(askBankKey));

    # Wells Fargo - Automatic Teller Machine (Definitions)

def goBank():
    print (bankWelcome);
    print (askBankNumber);
    print (askBankKey);
    print (bankGoodbye);

    # Wells Fargo - Automatic Teller Machine (Constructors)

