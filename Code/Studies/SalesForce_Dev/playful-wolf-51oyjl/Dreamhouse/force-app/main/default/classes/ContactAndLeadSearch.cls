public with sharing class ContactAndLeadSearch {
  public static List<List<sObject>> searchContactsAndLeads(String searchName) {
    try {
      List<List<sObject>> results = [
        FIND :searchName
        IN NAME FIELDS
        RETURNING Contact(FirstName, LastName), Lead(FirstName, LastName)
      ];
      return results;
    } catch (Exception e) {
      System.debug('Error during search: ' + e.getMessage());
      // return empty structure to satisfy return type
      return new List<List<SObject>>();
    }
  }
}
