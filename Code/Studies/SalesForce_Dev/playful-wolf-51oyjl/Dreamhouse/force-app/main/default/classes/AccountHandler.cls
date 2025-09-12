public with sharing class AccountHandler {
  // Base generator: always 8 digits (last 8 of current epoch milliseconds)
  private static String generateAccountNumber8() {
    String ms = String.valueOf(Datetime.now().getTime()); // digits only
    return ms.substring(ms.length() - 8); // 8 chars
  }

  // Try up to 3 times to avoid a rare collision; then fall back.
  private static String generateAccountNumber8Unique() {
    for (Integer i = 0; i < 3; i++) {
      String num = generateAccountNumber8();
      if ([SELECT COUNT() FROM Account WHERE AccountNumber = :num] == 0) {
        return num;
      }
    }
    return generateAccountNumber8();
  }

  // Inserts a new Account with a valid AccountNumber.
  // Returns the Account on success, or null if DML fails (e.g., blank name).
  public static Account insertNewAccount(String accountName) {
    try {
      Account newAccount = new Account(
        Name = accountName,
        AccountNumber = generateAccountNumber8Unique()
      );
      insert newAccount;
      return newAccount;
    } catch (DmlException e) {
      System.debug('A DML exception has occurred: ' + e.getMessage());
      return null;
    }
  }
}
