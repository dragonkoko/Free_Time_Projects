CREATE OR REPLACE PACKAGE BODY PKG_BANK_OPERATIONS AS

  no_fk_found EXCEPTION;
  PRAGMA EXCEPTION_INIT(no_fk_found, -02291);
  cannot_insert_null EXCEPTION;
  PRAGMA EXCEPTION_INIT(cannot_insert_null, -01400);
  not_enough_money EXCEPTION;
  PRAGMA EXCEPTION_INIT(not_enough_money, -02290);
  not_existing_iban EXCEPTION;
  PRAGMA EXCEPTION_INIT(not_existing_iban, -02291);
  not_same_currency EXCEPTION;
  PRAGMA EXCEPTION_INIT(not_same_currency, -20002);
  
  procedure p_insert_customer(FIRST_NAME varchar2, EGN number, ADDRESS varchar2,
                              PHONE number, LAST_NAME varchar2) AS
  BEGIN
      insert into customers(first_name, last_name,egn, phone, address)
      values(FIRST_NAME,LAST_NAME,EGN,PHONE,ADDRESS);
      commit;
  END p_insert_customer;
  
  procedure p_update_customer(ip_FIRST_NAME varchar2, ip_EGN number, ip_ADDRESS varchar2,
                              ip_PHONE number, ip_LAST_NAME varchar2) AS
    v_cnt number;
  BEGIN
      UPDATE customers c SET c.first_name = ip_FIRST_NAME, c.address = ip_ADDRESS,
      c.phone = ip_PHONE, c.last_name = ip_LAST_NAME WHERE c.egn = ip_EGN;
      
      v_cnt := SQL%ROWCOUNT;
      
      if v_cnt = 0 then
        raise_application_error(-20002, 'No customer found');
      end if;
      
      commit;
  END p_update_customer;
  
  procedure p_insert_bank_account(IBAN varchar2, BALANCE number, CURRENCY varchar2,
                                  CUSTOMER_ID number)
                                  AS
    cnt NUMBER;                                  
  BEGIN

      SELECT COUNT(*)
      INTO cnt
      FROM CUSTOMERS
      WHERE id = CUSTOMER_ID;
      
      -- dbms_lock.sleep(10);
      
      IF( cnt != 0 ) THEN
        insert into bank_account(iban,balance,currency,customer_id)
        values(IBAN,BALANCE,CURRENCY,CUSTOMER_ID);
        commit;

      END IF;
      
    EXCEPTION
      WHEN OTHERS THEN
        ROLLBACK;
        dbms_output.put_line(dbms_utility.format_error_backtrace ||
                             dbms_utility.format_error_stack);
  END p_insert_bank_account;
  
  procedure p_insert_bank_account2(IBAN varchar2, BALANCE number, CURRENCY varchar2, CUSTOMER_ID number)
                                  AS
  BEGIN

      dbms_output.put_line('Inserting IBAN');

      insert into bank_account(iban,balance,currency,customer_id)
      values(IBAN,BALANCE,CURRENCY,CUSTOMER_ID);
      commit;

    EXCEPTION
      WHEN no_fk_found THEN
        dbms_output.put_line('No foreign key found');
        raise_application_error(-20001, 'No foreign key found');
        ROLLBACK;
      WHEN OTHERS THEN
        dbms_output.put_line(dbms_utility.format_error_backtrace ||
                             dbms_utility.format_error_stack);
        ROLLBACK;
  END p_insert_bank_account2;
  
  procedure p_make_transacton(ip_AMOUNT number, ip_IBAN_FROM varchar2, ip_IBAN_TO varchar2) AS
  from_currency varchar2(22);
  counter number;
  BEGIN
  
--      SAVEPOINT start_bank_transaction;  
  
  		if ip_AMOUNT is null then
        raise cannot_insert_null;
      end if;
      
      SELECT DISTINCT(currency) 
      INTO from_currency
      FROM bank_account
      WHERE iban = ip_IBAN_FROM;
      
      SELECT COUNT(*)
      INTO counter
      FROM BANK_ACCOUNT
      WHERE ip_IBAN_TO = iban AND from_currency = currency;
      
      IF (counter = 0) THEN
           raise not_same_currency;
      END IF;           
         
       UPDATE bank_account t SET t.BALANCE = (t.BALANCE - ip_AMOUNT) WHERE t.IBAN = ip_IBAN_FROM;
       UPDATE bank_account t SET t.BALANCE = (t.BALANCE + ip_AMOUNT) WHERE t.IBAN = ip_IBAN_TO;
       insert into transactions(transaction_date,amount,iban_from,iban_to)
                   values(CURRENT_TIMESTAMP,ip_AMOUNT,ip_IBAN_FROM,ip_IBAN_TO);  
       commit;
       EXCEPTION
         WHEN cannot_insert_null THEN
           dbms_output.put_line('Cannot INSERT NULL');
           -- ROLLBACK TO start_bank_transaction;
           rollback;
         WHEN not_enough_money THEN
           dbms_output.put_line('Not enough money in IBAN FROM ' || ip_IBAN_FROM);
           --ROLLBACK TO start_bank_transaction;
           rollback;           
         WHEN not_existing_iban THEN
           dbms_output.put_line('Not Existing IBAN');
           -- ROLLBACK TO start_bank_transaction;
           rollback;
         WHEN not_same_currency THEN
           dbms_output.put_line('The currency is not the same');
           -- ROLLBACK TO start_bank_transaction;
           rollback;         
         WHEN OTHERS THEN
           dbms_output.put_line('Unknown Exception');
           -- ROLLBACK TO start_bank_transaction;
           rollback;           

  END p_make_transacton;
  
END PKG_BANK_OPERATIONS;
