CREATE OR REPLACE PACKAGE PKG_BANK_OPERATIONS AS

  /* TODO enter package declarations (types, exceptions, methods etc) here */
  -- Procedures for inserts
  procedure p_insert_customer(FIRST_NAME varchar2, EGN number, ADDRESS varchar2,
                              PHONE number, LAST_NAME varchar2);
                              
  procedure p_update_customer(ip_FIRST_NAME varchar2, ip_EGN number, ip_ADDRESS varchar2,
                              ip_PHONE number, ip_LAST_NAME varchar2);
                              
  procedure p_insert_bank_account(IBAN varchar2, BALANCE number, CURRENCY varchar2,
                                  CUSTOMER_ID number);
                                  
  procedure p_insert_bank_account2(IBAN varchar2, BALANCE number, CURRENCY varchar2, CUSTOMER_ID number);

  procedure p_make_transacton(ip_AMOUNT number, ip_IBAN_FROM varchar2, ip_IBAN_TO varchar2);
END PKG_BANK_OPERATIONS;
