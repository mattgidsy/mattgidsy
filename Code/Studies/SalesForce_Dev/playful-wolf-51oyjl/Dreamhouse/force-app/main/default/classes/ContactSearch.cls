public with sharing class ContactSearch {
  public static List<Contact> searchForContacts(
    String lastName,
    String postCode
  ) {
    List<Contact> results = new List<Contact>();
    try {
      results = [
        SELECT Id, Name
        FROM Contact
        WHERE LastName = :lastName AND MailingPostalCode = :postCode
      ];
    } catch (Exception e) {
      System.debug('Error during contact search: ' + e.getMessage());
      // results stays as an empty list
    }
    return results;
  }
}
